# YAML Configurations and CLI Arguments Merger

This repo contains simple script to merge user-prodived CLI arguments with existing parameters loaded from a YAML file. This is particular useful when one has default application's parameters stored in a YAML file, but wants to update some of those parameters at run-time through CLI.

### Requirements
yaml

### Example of a common use case

A deep learning training script has the default model and data params stored in a yaml file as follows
```
model:
  name: "resnet50"
  num_class: 1000
  learning_rate: 0.001
  optimizer:
    type: "adam"
    momentum: 0.9

dataset:
  path: "/data/images"
  batch_size: 32
```
Run the training script using the default config using
```
python main.py
```
Now, say you want to train the model with the same parameters except that you want to try a smaller learning rate, say ```learning_rate = 0.0005```. Use the following CLI command:
```
python main.py --model.learning_rate 0.0005 --target_config ./configs/config_new_lr.yaml
```

This will generate a new yaml file at ```/configs/config_new_lr.yaml```. The user doesn't need to create a new config file before running a new experiment with some small update to an existing configuration. This can save time and adds more convenience.

The newly create yaml file is as follows.

```
model:
  name: "resnet50"
  num_class: 1000
  learning_rate: 0.0005
  optimizer:
    type: "adam"
    momentum: 0.9

dataset:
  path: "/data/images"
  batch_size: 32
```