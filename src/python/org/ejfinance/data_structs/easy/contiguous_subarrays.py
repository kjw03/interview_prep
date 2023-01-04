import re
import math
from typing import List

import pandas as pd
import numpy as np
import pytest

def _count_subarrays(arr: List[int]) -> np.ndarray:
  # Count number of forward contiguous subarrays
  count_subarrays = np.zeros(len(arr), dtype=np.int32)
  for idx, val in enumerate(arr):
    for j in range(idx, len(arr)):
      print(f"subarray under test for start value {val}: {arr[idx:j]}")
      if all([i <= val for i in arr[idx:j+1]]):
        count_subarrays[idx] += 1
      else:
        break

  return count_subarrays

def count_contiguous_subarrays(arr: List[int]) -> List[int]:
  """Determine number of contiguous subarrays

  Conditions for subarrays
  1) Value at index i must be max element in
      contiguous subarray
  2) Contiguous subarrays start from or end on index i.
      This means the subarray must start at index (i+1)%len(arr)
      or end on index i (non-inclusive)

  Example:
  1) Input: [3, 4, 1, 6, 2]
  1) Output: [1, 3, 1, 6, 0]

  Index 0 -> [3]
  Index 1 -> [4], [3, 4], [4, 1]
  Index 2 -> [1]
  Index 3 -> [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]  
  Index 4 -> [2]

  2) Input: [2, 2, 1, 2, 2]
  2) Output: [5, 5, 1, 5, 5]

  Index 0 -> [2], [2, 2], [2, 2, 1], [2, 2, 1, 2], [2, 2, 1, 2, 2]
  Index 1 -> [2], [2, 2], [2, 1], [2, 1, 2], [2, 1, 2, 2]
  Index 2 -> [1]
  Index 3 -> [2], [2, 2], [1, 2], [2, 1, 2], [2, 2, 1, 2]
  Index 4 -> [2], [2, 2], [1, 2, 2], [2, 1, 2, 2], [2, 2, 1, 2, 2]

  :param arr: An array of N integers
  :return: Integer number of valid subarrays in input"""

  count_forward_subarrays = _count_subarrays(arr)
  print(f"count_forward_subarrays = {count_forward_subarrays}")
  count_backward_subarrays = list(reversed(_count_subarrays(list(reversed(arr)))))

  total_count = (count_forward_subarrays + count_backward_subarrays - 1)
  return total_count.tolist() 

@pytest.mark.parametrize("test_input, expected_output",
  [pytest.param([3, 4, 1, 6, 2], [1, 3, 1, 5, 1]),
   pytest.param([2, 4, 7, 1, 5, 3], [1, 2, 6, 1, 3, 1]),
   pytest.param([2, 2, 1, 2, 2], [5, 5, 1, 5, 5])])
def test_count_contiguous_subarrays(test_input: List[int],
                              expected_output: List[int]):
  assert count_contiguous_subarrays(test_input) == expected_output

if (__name__ == '__main__'):
  pytest.main(["--durations", "0"])