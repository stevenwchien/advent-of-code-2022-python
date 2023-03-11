from __future__ import annotations
from typing import Tuple

class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def move_toward(self, other: Point) -> None:
    diff_x = other.x - self.x
    diff_y = other.y - self.y

    if abs(diff_x) <= 1 and abs(diff_y) <= 1:
      return

    if abs(diff_x) > 2 or abs(diff_y) > 2:
      raise ValueError('Rope state is corrupt')

    if abs(diff_x) == 2:
      self.x += diff_x / 2\

      if abs(diff_y) == 1:
        self.y += diff_y

    if abs(diff_y) == 2:
      self.y += diff_y / 2

      if abs(diff_x) == 1:
        self.x += diff_x

  def get_pt(self) -> Tuple[int, int]:
    return (self.x, self.y)

  def move_right(self) -> None:
    self.x = self.x + 1

  def move_left(self) -> None:
    self.x = self.x - 1

  def move_down(self) -> None:
    self.y = self.y - 1

  def move_up(self) -> None:
    self.y = self.y + 1

class Rope:
  def __init__(self, head: Point, length: int):
    self.length: int = length
    self.points: list[Point] = [Point(head.x, head.y) for i in range(length)]

  def move_right(self) -> None:
    self.points[0].move_right()
    self.move_rest_of_rope()

  def move_left(self) -> None:
    self.points[0].move_left()
    self.move_rest_of_rope()

  def move_down(self) -> None:
    self.points[0].move_down()
    self.move_rest_of_rope()

  def move_up(self) -> None:
    self.points[0].move_up()
    self.move_rest_of_rope()

  def move_rest_of_rope(self) -> None:
    for i in range(1, self.length):
      self.points[i].move_toward(self.points[i - 1])

  def head(self) -> Point:
    return self.points[0]

  def tail(self) -> Point:
    return self.points[-1]

class Grid:
  def __init__(self, rope_length: int):
    self.rope: Rope = Rope(Point(0, 0), rope_length)
    self.visited: set = set([(0, 0)])

  def step(self, instruction: str) -> None:
    direction, num_steps = instruction.split(' ')

    for i in range(int(num_steps)):
      if direction == 'R':
        self.rope.move_right()
      elif direction == 'L':
        self.rope.move_left()
      elif direction == 'D':
        self.rope.move_down()
      elif direction == 'U':
        self.rope.move_up()
      else:
        raise ValueError('Direction must be one of these values')

      # Record tail position
      self.visited.add(self.rope.tail().get_pt())

  def unique_tail_visits(self) -> int:
    return len(self.visited)

with open('day9/input.txt') as f:
  grid1 = Grid(2)
  grid2 = Grid(10)

  for line in f:
    grid1.step(line.strip())
    grid2.step(line.strip())

  print(f'Part 1: {grid1.unique_tail_visits()}')
  print(f'Part 2: {grid2.unique_tail_visits()}')
