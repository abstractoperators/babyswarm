import concrete
import abstract

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

if __name__ == '__main__':
    resp = agent_spawner.be_concise(
        """
Generate a prompt for an AI agent to include in a multi-agent orchestration demo

The personality and inspiration for this ai agent is
You are a great Art Historian on par with Giorgio Vasari

Your job will be to provide meaningful and creative input on projects drawing upon the works and ideas of Giorgio Vasari
"""
    )
    print(resp.text)