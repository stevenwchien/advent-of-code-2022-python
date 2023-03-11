import re

class Instruction:
  def __init__(self, line):
    pattern = re.compile(r'move (?P<num_boxes>\d+) from (?P<start>\d+) to (?P<end>\d+)')
    match = pattern.search(line)

    self.num_boxes: int = int(match['num_boxes'])
    self.start: int =int(match['start'])
    self.end: int = int(match['end'])

class Stack:
  def __init__(self, crates):
    self.crates = crates

  def push(self, crate):
    self.crates.append(crate)

  def pop(self):
    return self.crates.pop()

  def move(self, num):
    moved_crates = self.crates[(-1 - num + 1):]
    self.crates = self.crates[0:len(self.crates) - num]

    return moved_crates

  def place(self, crates):
    self.crates = self.crates + crates

  def peek(self):
    return self.crates[-1]

  def empty(self):
    return len(self.crates) == 0

  def num_entries(self):
    return len(self.crates)

class Stacks:
  def __init__(self, lines):
    self.num_stacks = 9
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

  def process_instruction2(self, instruction: Instruction):
    start_stack = self.stacks[instruction.start-1]
    end_stack = self.stacks[instruction.end-1]
    crates_to_move = start_stack.move(instruction.num_boxes)

    end_stack.place(crates_to_move)

  def process_instruction(self, instruction: Instruction):
    start_stack = self.stacks[instruction.start-1]
    end_stack = self.stacks[instruction.end-1]

    for _i in range(instruction.num_boxes):
      end_stack.push(start_stack.pop())

  def top_crates(self) -> str:
    return ''.join(list(map(lambda stack : stack.peek(), self.stacks)))

  def print(self) -> None:
    nums = ' '.join([f' {j + 1} ' for j in range(self.num_stacks)])
    final = [nums]
    max_stack_length = max(list(map(lambda stack : stack.num_entries(), self.stacks)))

    for crate_idx in range(max_stack_length):
      line_item = ''
      for stack_idx in range(self.num_stacks):
        if self.stacks[stack_idx].num_entries() > crate_idx:
          line_item += f'[{self.stacks[stack_idx].crates[crate_idx]}]'
        else:
          line_item += f'   '

        line_item += ' '

      final.append(line_item)

    while len(final) > 0:
      print(final.pop())

with open('inputs/day5.txt') as f:
  stack_lines = []
  for line in f:
    if line == '\n':
      break

    stack_lines.append(line)

  stacks = Stacks(stack_lines)
  stacks2 = Stacks(stack_lines)

  for line in f:
    instruction = Instruction(line)
    stacks.process_instruction(instruction)
    stacks2.process_instruction2(instruction)

  stacks.print()
  print(f'Solution Part 1: {stacks.top_crates()}')

  stacks2.print()
  print(f'Solution Part 2: {stacks2.top_crates()}')
