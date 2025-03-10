import yaml
from utils import load_config, flatten_dict, parse_cli_args, merge_config_and_cli


if __name__ == "__main__":
    config_path = "./configs/default_config.yaml"
    
    # Load hierarchical config
    config = load_config(config_path)
    
    # Flatten config for CLI argument parsing
    flat_config = flatten_dict(config)
        
    # Parse CLI arguments
    cli_args = parse_cli_args(flat_config)
    
    # Merge CLI arguments into hierarchical config
    final_config = merge_config_and_cli(config, cli_args)    
    
    if config['target_config']:
        save_path = config['target_config']
        with open(save_path, 'w') as f:
            del final_config['target_config']
            yaml.dump(final_config, f, default_flow_style=False)
    
    print("Final Configuration:", final_config)
    
    #############################
    # Application logic goes here
    #############################
    
