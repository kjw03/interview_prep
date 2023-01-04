from typing import Iterable

import pytest

class _TrieNode:
  def __init__(self, value, is_word_end: bool) -> None:
    self.value = value
    self.is_word_end: bool = is_word_end
    self.children = []

  def add_child(self, child) -> None:
    self.children.append(child)

  def __eq__(self, other):
    if isinstance(other, _TrieNode):
      return self.value == other.value
    elif isinstance(other, type(self.value)):
      return self.value == other
    return False

class Trie:
  def __init__(self) -> None:
    self.root = _TrieNode(None, False)

  def lookup(self, iter: Iterable):
    cur_node = self.root
    found: bool = False
    try:
      for idx, val in enumerate(iter):
        child_idx = cur_node.children.index(val)
        cur_node = cur_node.children[child_idx]
      found = True if cur_node.is_word_end else False
    except ValueError:
      print("Pattern not found.")

    return found

  def insert(self, iter: Iterable):
    parent_node = self.root
    for idx, val in enumerate(iter):
      is_word_end = False if (idx < len(iter) - 1) else True
      if val in parent_node.children:
        child_idx = parent_node.children.index(val)
        node: _TrieNode = parent_node.children[child_idx]
        node.is_word_end = True if (idx == len(iter) - 1) else node.is_word_end
      else:
        node = _TrieNode(val, is_word_end)
        parent_node.add_child(node)
      parent_node = node

@pytest.mark.parametrize("test_insert, test_lookup, expected_output",
  [pytest.param('hello world', 'hello world', True),
   pytest.param('hello world', 'hello world!', False),
   pytest.param('hello world', 'gello world', False)])
def test_insert_and_lookup(test_insert, test_lookup, expected_output):
  t1 = Trie()
  t1.insert(test_insert)
  assert t1.lookup(test_lookup) == expected_output

if (__name__ == '__main__'):
  pytest.main()
  