import os
import yaml

def load_config():
    # Get the absolute path to the directory containing this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Move one level up to project root (since config_loader.py is inside utilities)
    project_root = os.path.dirname(current_dir)
    # Construct absolute path to config.yml
    config_path = os.path.join(project_root, "config", "config.yml")

    with open(config_path, "r") as f:
        return yaml.safe_load(f)
