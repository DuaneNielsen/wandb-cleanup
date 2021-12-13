## wandb-cleanup

Deletes models without tags

To install in your python environment

```bash
git clone https://github.com/duanenielsen/wandb-cleanup
pip install -e .
```

To use, tag models you want to keep in wandb 
(by default wandb tags the latest model uploaded) then run

```bash
wandb-cleanup <userid> <project_name> 
```

this will list the model artifacts, and indicate which are to be deleted vs kept

To actually delete execute

```bash
wandb-cleanup <userid> <project_name> --delete
```

example usage

```bash
> wandb-cleanup duannielsen oardm_cifar

KEEPING model-2xaf8kp7:v12 with tags ['latest', 'best']
DELETING model-2xaf8kp7:v11
DELETING model-2xaf8kp7:v10
DELETING model-2xaf8kp7:v9
this was a dry run, add --delete to confirm you want to delete/keep the above files

> wandb-cleanup duannielsen oardm_cifar --delete

KEEPING model-2xaf8kp7:v12 with tags ['latest', 'best']
DELETING model-2xaf8kp7:v11
DELETING model-2xaf8kp7:v10
DELETING model-2xaf8kp7:v9
```

