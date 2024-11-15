import json
import random

import concrete
import concrete.projects

from structure import abstract
from structure.letta import letta_observer
from structure.operators import employees, historical
from structure.tools import convo

from structure import state

UNIVERSE_STATE = state.fetch_universe()

kent = employees.Kent()
miguel = employees.Builder()
andy = employees.Designer()

employees = [
    kent, 
    miguel,
    andy
]

humanities = [
    historical.ArtHistorian(),
    historical.Philosopher(),
    historical.Nihilist(),
    historical.Psychologist(),
    historical.LearningCoach(),
    historical.Sociologist(),
]

sciences = [
    historical.ComputerScientist(),
    historical.Riddler(),
    historical.Physicist(),
    historical.Mathematician(),
    historical.Naturalist(),
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
                "tools": [convo.ConversateTool],
            },
        ).tool_parameters[0].value
        proj_state['reactions'] = proj_state['reactions'] + [f"{player.__class__.__name__}: {idea}"]
    return proj_state


def main():
    while True:
        proj = breakout_session(random.sample(company, breakout_size), generate_idea_prompt)
        proj['final_summary'] = kent.chat(
            f"""Summarize this idea brainstorm: {json.dumps(proj)}"""
        ).text

if __name__ == '__main__':
    main()