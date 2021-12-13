import wandb
import argparse

"""
deletes all models that do not have a tag attached

by default this means wandb will delete all but the "latest" or "best" models

set dry_run == False to delete...
"""


def clean():
    parser = argparse.ArgumentParser()
    parser.add_argument('userid', type=str)
    parser.add_argument('project_name', type=str)
    parser.add_argument('--delete', action='store_true', default=False)
    args = parser.parse_args()
    api = wandb.Api(overrides={"project": args.project_name, "entity": args.userid})
    project = api.project(args.project_name)

    for artifact_type in project.artifacts_types():
        for artifact_collection in artifact_type.collections():
            for version in api.artifact_versions(artifact_type.type, artifact_collection.name):
                if artifact_type.type == 'model':
                    if len(version.aliases) > 0:
                        # print out the name of the one we are keeping
                        print(f'KEEPING {version.name} with tags {[tag for tag in version.aliases]}')
                    else:
                        print(f'DELETING {version.name}')
                        if args.delete:
                            version.delete()

    if not args.delete:
        print('this was a dry run, add --delete to confirm you want to delete/keep the above files')