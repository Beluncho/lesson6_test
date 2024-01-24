import math
from functions import my_filter, my_map, my_sorted, my_square_circle, my_sqrt, exponentiation, pythagoras


# filter
def test_filter():
    assert my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5]  # True
    assert my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2]  # True
    assert my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5]  # True
    assert my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b']  # True


# map

def test_map():
    assert my_map(int, ['1', '2', '3', '4', '5']) == [1, 2, 3, 4, 5]


# sorted

def test_sorted():
    assert my_sorted([1, 3, 4, 2]) == [1, 2, 3, 4]


# pi
def test_pi():
    assert my_square_circle(1) == math.pi


# sqrt
def test_sqrt():
    assert my_sqrt(15) == math.sqrt(15**2)


# pow
def test_pow():
    assert exponentiation(15, 148) == 15 ** 148


# hypot
def test_hypot():
    assert pythagoras(15, 25) == (15*15 + 25*25) ** 1/2
