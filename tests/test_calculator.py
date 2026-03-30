import math
import pytest

from calculator.calculator import (
    squareNums,
    triNums,
    lazyCaterer,
    magicSquares,
    hypotenuse,
    rectangleArea,
    circleCircumference,
)


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 4),
        (5, 25),
        (10, 100),
    ],
)
def test_squareNums(n, expected):
    assert squareNums(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1.0),
        (4, 10.0),
        (10, 55.0),
    ],
)
def test_triNums(n, expected):
    assert triNums(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2.0),
        (2, 4.0),
        (5, 16.0),
    ],
)
def test_lazyCaterer(n, expected):
    assert lazyCaterer(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1.0),
        (3, 15.0),
        (5, 65.0),
    ],
)
def test_magicSquares(n, expected):
    assert magicSquares(n) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 5.0),
        (5, 12, 13.0),
        (8, 15, 17.0),
    ],
)
def test_hypotenuse(a, b, expected):
    assert hypotenuse(a, b) == expected


@pytest.mark.parametrize(
    "length, width, expected",
    [
        (2, 3, 6),
        (5, 4, 20),
        (10, 7, 70),
    ],
)
def test_rectangleArea(length, width, expected):
    assert rectangleArea(length, width) == expected


@pytest.mark.parametrize(
    "radius, expected",
    [
        (1, 2 * math.pi),
        (2, 4 * math.pi),
        (3, 6 * math.pi),
    ],
)
def test_circleCircumference(radius, expected):
    assert math.isclose(circleCircumference(radius), expected, rel_tol=1e-9)
