from typing import Any

import concrete

def one_sentence(msg: str) -> str:
    return f"{msg} \nGive a short reply of max one sentence."


def be_concise(msg: str) -> str:
    return f"{msg} \nBe concise yet expressive."


class SayLess(concrete.operators.Operator):
    def chat(self, msg: str, options: dict = {}):
        return one_sentence(msg)

    def be_concise(self, msg: str, options: dict = {}):
        return be_concise(msg)

    def answer_question(self, context, question, asker, options={}):
        return be_concise(
            f"""
The AI agent {asker.__class__.__name__} has a question based on the following context.
    
# Context
{context}

Their question is
# Question
{question}

Answer their question to the best of your ability or say "I don't know" if you don't know.
"""
        )


class PromptEngineer(SayLess, concrete.operators.PromptEngineer):
    def make_agent(self, role, model, options={}):
        return be_concise(
            f"""
Generate a prompt for an AI agent to include in a multi-agent orchestration demo

The personality and inspiration for this ai agent is
You are a great {role} on par with {model}

Your job will be to provide meaningful and creative input on projects drawing upon the works and ideas of {model}
"""
        )

    def make_hackathon_judge(self, objective, criterion, options={}):
        return be_concise(
            f"""
Generate a prompt for an AI agent to include in a multi-agent orchestration demo

You are a hackathon judge with the following objective:
{objective}

You are specifically judging for
{criterion}
"""
        )