from typing import List
import pytest

ALLOWED_CALCULATION_ERROR = .00001

def estimate_water_trapped(mtn_heights: List[float]) -> float:
    """Calculate water trapped in mountains

    Given an array representing elevation values of a two dimensional mountain range, 
    compute how much water can be trapped between mountain peaks after 
    sufficiently heave rainfall.

    :param mtn_heights: Height of mountain range sampled over distance over a line
    :result: Units of water trapped.

    Example: mtn_heights = [3, 5, 7, 5, 6.2, 3, 3.5]
             result = 1.7 (i.e., 1.7 units of water trapped between
                peaks at elevation 7 and 6.2)

    Approach:
        1) Compute at each index the max elevation to the left and right of that point
            in the mountain range (i.e., two arrays)
        2) For each index, if elevantion at this index is less than both neighbors, assume
            the number of water units trapped at this index is min(max left peak,
            max right peak) - this elevation
        3) Return global sum of trapped water at each index
    """
    if not mtn_heights:
        raise ValueError('Null or empty object provided as input')
    
    # No water is considered trapped with a single elevation measurement
    if (len(mtn_heights) == 1):
        return 0
    
    # Calculate highest peak to the left of each index
    l_peak_elevations: List[float] = [max(mtn_heights[0:idx+1]) for idx in range(len(mtn_heights))]
        
    # Calculate highest peak to the right of each index
    r_peak_elevations: List[float] = [max(mtn_heights[-1:idx:-1]) for idx in range(-len(mtn_heights)-1, -1, 1)]
    
    water_trapped: List[float] = [min(l_peak_elevations[idx], r_peak_elevations[idx]) - mtn_heights[idx]
        if (mtn_heights[idx] < l_peak_elevations[idx] and mtn_heights[idx] < r_peak_elevations[idx]) 
        else 0 for idx in range(len(mtn_heights))]
    
    return sum(water_trapped)

@pytest.mark.parametrize("test_input, expected",
    [pytest.param(None, None, marks=pytest.mark.xfail(reason='None passed as input')),
     pytest.param([1], None, marks=pytest.mark.xfail(reason='None passed as input')),
     pytest.param([3, 5, 7, 5, 6.2, 3, 3.5], 1.7),
     pytest.param([3, 9, 7, 5, 6.2, 3, 10], 14.8),
     pytest.param([3, 3, 3, 3, 3, 3], 0),               # Flat elevation
     pytest.param([13, 12, 9, 8, 6.2, 3.9, 3.5], 0)])   # Monotonically decreasing elevation
def test_estimate_water_trapped(test_input: List[float], expected: float):
    assert abs(estimate_water_trapped(test_input) - expected) < ALLOWED_CALCULATION_ERROR

if __name__ == '__main__':
    pytest.main()

