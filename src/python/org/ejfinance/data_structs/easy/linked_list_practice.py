
# from dataclasses import dataclass
# from collections.abc import Iterable
from typing import Iterable

import pytest

# Create classes required to construct a linked list data structure
# If able, we could just use the list() built-in in Python 3, or deque
# This implementation could be improved by annotating it as a dataclass
class Node:
  def __init__(self, data: int):
    self.data = data
    self.next: Node = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def append(self, nodes: Iterable[Node]):
    for idx, node in enumerate(nodes):
      if idx == 0:
        n: Node = self.head
        while (n is not None and n.next != None):
          n = n.next

      if n == None:
        self.head = node
      else:
        n.next = node
      n = node
      self.size += 1

def return_kth_to_end_node_data(llist: LinkedList, k: int) -> int:
  """Return the data stored in the kth to last linked list node

  :param llist: Linked list instance
  :param k: Number of nodes from end of linked list to return value
  :return: Value in node k from end of linked list (0 means return value at last node)

  Problem statement: Return the data stored in the kth to last node
    in a linked list data structure. 

  Conditions/Assumptions: 
    1) Using the LinkedList class as defined above
  
  Examples:
    1) Append elements in [1, 2, 3, 4, 5] -> return 3 if k=2
    2) Append elements in [1, 2] -> return None if k=2

  Approach: Decide on manually tracking kth to current value... max heap on index, (two runners), deque
    1) Traverse k nodes into the linked list with one reference
    2) Move each runner forward one node until the ahead runner hits the end of the list
    3) Retrieve the value at the lagging runner
  """
  print(f"llist size = {llist.size}")

  if not llist:
    raise ValueError("Linked list object reference is None")

  # Return None if the linked list does not contain at least k+1 Nodes
  if (llist.size < k+1):
    return None

  # Set up two runners
  run_ahead = llist.head
  run_behind = llist.head

  # Traverse k items with the runner in the lead
  for i in range(k):
    run_ahead = run_ahead.next

  while (run_ahead.next != None):
    run_ahead = run_ahead.next
    run_behind = run_behind.next
  
  return run_behind.data

llist = LinkedList()
llist.append([Node(val) for val in range(20)])

@pytest.mark.parametrize("test_input, k, expected",
  [pytest.param(None, None, None, marks=pytest.mark.xfail(reason='None passed as input')),
   pytest.param(llist, 3, 16)])
def test_multiply_all_except_self_on_garbage(test_input, k, expected):
  assert return_kth_to_end_node_data(test_input, k) == expected, 'Test case failed.'

if (__name__ == '__main__'):
  pytest.main(["--durations", "0"])

