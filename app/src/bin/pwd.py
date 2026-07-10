from os import getcwd


def current_pathname():
    return getcwd()


def pwd():
    print(f"{current_pathname()}")
