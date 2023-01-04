import string

import pytest

def unique_char_check(input: str) -> bool:
  """Return true if input string has all unique characters
  
  Conditions:
      1) This function is case sensitive
      2) Cannot use available data structure beyond list/dict/set
  
  Examples:
      1) abcdefghiv -> True
      2) aa -> False
      3) aAbBcC -> True
      4) .(*4)f6F -> True
      5) '' -> False
      6) None -> False

  Approach:
      1) For each character in the input string
          1a) converting character to numerical code
          2a) Check if code already in hash map. If so, return False. If not, store in Hash map.
      2) Return True if no collisions were found when setting up the hash map
      Time complexity: O(n)
      Space complexity: O(n)
  """
  if not input:
    raise ValueError("Input was None or empty string")

  # Alternative implementation if you allow use of a Hash table
  # from collections import Counter
  # if max(Counter(input).values()) > 1:
  #   return False
  
  seen_letters: set = set()
  for c in input:
    numerical_code = ord(c)
    if numerical_code in seen_letters:
      return False
    seen_letters.add(numerical_code)

  return True

@pytest.mark.parametrize("test_input, expected_output",
  [pytest.param(None, None, marks=pytest.mark.xfail(reason='None passed as input')),
   pytest.param('', None, marks=pytest.mark.xfail(reason='Empty string passed as input')),
   pytest.param('abcdefghiv', True),
   pytest.param('aa', False),
   pytest.param('aAbBcC', True),
   pytest.param('.(*4)f6F', True)])
def test_unique_char_check(test_input, expected_output):
  assert unique_char_check(test_input) == expected_output, 'Test case failed.'

if (__name__ == '__main__'):
  pytest.main(["--durations", "0"])