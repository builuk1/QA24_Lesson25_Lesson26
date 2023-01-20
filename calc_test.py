from calc import *  # позволяет вызывать методы, как будто они тут есть
# import calc #вызывает методы через обращение к calc > calc.plus
import pytest


def test_plus_pos():
    assert plus(2, 3) == 4  # assert должен получить true, чтобы тест считался пройденным


def test_plus_neg():
    assert plus(2, 2) != 3


def test_minus_pos():
    assert minus(2, 2) == 0


def test_mult_pos():
    assert mult(4, 4) == 16


def test_div_pos():
    assert div(4, 2) == 2
