"""tests for src.compressing.compress_numbers funsction"""

from src.compressing import compress_numbers
import pytest


@pytest.mark.parametrize("normal_in_value,res_value",[
    ([1, 1, 2, 2, 3], [1, 2, 3]),
    ([0, 0, 1, 1, 0], [0, 1, 0])
])
def test_default_scenario(normal_in_value,res_value):
    """ test scenario with expected variables """
    assert res_value == compress_numbers(normal_in_value)


@pytest.mark.parametrize("empty_value",[
    ([])
])
def test_empty_scenario(empty_value):
    """empty-scenario"""
    assert empty_value == compress_numbers(empty_value)

@pytest.mark.parametrize("single_value",[
    ([-123])
])
def test_single_scenario(single_value):
    """single-scenario"""
    assert single_value == compress_numbers(single_value)


"""test out of bordered values"""
@pytest.mark.parametrize("in_value,out_value",[
    (["111","0111", "-124","+124"], [111, -124, 124]),
    ([123.23, 123.42, 99.9, 99.999], [123, 99])
])
def test_default_scenario(in_value,out_value):
    """ test scenario with str, float variables """
    assert out_value == compress_numbers(in_value)


"""test wrong values """
@pytest.mark.parametrize("val_err_input",[
    (["111.0","0111", "11.0.9", "-124"]),
    ([1,"~"]),
    (["11.0","11,0"])
])
def test_exception_val_err(val_err_input):
    """test scenario with val error exception"""
    with pytest.raises(ValueError):
        compress_numbers(val_err_input)
