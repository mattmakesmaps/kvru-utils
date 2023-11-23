# Package import pattern REF: https://docs.python-guide.org/writing/structure/#test-suite
from context import mp3convert

from mp3convert import Ledger

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5