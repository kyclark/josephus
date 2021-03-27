# Josephus Problem

A solution to https://www.codeabbey.com/index/task_view/josephus-problem.

My version accepts and validates N and K from the command line:

```
$ ./solution.py -h
usage: solution.py [-h] [-n int] [-k int]

Josephus Problem

optional arguments:
  -h, --help  show this help message and exit
  -n int      N (default: 10)
  -k int      K (default: 3)
```

Both N and K must be greater than 0:

```
$ ./solution.py -n 0 -k 10
usage: solution.py [-h] [-n int] [-k int]
solution.py: error: -n "0" must be > 0
$ ./solution.py -k 0 -n 10
usage: solution.py [-h] [-n int] [-k int]
solution.py: error: -k "0" must be > 0
```

By default, N = 10 and K = 3:

```
$ ./solution.py
n = 10, k = 3, answer = 4
```

The `josephus.py` program contains all the code to get and validate the arguments.
You must supply the code for the `josephus()` function:

```
def josephus(n: int, k: int) -> int:
    """ Choose the survivor """

    return 0
```

I have provided a `test_josephus()` function that tests with three known values for the correct answer (per the website):

```
def test_josephus() -> None:
    """ Test josephus """

    assert josephus(10, 3) == 4
    assert josephus(64, 17) == 13
    assert josephus(67, 12) == 16
```

You can use `pytest` to run the test.
It should fail because the function currently returns 0:

```
$ pytest -v josephus.py
============================= test session starts ==============================
...
collected 1 item

josephus.py::test_josephus FAILED                                        [100%]

=================================== FAILURES ===================================
________________________________ test_josephus _________________________________

    def test_josephus() -> None:
        """ Test josephus """

>       assert josephus(10, 3) == 4
E       assert 0 == 4
E         +0
E         -4

josephus.py:61: AssertionError
=========================== short test summary info ============================
FAILED josephus.py::test_josephus - assert 0 == 4
============================== 1 failed in 0.08s ===============================
```

The tests pass with `solution.py`:

```
$ pytest -v solution.py
============================= test session starts ==============================
...
collected 1 item

solution.py::test_josephus PASSED                                        [100%]

============================== 1 passed in 0.01s ===============================
```

Once your unit `test_josephus()` function passes, then the integration test should pass, too.
For instance, I'll copy `solution.py` to `josephus.py` to run the tests:

```
$ mv josephus.py foo.py
$ cp solution.py josephus.py
$ pytest -xv josephus.py test.py
============================= test session starts ==============================
...
collected 8 items

josephus.py::test_josephus PASSED                                        [ 12%]
test.py::test_exists PASSED                                              [ 25%]
test.py::test_usage PASSED                                               [ 37%]
test.py::test_bad_n PASSED                                               [ 50%]
test.py::test_bad_k PASSED                                               [ 62%]
test.py::test_defaults PASSED                                            [ 75%]
test.py::test_args1 PASSED                                               [ 87%]
test.py::test_args2 PASSED                                               [100%]

============================== 8 passed in 0.76s ===============================
```

You can also use the `make test` shortcut if you have `make` installed.

If you find this program interesting and the use of tests helpful, I encourage you to check out my first book, [Tiny Python Projects](https://www.amazon.com/Tiny-Python-Projects-Ken-Youens-Clark/dp/1617297518/).

## Author

Ken Youens-Clark <kyclark@gmail.com>
