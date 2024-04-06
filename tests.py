from random import randint
from solver import solve
from math import floor


def round(a, n):
    return floor(a * 10**n) / 10**n


def test_solver():
    for i in range(100):
        b = randint(-100, 100)
        a = randint(1, 100)
        correct = round(-b/a, 5)
        answer = round(solve(a, b), 5)
        assert answer == correct
