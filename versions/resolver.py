import yaml
from pathlib import Path

REGISTRY_PATH = Path("versions/registry.yaml")

def load_versions():
    with open(REGISTRY_PATH, "r") as f:
        return yaml.safe_load(f)

def get_active_versions():
    registry = load_versions()
    return {
        "corpus": registry["corpus"]["current"],
        "prompt": registry["prompts"]["current"],
        "model": registry["model"]["name"]
    }
