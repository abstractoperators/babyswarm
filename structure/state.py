import json

universe_path = "./state/universe-state.json"



def fetch_universe():
    with open(universe_path, 'r') as f:
        state = json.load(f)
    return state

def save_universe(state):
    with open(universe_path, 'w') as f:
        json.dump(state, f, indent=4, sort_keys=True)


s = fetch_universe()
s['yoo'] = 'gurt'
save_universe(s)
