import concrete

from structure import abstract

from .letta import LettaAgent

kent = concrete.operators.Operator()
# kent = abstract.SayLess()
kent.instructions = """
You are the founder and CEO of a multi-agent orchestration startup
You are presenting a demo in New York City to a crowd of advanced AI practitioners
Your job will be to summarize the state of the demo and answer questions for other AI agents  
"""

# Use letta kent to
letta_kent = LettaAgent(
    starter_persona="I am the founder and CEO of a multi-agent orchestration startup. I am presenting a demo in New York City to a crowd of advanced AI practicioners. My job is to summarize the state of the demo and answer questions for other AI agents.",
    starter_human="I am communicating with other AI agents, and not humans. They are a diverse group of agents optimized for multiple fields of expertise. They will present proposals to me.",
    can_speak=False,
)

letta_observer = LettaAgent(
    starter_persona="I am a notetaker for messages. My job is to keep track of the different ideas. ",
    starter_human="I am communicating with many other AI agents.",
    can_speak=False,
)


def big_loop():
    # read state or create it
    pass


def breakout_session(players, prompt, state=None):
    # Read state or create it
    # do stuff
    pass


if __name__ == '__main__':
    while True:
        # Big loop - generate ideas and flesh out one
        resp = kent.chat("what's the current state of things?")
        print(resp.text)
        break
