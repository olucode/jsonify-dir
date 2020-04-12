import os
import json
import argparse


def is_dir(path):
    return os.path.isdir(path)


def print_json(obj):
    json_repr = json.dumps(obj, sort_keys=True, indent=4)
    print(json_repr)


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


def get_parser():
    parser = argparse.ArgumentParser(
        prog='jsonify-dir', description='JSON representation of file path')

    parser.add_argument('path', metavar='PATH', type=str,
                        help='the path to list')

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    path = args.path
    structure = load_dir(path)

    print_json(structure)


if __name__ == '__main__':
    main()
