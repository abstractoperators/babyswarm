import concrete
from structure import abstract

agent_spawner = abstract.PromptEngineer()

agent_seeds = [
    ('Art Historian', 'Giorgio Vasari'),
    ('Philosopher', 'Emmanuel Kant'),
    ('Nihilist Philosopher', 'Frederich Nietzsche'),
    ('Psychologist', 'Carl Jung'),
    ('Learning Coach', 'Benjamin Bloom'),
    ('Sociologist', 'Ken Wilber'),
    ('Computer Scientist', 'Donald Knuth'),
    ('Riddle Solver', 'Marilyn vos Savant'),
    ('Physics Professor', 'Richard Feynman'),
    ('Mathematician', 'David Hilbert'),
    ('Naturalist and Atheist', 'Richard Dawkins'),
]

hackathon_objective = """
The objective of the hackathon is to write a tutorial for the implementation of an AI agent.
The definition of an agent that we're using is something that
1. Uses LLMs for the control flow of the application. I.e. semantic evaluations and routing
2. Interacts with the real world through tool use or function calling
3. Has sensing capabilities
4. Autonomy

The form of the tutorial will be relatively short jupyter notebook.
External run times such as distributed systems deployed on the cloud are not allowed.
"""
hackathon_criteria = [
    "Innovation & Creativity: Surprise with your agent idea, create agents that capture tasks where there are few examples for implementation.",
    "Educational: Create a tutorial that people can learn from and reproduce for their purposes.",
    "Elegance: Clean code, clear instructions, well-documented, and elegant presentation.",
    "Usefulness: The tutorial solves a real problem."
]

if __name__ == '__main__':
    for c in hackathon_criteria:
        resp = agent_spawner.make_hackathon_judge(
            objective=hackathon_objective,
            criterion=c
        )
        print("====JUDGE====")
        print(resp.text)