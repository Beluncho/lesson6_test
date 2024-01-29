import pytest

from def_file_manager import *
from use_function import *


def test_choice4():
    assert choice4() == sys.path


def test_choice5():
    assert choice5() == ['.git',
                         '.gitignore',
                         '.idea',
                         '.pytest_cache',
                         'def_file_manager.py',
                         'def_victory.py',
                         'file_manager.py',
                         'functions.py',
                         'LICENSE',
                         'README.md',
                         'test_filemanager.py',
                         'test_python.py',
                         'use_function.py',
                         'victory.py',
                         'vyctory_new.py',
                         '__pycache__']


def test_choice6():
    assert choice6() == '__pycache__'


def test_choice7():
    assert choice7() == sys.platform


def test_choice8():
    assert choice8('Bel') == 'Bel'
    assert choice8('Alex') == 'Alex'






