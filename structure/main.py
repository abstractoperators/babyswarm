import json
import random

import concrete
import concrete.projects

import abstract
from abstract import letta_observer
import operators
import tools

import state

UNIVERSE_STATE = state.fetch_universe()

kent = operators.Kent()
miguel = operators.Builder()
andy = operators.Designer()

employees = [
    kent, 
    miguel,
    andy
]

humanities = [
    operators.ArtHistorian(),
    operators.Philosopher(),
    operators.Nihilist(),
    operators.Psychologist(),
    operators.LearningCoach(),
    operators.Sociologist(),
]

sciences = [
    operators.ComputerScientist(),
    operators.Riddler(),
    operators.Physicist(),
    operators.Mathematician(),
    operators.Naturalist(),
]

company = employees + humanities + sciences
breakout_size = 3

generate_idea_prompt = """
    Generate exactly one creative use case for multi-agent orchestration.
    It should not be the same as previous ideas you may have generated.
"""

def breakout_session(players: list[abstract.SayLess], prompt):
    proj_state = state.fetch_project()
    UNIVERSE_STATE['projects'] = UNIVERSE_STATE['projects'] + [proj_state.path]

    player = players[0]
    memories = letta_observer.get_incontext_memory()
    print("memories", memories)
    idea = player.be_concise(
        f"""
You are participating in a brainstorm exercise.
There is an AI agent that is listening to all discussion across time.
This set of memories represent all the ideas you have generated so far:
{letta_observer.get_incontext_memory()}

{prompt}
 """   ).text
    proj_state['initial-idea'] = f"{player.__class__.__name__}: {idea}"
    proj_state['reactions'] = []

    for player in players[1:]:
        idea = player.be_concise(
            idea,
            options={
                "tools": [tools.ConversateTool],
            },
        ).tool_parameters[0].value
        proj_state['reactions'] = proj_state['reactions'] + [f"{player.__class__.__name__}: {idea}"]
    return proj_state


if __name__ == '__main__':
    # UNIVERSE_STATE['projects'] = []
    while True:
        proj = breakout_session(random.sample(company, breakout_size), generate_idea_prompt)
        proj['final_summary'] = kent.chat(
            f"""Summarize this idea brainstorm: {json.dumps(proj)}"""
        ).text
