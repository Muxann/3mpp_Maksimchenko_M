from my_funcs.utils import *
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [(5, 2, 10),
                                                   (4, 6, 24),
                                                   (-7, 7, -49),
                                                   (3.5, 4, 14)])
def test_multiplication_good(a, b, expected_result):
    assert multiplication(a, b) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [(5, 2, 7),
                                                   (4, 6, 10),
                                                   (-7, 7, 0),
                                                   (3.5, 4, 7.5)])
def test_addition_good(a, b, expected_result):
    assert addition(a, b) == expected_result


@pytest.mark.parametrize("a, b, expected_result", [(5, 2, 3),
                                                   (4, 6, -2),
                                                   (-7, 7, -14),
                                                   (3.5, 4, -0.5)])
def test_subtraction_good(a, b, expected_result):
    assert subtraction(a, b) == expected_result


@pytest.mark.parametrize("expected_exception, divider, divisionable", [(ZeroDivisionError, 0, 10),
                                                                       (TypeError, "2", 20)])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        division(divisionable, divider)
