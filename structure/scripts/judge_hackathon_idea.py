import argparse
from structure.operators import judges

from pprint import pprint


parser = argparse.ArgumentParser(description="Idea Judger")
subparsers = parser.add_subparsers(dest="mode")
prompt_parser = subparsers.add_parser("idea")
prompt_parser.add_argument("idea", type=str)

judge_agents = [
    judges.InnovationAndCreativity(),
    judges.Educational(),
    judges.Elegance(),
    judges.Usefulessness(),
]

def judge_idea(idea: str):
    feedback = {}
    for j in judge_agents:
        feedback[j.__class__.__name__] = j.judge(idea).text
    return feedback

if __name__ == '__main__':
    args = parser.parse_args()
    feedback = judge_idea(args.idea)
    pprint(feedback)