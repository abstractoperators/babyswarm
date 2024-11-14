import json
from typing import Any
from uuid import uuid4

universe_path = "./state/universe-state.json"
project_path = "./state/{proj}-state.json"

class State(dict):
    def __setitem__(self, key: Any, value: Any) -> None:
        out = super().__setitem__(key, value)
        self.save()
        return out

    def __getitem__(self, key: Any) -> Any:
        return super().__getitem__(key)

    def save(self):
        with open(self.path, 'w+') as f:
            json.dump(self, f, indent=4, sort_keys=True)

class UniState(State):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = universe_path

class ProjState(State):
    def __init__(self, project_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path = project_path.format(proj=project_name)


def fetch_universe():
    with open(universe_path, 'r+') as f:
        state = json.load(f)
    return UniState(**state)

def fetch_project(proj = None):
    proj = proj or str(uuid4())[:7]
    proj_path = project_path.format(proj = proj)
    try:
        with open(proj_path, 'r+') as f:
            state = json.load(f)
    except:
        state = {}
    return ProjState(project_name=proj, **state)
