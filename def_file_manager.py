import os.path
import os
import shutil
import sys


def choice4():
    """

    :return:
    """
    path = list(sys.path)
    print(sys.path)
    return path


def choice5():

    path = os.listdir(path=".")
    for el in path:
        if os.path.isdir(el):
            print(el)

    return path


def choice6():
    with os.scandir(path='.') as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                print(entry.name)
    return entry.name


def choice7():
    print(sys.platform)
    return sys.platform


def choice8(who_creator):
    print(who_creator)
    return f'{who_creator}'
