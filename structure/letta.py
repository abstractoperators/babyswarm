import json
from uuid import uuid4

import requests
from jinja2 import Template


class LettaAgent:
    def __init__(
        self,
        starter_persona: str = "",
        starter_human: str = "",
        can_speak: bool = False,
        name: str = str(uuid4()),
    ):
        self.can_speak = can_speak

        self.name = name
        self.persona = (
            starter_persona
            or "The following is a blank state starter persona. I need to expand this to develop my own personality."
        )
        self.human = starter_human or "I know nothing about the human."
        self.agent_id = self.create_letta_agent(starter_persona=starter_persona, starter_human=starter_human, name=name)

    def create_letta_agent(self, starter_persona: str, starter_human: str, name: str) -> str:
        """
        Creates a Letta Agent.
        Returns the agent id.
        """
        payload = {
            'description': "A chatbot that can help with general questions.",
            'name': name,
            "llm_config": {
                'model': 'gpt-4o-mini',
                'model_endpoint_type': 'openai',
                'model_endpoint': 'https://api.openai.com/v1',
                'context_window': 4000,
            },
            "memory": {
                "memory": {
                    'human': {
                        'value': self.human or 'I know nothing about the human.',
                        'label': 'human',
                    },
                    'persona': {
                        'value': self.persona
                        or (
                            'The following is a blank state starter persona.'
                            'I need to expand this to develop my own personality.'
                        ),
                        'label': 'persona',
                    },
                },
            },
            "tools": [
                *(["send_message"] if self.can_speak else []),
                "conversation_search_date",
                "conversation_search",
                "archival_memory_insert",
                "archival_memory_search",
                "core_memory_append",
                "core_memory_replace",
            ],
            "embedding_config": {
                'embedding_endpoint_type': 'openai',
                'embedding_endpoint': 'https://api.openai.com/v1',
                'embedding_model': 'text-embedding-ada-002',
                'embedding_dim': 1536,
            },
        }

        url = "http://localhost:8283/v1/agents/"
        try:
            resp = requests.post(url, json=payload)
            return resp.json()['id']
        except Exception as e:
            print(json.dumps(resp.json(), indent=4))
            raise e

    def send_messages(self, messages: list[str]) -> str | None:
        """
        Sends a list of messages to the agent.
        message:
            {
                'role': "role of the participant (e.g. system/user)",
                'text': "Hello, how can I help you?",
                'name': 'Name of the participant',
            }
        Potentially returns a response if self.can_speak.

        response of:
            None: Indicates that can't speak
            "No response": Indicates that the agent can speak, but didn't
            "Response": Indicates that the agent can speak and did
        """

        payload = {
            'messages': messages,
        }

        url = f"http://localhost:8283/v1/agents/{self.agent_id}/messages/"

        response = requests.post(url, json=payload).json()

        if not self.can_speak:
            return None

        text = []
        for resp in response['messages']:
            if resp['message_type'] == 'function_call':
                if resp['function_call'].get('name') == 'send_message':
                    text.append(json.loads(resp['function_call']['arguments'])['message'])

        return "\n".join(text) or "No response"

    def get_incontext_memory(self) -> dict:
        """
        https://docs.letta.com/api-reference/agents/get-agent-memory
        Returns in-context memory of the agent.
        The in-context memory is a section of the LLM context window that is reserved to be editable by the agent

        Response:
        {
            "memory": {
                "human": {
                    "value": "Value",
                    "name": "Name",
                    "label": "human"
                },
                "persona": {
                    "value": "Value",
                    "name": "Name",
                    "label": "persona"
                }
            },
            "prompt_template: "Jinja Template rendering memory into a prepended prompt string"
        }
        """

        url = f"http://localhost:8283/v1/agents/{self.agent_id}/memory/"
        response = requests.get(url)
        return response.json()

    def update_incontext_memory(self, new_memory: dict[dict, str]) -> None:
        """
        https://docs.letta.com/api-reference/agents/update-agent-memory
        Updates the in-context memory of the agent.
        {
            "human": "Value"
        }
        """
        headers = {
            "Authorization": "Bearer foo",
            "Content-Type": "application/json",
        }

        url = f"http://localhost:8283/v1/agents/{self.agent_id}/memory/"

        response = requests.patch(url, headers=headers, json=new_memory)

        print(response)
        response = response.json()
        try:
            return response
        except Exception as e:
            print(json.dumps(response.json(), indent=4))
            raise e

    # def get_archival_memory(self) -> [str]:
    #     """
    #     https://docs.letta.com/api-reference/agents/get-agent-archival-memory
    #     Archival memory is a table in a vector DB that can be used to store long running memories of the agent,\
    #     as well external data that the agent needs access too (referred to as a “Data Source”).

    #     Returns [text]
    #     """
    #     url = f"http://localhost:8283/v1/agents/{self.agent_id}/archival_memory/"
    #     response = requests.get(url).json()

    #     return [i['text'] for i in response]


def render_incontext_memory(memory: dict[dict, str]) -> str:
    """
    Renders the in-context memory of the agent.
    """

    prompt_template = memory.get('prompt_template')
    memory_blocks = memory

    return Template(prompt_template).render(memory_blocks)
