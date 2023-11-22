# Package import pattern REF: https://docs.python-guide.org/writing/structure/#test-suite
from context import mp3convertackage

from mp3convertpackage import Ledger

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5