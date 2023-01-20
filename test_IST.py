from IST import *
import pytest


def test_x_pos():
    assert ist(3, 0) == "Display_messageX"


def test_y_pos():
    assert ist(3, 2) == "Display_messageY"


def test_z_pos():
    assert ist(1, 1) == "Display_messageZ"


def test_z_neg():
    assert ist('a', 'b') == "Display_messageZ"
