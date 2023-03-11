from __future__ import annotations
from collections import deque

IN_ORDER = -1

class SignalList:
  def __init__(self, starting_list: list[SignalList | int]):
    self.internal_list: list[SignalList | int] = starting_list

  def elem(self, idx: int) -> SignalList | int:
    return self.internal_list[idx]
  
  def __str__(self):
    out_str_vals = []

    for elem in self.internal_list:
      out_str_vals.append(str(elem))

    out_str = ','.join(out_str_vals)

    return f'[{out_str}]'
  
  @classmethod
  # If [: push [
  # If number (token): push token - until the next comma
  # If comma: skip
  # If ]: pop all values until the previous [, then make a new Signal List with the values popped
  def parse(cls, input) -> SignalList:
    idx = 0
    stack = deque()
    stack.append(input[idx])
    idx += 1

    while idx < len(input):
      if input[idx] == '[':
        stack.append(input[idx])
        idx += 1
      elif input[idx:idx+2].isnumeric(): # Handle double digit int
        stack.append(int(input[idx:idx+2]))
        idx += 2
      elif input[idx].isnumeric(): # Single digit int
        stack.append(int(input[idx]))
        idx += 1
      elif input[idx] == ',':
        idx += 1
        continue
      elif input[idx] == ']':
        next_val = stack.pop()
        new_list = deque()
        while next_val != '[':
          new_list.appendleft(next_val)
          next_val = stack.pop()

        stack.append(cls(list(new_list)))
        idx += 1
      else:
        raise ValueError

    return stack.pop()

# -1 if in order. 0 if same. 1 if not in order
def compare_int(int1: int, int2: int) -> int:
  if int1 < int2:
    return IN_ORDER
  elif int1 > int2:
    return 1
  else:
    return 0
  
# -1 if in order. 0 if same. 1 if not in order
def compare_list(sl1: SignalList, sl2: SignalList) -> int:
  len_sl1 = len(sl1.internal_list)
  len_sl2 = len(sl2.internal_list)

  # Iterate through each element and compare them. Return the greater one
  for idx in range(min(len_sl1, len_sl2)):
    cmp = compare(sl1.elem(idx), sl2.elem(idx))
    if cmp == IN_ORDER or cmp == 1:
      return cmp
    
  return compare_int(len_sl1, len_sl2)

# -1 if in order. 0 if same. 1 if not in order
def compare(sl1: SignalList | int, sl2: SignalList | int) -> int:
  if isinstance(sl1, int) and isinstance(sl2, int):
    return compare_int(sl1, sl2)
  elif isinstance(sl1, int):
    return compare(SignalList([sl1]), sl2)
  elif isinstance(sl2, int):
    return compare(sl1, SignalList([sl2]))
  else:
    return compare_list(sl1, sl2)

# Part 1
pairs = []
with open('day13/input.txt') as file:
  first = True
  for line in file:
    if line == '\n':
      continue

    sl = SignalList.parse(line.strip())

    if first:
      pairs.append([sl])
    else:
      pairs[-1].append(sl)

    first = not first

sum_idx = 0
for idx, pair in enumerate(pairs):
  cmp = compare(pair[0], pair[1])
  if cmp == IN_ORDER:
    sum_idx += idx + 1

print(sum_idx)

# Part 2
decoder2 = SignalList.parse('[[2]]')
decoder6 = SignalList.parse('[[6]]')

signal_lists = [decoder2,decoder6]
with open('day13/input.txt') as file:
  for line in file:
    if line == '\n':
      continue

    sl = SignalList.parse(line.strip())

    signal_lists.append(sl)

decoder2_pos = 1
decoder6_pos = 1
for signal_list in signal_lists:
  if compare(signal_list, decoder2) == IN_ORDER:
    decoder2_pos += 1

  if compare(signal_list, decoder6) == IN_ORDER:
    decoder6_pos += 1

print(decoder2_pos)
print(decoder6_pos)
print(decoder2_pos*decoder6_pos)
