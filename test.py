""" Tests for josephus.py """

import os
import re
import random
from subprocess import getstatusoutput

PRG = './josephus.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_n():
    """ Dies on bad N """

    bad = random.choice(range(-10, 1))
    ok = random.choice(range(3, 10))
    rv, out = getstatusoutput(f'{PRG} -n {bad} -k {ok}')
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)
    assert re.search(f'-n "{bad}" must be > 0', out)


# --------------------------------------------------
def test_bad_k():
    """ Dies on bad K """

    bad = random.choice(range(-10, 1))
    ok = random.choice(range(3, 10))
    rv, out = getstatusoutput(f'{PRG} -k {bad} -n {ok}')
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)
    assert re.search(f'-k "{bad}" must be > 0', out)


# --------------------------------------------------
def test_defaults():
    """ Runs OK with defaults """

    rv, out = getstatusoutput(f'{PRG}')
    assert out == f'n = 10, k = 3, answer = 4'


# --------------------------------------------------
def test_args1():
    """ Runs OK with arguments """

    rv, out = getstatusoutput(f'{PRG} -n 64 -k 17')
    assert out == f'n = 64, k = 17, answer = 13'


# --------------------------------------------------
def test_args2():
    """ Runs OK with arguments """

    rv, out = getstatusoutput(f'{PRG} -k 12 -n 67')
    assert out == f'n = 67, k = 12, answer = 16'
