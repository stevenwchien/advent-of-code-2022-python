from typing import Tuple

INTERESTING_CYCLES = [20, 60, 100, 140, 180, 220]

def init_crt_grid() -> list[list[str]]:
  grid = []
  for row in range(6):
    grid.append(['0' for col in range(40)])

  return grid
class Computer:
  def __init__(self):
    self.cycle: int = 0
    self.register_x: int = 1
    self.interesting: list[int] = []
    self.sum_interesting: int = 0
    self.grid: list[list[str]] = init_crt_grid()

  def print_grid(self) -> None:
    for row in self.grid:
      print(''.join(row))

  def strength(self) -> int:
    return self.cycle * self.register_x

  def cursor_pos(self) -> Tuple[int, int]:
    return ((self.cycle - 1) // 40, (self.cycle - 1) % 40)

  def noop(self) -> None:
    self.cycle += 1
    self.check_draw()
    self.check_interesting()

  def addx(self, val: int) -> None:
    for i in range(2):
      self.cycle += 1
      self.check_draw()
      self.check_interesting()

    self.register_x += int(val_str)

  def check_draw(self) -> None:
    x, y = self.cursor_pos()
    if abs(self.register_x - y) <= 1:
      self.grid[x][y] = '#'
    else:
      self.grid[x][y] = '.'

  def check_interesting(self) -> None:
    if self.cycle in INTERESTING_CYCLES:
      self.interesting.append(self.strength())
      self.sum_interesting += self.strength()

with open('day10/input.txt') as f:
  computer = Computer()

  for line in f:
    if line.startswith('noop'):
      computer.noop()
    elif line.startswith('addx'):
      instruction, val_str = line.strip().split(' ')
      computer.addx(int(val_str))
    else:
      raise ValueError('Parsing has gone wrong')

  print(f'Part 1: {computer.sum_interesting}')
  print('Part 2:')
  computer.print_grid()
