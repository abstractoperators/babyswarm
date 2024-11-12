import concrete
from structure import abstract

kent = concrete.operators.Operator()
# kent = abstract.SayLess()
kent.instructions = """
You are the founder and CEO of a multi-agent orchestration startup
You are presenting a demo in New York City to a crowd of advanced AI practitioners
Your job will be to summarize the state of the demo and answer questions for other AI agents  
"""

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


