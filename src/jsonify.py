import os
import json


def is_dir(path):
    return os.path.isdir(path)


def load_dir(path):
    structure = {}
    basename = None

    if not is_dir(path):
        return structure

    dir_list = os.listdir(path)

    for f in dir_list:
        fpath = os.path.join(path, f)
        basename = os.path.basename(fpath)

        if is_dir(fpath):
            sub_dir_list = os.listdir(fpath)
            if len(sub_dir_list):
                # Recursively load the sub-directories
                sub_dirs = load_dir(fpath)
                structure[basename] = sub_dirs
            else:
                structure[basename] = []
        elif os.path.isfile(fpath):
            structure[basename] = None

    return structure


def main(path):
    structure = load_dir(path)

    json_repr = json.dumps(structure, sort_keys=True, indent=4)
    print(json_repr)
