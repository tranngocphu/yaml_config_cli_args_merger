import yaml
import argparse

def load_config(config_path):
    """Load default parameters from a YAML configuration file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
    

def flatten_dict(d, parent_key='', sep='.'):
    """Flatten nested dictionaries using dot notation."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def nested_update(d, keys, value):
    """Recursively update a nested dictionary given a list of keys."""
    for key in keys[:-1]:
        d = d.setdefault(key, {})
    d[keys[-1]] = value
    
    
def parse_cli_args(flat_config):
    """Dynamically generate CLI arguments based on the flattened config structure."""
    parser = argparse.ArgumentParser(description="Override hierarchical config via CLI.")
    parser.add_argument('--target_config', type=str, default='')
    for key, val in flat_config.items():
        arg_type = type(val) if val is not None else str  # Default to str if None
        parser.add_argument(f"--{key}", type=arg_type, help=f"Override for {key}")

    args = vars(parser.parse_args())  # Convert namespace to dict
    return {k: v for k, v in args.items() if v is not None}  # Remove None values


def merge_config_and_cli(config, cli_args):
    """Merge CLI arguments into the hierarchical config."""
    for flat_key, value in cli_args.items():
        nested_keys = flat_key.split('.')
        nested_update(config, nested_keys, value)
    return config