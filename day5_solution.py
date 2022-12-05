import re

class Instruction:
  def __init__(self, line):
    pattern = re.compile(r'move (?P<num_boxes>\d+) from (?P<start>\d+) to (?P<end>\d+)')
    match = pattern.search(line)

    self.num_boxes = match['num_boxes']
    self.start = match['start']
    self.end = match['end']

class Stack:
  def __init__(self, crates):
    self.crates = crates

  def push(self, crate):
    self.crates.append(crate)

  def pop(self):
    return self.crates.pop()

  def peek(self):
    return self.crates[-1]

  def empty(self):
    len(self.crates) == 0

class Stacks:
  def __init__(self, lines):
    self.num_stacks = 0
    self.stacks: list[Stack] = [
      Stack(['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G']),
      Stack(['S', 'W', 'C']),
      Stack(['R', 'Z', 'T', 'M']),
      Stack(['D', 'T', 'C', 'H', 'S', 'P', 'V']),
      Stack(['G', 'P', 'T', 'L', 'D', 'Z']),
      Stack(['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D']),
      Stack(['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R']),
      Stack(['L', 'H', 'R', 'B', 'T', 'V', 'M']),
      Stack(['Q', 'P', 'D', 'S', 'V']),
    ]

  def process_instruction(self, instruction: Instruction):
    num = int(instruction.num_boxes)
    start_idx = int(instruction.start)
    end_idx = int(instruction.end)

    for _i in range(num):
      self.stacks[end_idx-1].push(self.stacks[start_idx-1].pop())

  def top_crates(self):
    return ''.join(list(map(lambda stack : stack.peek(), self.stacks)))

def process_instruction(instruction: Instruction):
  print(f'move {instruction.num_boxes} boxes from {instruction.start} to {instruction.end}')

with open('inputs/day5.txt') as f:
  stack_lines = []
  for line in f:
    if line == '\n':
      break

    stack_lines.append(line)

  stacks = Stacks(stack_lines)

  for line in f:
    instruction = Instruction(line)
    stacks.process_instruction(instruction)

  print(stacks.top_crates())