import math
from optparse import Values
from typing import Tuple, Iterable

import pytest

class MinHeap:
  """Traditional MinHeap data structure implementation
  
  Conditions: 
    1) Support tuples
    2) Size of heap no known beforehand

  Example:
    Inserts (in order): 10, 8, 4, 8, 6, 2
    extract_min call return values: 2, 4, 6, 8, 8, 10

  Approach:
    - Initialize List (backed by variable length array
      in CPython reference implementation of Python programming
      language, the software while compiles Python source into
      bytecode and then interprets it)
    - Insert - Insert new value at end of array. Bubble it up until
      it is the root or the parent is a lower value 
    - extract_mind - If len(self.values) > 1, replace self.values[0]
      with self.values[-1], then call self.values.pop(). If the new root
      is larger than either child, swap it with the smaller child node. Repeat
      for that child if a swap is done until your are at the bottom level of the
      tree or the current value is smaller than both children.
  """
  def __init__(self, init_values: Iterable[int]):
    self.values = list()
    for i in init_values:
      self.insert(i)

  def _get_parent_idx(self, child_idx: int):
    if child_idx == 0:
      raise ValueError("The node has no parent. It is the root of the tree.")
    return (child_idx - 2)//2 if (child_idx % 2 == 0) else (child_idx - 1)//2
  
  def _get_children_idxs(self, parent_idx: int) -> Tuple[int, int]:
    left_child_idx: int = 2 * parent_idx + 1
    right_child_idx: int = 2 * parent_idx + 2
    return (left_child_idx, right_child_idx)

  def insert(self, value):
    self.values.append(value)

    # Bubble up the node
    if len(self.values) > 1:  
      curr_idx = len(self.values) - 1
      parent_idx = self._get_parent_idx(curr_idx)

      while self.values[curr_idx] < self.values[parent_idx]:
        self.values[parent_idx], self.values[curr_idx] = (self.values[curr_idx],
                                                          self.values[parent_idx])

        # Exit if we just replaced the root node
        if parent_idx == 0:
          break

        # Prepare for check if we need to bubble up again
        curr_idx = parent_idx
        parent_idx = self._get_parent_idx(curr_idx)
    
    return

  def extract_min(self):
    # Return Exception if there is no value to pop
    if len(self.values) == 0:
      raise Exception("No value in heap to pop.")

    # If the tree is a single node, pop the value and return it
    if len(self.values) == 1:
      return self.values.pop() 
      
    # Extract the min value that will be returned
    min_value = self.values[0]

    # Update the tree by replacing the root with the largest node and bubbling it down
    self.values[0] = self.values[-1]
    self.values.pop()

    # Bubble the new root down until the tree is correct
    curr_idx = 0
    while (True):
      (left_child_idx, right_child_idx) = self._get_children_idxs(curr_idx)
      replacement_idx = None
      
      # Is the left child is a candidate to bubble up and replace the current node?
      if (left_child_idx < len(self.values) and
          self.values[left_child_idx] < self.values[curr_idx]):
        replacement_idx = left_child_idx

      # Is the right child is a candidate to bubble up and replace the current node?
      if (right_child_idx < len(self.values) and
          self.values[right_child_idx] < self.values[curr_idx]):
        replacement_idx = (right_child_idx if (replacement_idx is None) else
                           right_child_idx if (self.values[right_child_idx] < self.values[replacement_idx])
                           else replacement_idx)

      # Swap the current node and its selected child
      if replacement_idx != None:
        self.values[replacement_idx], self.values[curr_idx] = (self.values[curr_idx], 
                                                               self.values[replacement_idx])
        curr_idx = replacement_idx
      else:
        break

    return min_value

@pytest.mark.parametrize("insertion_values, expected_min_values",
  [pytest.param([1, 4, 8, 23, 6, 4, 9, 9, 9], [1, 4, 4, 6]),
   pytest.param([], [1, 4, 4, 6], marks=pytest.mark.xfail(reason="Cannot extract a min value from an empty min heap")),
   pytest.param([9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9]),
   pytest.param([9, -10, 5, 100, -2, 4, 9, 9], [-10, -2, 4, 5]),
   pytest.param([9, -10, 5, 100, -2, 4, 9, 9, 100, -2, 4, 9, 9, 101, -3, 4, 9, 9], [-10, -3, -2, -2])])
def test_min_heap(insertion_values, expected_min_values):
  minheap: MinHeap = MinHeap(insertion_values)
  for i in expected_min_values:
    assert minheap.extract_min() == i

if (__name__ == '__main__'):
  pytest.main(["--durations", "0"])

