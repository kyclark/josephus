#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-03-27
Purpose: https://www.codeabbey.com/index/task_view/josephus-problem
"""

import argparse
from itertools import cycle
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    n: int
    k: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Josephus Problem',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n', help='N', metavar='int', type=int, default=10)

    parser.add_argument('-k', help='K', metavar='int', type=int, default=3)

    args = parser.parse_args()

    if args.n < 1:
        parser.error(f'-n "{args.n}" must be > 0')

    if args.k < 1:
        parser.error(f'-k "{args.k}" must be > 0')

    return Args(args.n, args.k)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(f'n = {args.n}, k = {args.k}, answer = {josephus(args.n, args.k)}')


# --------------------------------------------------
def josephus(n: int, k: int) -> int:
    """ Choose the survivor """

    return 0


# --------------------------------------------------
def test_josephus() -> None:
    """ Test josephus """

    assert josephus(10, 3) == 4
    assert josephus(64, 17) == 13
    assert josephus(67, 12) == 16


# --------------------------------------------------
if __name__ == '__main__':
    main()
