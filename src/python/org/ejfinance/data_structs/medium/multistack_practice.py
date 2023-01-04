from typing import List

import pytest
import numpy as np

"""
Problem statement: Implement three stacks using a single array implementation

Assumptions:
  1) Goal is to use a one dimensional array rather than utilize numpy's n-dimensional array class
  2) Scope is limited to numeric values (float by default)
  3) Each array is of a fixed size, known as the time of instantiation

Examples:
  1) 3 stack array where each array is size=5, with the following values pushed for each stack
    Stack 1: push([1, 2, 3, 4, 5]) 
    Stack 2: push([1, 2]) -> pop([1,2]) 
    Stack 3: push([10]) -> peek()

Approach:
  1) Write Multistack class backed by a single dimensional array
    1a) Partition the single array where each stack will live in one partition

Runtime:
  Push runtime complexity: O(1)
  Pop runtime complexity: O(1)
  Peek runtime complexity: O(1)
"""
class MultiStack:
  def __init__(self, number_stacks, per_stack_size):
    self._number_stacks = number_stacks
    self._per_stack_size = per_stack_size
    self._values: np.ndarray = np.empty(per_stack_size * number_stacks, dtype=np.float64)
    self._sizes: List[int] = [0] * number_stacks
    self.stack_start_idxs: List[int] = [int(i * per_stack_size) for i in range(number_stacks)]
    self.stack_end_idxs: List[int] = [int(i * per_stack_size) + per_stack_size for i in range(number_stacks)]

  def push(self, stack_number: int, value: float):
    if (self.is_stack_full(stack_number)):
      return Exception(f"Stack {stack_number} is full.")

    (self._values[self.stack_start_idxs[stack_number] +
                  self._sizes[stack_number]]) = value
    self._sizes[stack_number] += 1

  def peek(self, stack_number: int):
    if (self.is_stack_empty(stack_number)):
      return Exception(f"Stack {stack_number} is empty.")
    
    return_val = (self._values[self.stack_start_idxs[stack_number] +
                               self._sizes[stack_number] - 1])
    return return_val

  def pop(self, stack_number: int):
    return_val = self.peek(stack_number)
    self._sizes[stack_number] -= 1
    return return_val

  def is_stack_empty(self, stack_number):
    return self._sizes[stack_number] == 0

  def is_stack_full(self, stack_number: int) -> bool:
    return self._sizes[stack_number] == self._per_stack_size

class TestMultiStack:

  # A superior testing approach would be to initialize a MultiStack object per test, and test a particular sequence
  # of actions in each test. The test below is too complicated.
  # Examples:
  #   1) test_push_peek(), starting with an empty MultiStack
  #   2) test_pop_peek(), starting with a populated MultiStack
  #   3) test_push_pop(), starting with an empty MultiStack
  @pytest.mark.parametrize("num_stacks, per_stack_size, pushes, pops, expected_pops, peeks, expected_peeks",
    [pytest.param(3,
                  10,
                  [[1, 2, 3, 4, 5], [1,2], [10]],
                  [0, 2, 0],
                  [2, 1],
                  [1, 0, 1],
                  [5, 10])])
  def test_example1(self, num_stacks, per_stack_size, pushes, pops, expected_pops, peeks, expected_peeks):
    # Construct multistack
    ms = MultiStack(num_stacks, per_stack_size)
    for i in range(num_stacks):
      for val in pushes[i]:
        ms.push(i, val)

    # Pop from multistack
    assert_idx = 0
    for stack_num in range(len(pops)):
      for j in range(pops[stack_num]):
        assert ms.pop(stack_num) == expected_pops[assert_idx]
        assert_idx += 1
    
    # Peek from multistack
    assert_idx = 0
    for stack_num in range(len(peeks)):
      for j in range(peeks[stack_num]):
        assert ms.peek(stack_num) == expected_peeks[assert_idx]
        assert_idx += 1

if (__name__ == '__main__'):
  pytest.main(["--durations", "0"])