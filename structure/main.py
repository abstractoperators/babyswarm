import concrete

from letta import LettaAgent
import operators

kent = operators.Kent()

# Use letta kent to
# letta_kent = LettaAgent(
#     starter_persona="I am the founder and CEO of a multi-agent orchestration startup. I am presenting a demo in New York City to a crowd of advanced AI practicioners. My job is to summarize the state of the demo and answer questions for other AI agents.",
#     starter_human="I am communicating with other AI agents, and not humans. They are a diverse group of agents optimized for multiple fields of expertise. They will present proposals to me.",
#     can_speak=False,
# )



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
        resp = kent.be_concise("what's the current state of things?")
        print(resp.text)

        miguel = operators.Builder()
        resp = miguel.be_concise("Am i nothing to you??")
        print(resp.text)
        break
