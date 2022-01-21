# Normally write this in file in source code folder

from typing import List
import pytest

def multiply_all_except_self(multipliers: List[float]) -> List[float]:
    """Apply custom multiplication routine to input list
    
    :param multipliers: An array of multipliers
    :return: An array output such that output[i] is equal to the product
                of all the elements of nums except multipliers[i]"""
    if not multipliers:
        raise ValueError("Input was null or empty.")
    
    # Define a total_product variable that contains
    # the product of all inputs sans zeros
    total_product: float = 1
    number_zeros: int = 0
    for m in multipliers:
        if (m == 0):
            number_zeros += 1
            continue
        total_product *= m
    if len(multipliers) == number_zeros:
        total_product = 0
        
    # Calculate the outcome per list index    
    outcome = [0 if (number_zeros > 1) else
                   0 if (m != 0 and number_zeros > 0) else
                   (total_product if (m == 0) else total_product / m)
                   for m in multipliers]
    
    return outcome


# Normally write this in file in test folder

# Set up test fixture (e.g., pytest test fixture) and call unit under test
@pytest.mark.parametrize("test_input, expected",
    [pytest.param(None, None, marks=pytest.mark.xfail(reason='None passed as input')),
     pytest.param(['one', 5, '4'], None, marks=pytest.mark.xfail(reason='Chars in input')),
     pytest.param([0, 4, 8], [32, 0, 0]),      # Obvious corner case
     pytest.param([0, 4, 8, 0], [0, 0, 0, 0]), # Less obvious corner case
     pytest.param([9, -4, 8], [-32, 72, -36])])
def test_multiply_all_except_self_on_garbage(test_input, expected):
    assert multiply_all_except_self(test_input) == expected, 'Test case failed.'

if (__name__ == '__main__'):
    pytest.main()

    
