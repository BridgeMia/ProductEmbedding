import os


def find_utils():
    # pathfinder is located in utils
    return os.path.split(os.path.realpath(__file__))[0]


def find_src():
    # pathfinder is located in utils
    # the parent dir is src
    return os.path.split(find_utils())[0]


def find_root():
    # the parent dir of src is the root of the project
    return os.path.join(find_src())[0]


if __name__ == '__main__':
    ret = find_utils()

    print(ret)
