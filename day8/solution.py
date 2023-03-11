def init_visible_grid(rows: int, cols: int) -> list[list[bool]]:
  grid = []

  # First row is already visible
  grid.append([True for _col in range(cols)])

  for _row in range(rows - 2):
    new_row = [False for _col in range(cols)]
    new_row[0] = True
    new_row[-1] = True
    grid.append(new_row)

  # Last row is already visible
  grid.append([True for _col in range(cols)])

  return grid

def init_zero_grid(rows: int, cols: int) -> list[list[bool]]:
  grid = []
  for _row in range(rows):
    grid.append([0 for _col in range(cols)])

  return grid

class Forest:
  def __init__(self, grid: list[list[int]]):
    self.grid: list[list[int]] = grid
    self.visible: list[list[bool]] = init_visible_grid(len(grid), len(grid[0]))
    self.scenic: list[list[bool]] = init_zero_grid(len(grid), len(grid[0]))

    self.set_visible_trees()

  def num_visible(self) -> int:
    return sum(list(map(lambda row: sum(row), self.visible)))

  def set_visible_trees(self):
    for row in range(1, len(self.grid) - 1):
      for col in range(1, len(self.grid[0]) - 1):
        self.set_visible(row, col)
  
  def most_scenic_value(self) -> int:
    return max(list(map(lambda row: max(row), self.scenic)))

  def set_visible(self, row: int, col: int):
    # Top
    top = [self.grid[row_idx][col] for row_idx in range(0, row)]
    top.reverse()
    num_less_top = self.num_less(row, col, top)
    if self.all_less(row, col, top):
      self.visible[row][col] = True

    # Left
    left = [self.grid[row][col_idx] for col_idx in range(0, col)]
    left.reverse()
    num_less_left = self.num_less(row, col, left)
    if self.all_less(row, col, left):
      self.visible[row][col] = True

    # Bottom
    bottom = [self.grid[row_idx][col] for row_idx in range(row + 1, len(self.grid))]
    num_less_bottom = self.num_less(row, col, bottom)
    if self.all_less(row, col, bottom):
      self.visible[row][col] = True

    # Right
    right = [self.grid[row][col_idx] for col_idx in range(col + 1, len(self.grid[0]))]
    num_less_right = self.num_less(row, col, right)
    if self.all_less(row, col, right):
      self.visible[row][col] = True

    self.scenic[row][col] = num_less_top*num_less_left*num_less_bottom*num_less_right

  def all_less(self, row: int, col: int, vals: list[int]):
    for val in vals:
      if val >= self.grid[row][col]:
        return False

    return True

  def num_less(self, row: int, col: int, vals: list[int]) -> int:
    are_less = 0
    for val in vals:
      if val < self.grid[row][col]:
        are_less += 1
      else:
        are_less += 1
        break

    return are_less

with open('day8/input.txt') as f:
  lines = f.readlines()
  grid = list(map(lambda line: [int(d) for d in line.strip()], lines))
  forest = Forest(grid)

  print(f'Part 1: {forest.num_visible()}')
  print(f'Part 2: {forest.most_scenic_value()}')
