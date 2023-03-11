from collections import deque

class Hill:
  def __init__(self, grid: list[list[str]]):
    self.grid = self._process_grid(grid)
    self.start = self._find(grid, 'S')
    self.end = self._find(grid, 'E')
    self.num_rows = len(grid)
    self.num_cols = len(grid[0])

  def min_path_start_to_end(self):
    self.visited = [[False for _ in range(self.num_cols)] for _ in range(self.num_rows)]
    queue = deque()
    queue.append((self.start[0], self.start[1], 0))

    while len(queue) > 0:
      (row, col, curr_len) = queue.pop()

      if row == self.end[0] and col == self.end[1]:
        return curr_len

      for (next_row, next_col) in self._adjacent_positions_up(row, col):
        queue.appendleft((next_row, next_col, curr_len+1))
        self.visited[next_row][next_col] = True

    return -1
  
  def min_path_end_to_a(self):
    self.visited = [[False for _ in range(self.num_cols)] for _ in range(self.num_rows)]
    queue = deque()
    queue.append((self.end[0], self.end[1], 0))

    while len(queue) > 0:
      (row, col, curr_len) = queue.pop()

      if self.grid[row][col] == ord('a'):
        return curr_len

      for (next_row, next_col) in self._adjacent_positions_down(row, col):
        queue.appendleft((next_row, next_col, curr_len+1))
        self.visited[next_row][next_col] = True

    return -1

  def _adjacent_positions_up(self, row: int, col: int) -> list[tuple]:
    adj = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]

    actual_candidates = []

    for (r, c) in adj:
      # Check if out of bounds
      if r == self.num_rows or r < 0 or c == self.num_cols or c < 0:
        continue
      
      # Check if visited/added to the queue already
      if self.visited[r][c]:
        continue

      # Check if the height is low enough
      if self.grid[r][c] > self.grid[row][col] + 1:
        continue

      actual_candidates.append((r, c))

    return actual_candidates

  def _adjacent_positions_down(self, row: int, col: int) -> list[tuple]:
    adj = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]

    actual_candidates = []

    for (r, c) in adj:
      # Check if out of bounds
      if r == self.num_rows or r < 0 or c == self.num_cols or c < 0:
        continue

      # Check if visited/added to the queue already
      if self.visited[r][c]:
        continue

      # Check if the height is too low
      if self.grid[r][c] < self.grid[row][col] - 1:
        continue

      actual_candidates.append((r, c))

    return actual_candidates

  def _find(self, grid: list[list[str]], val: str):
    for r in range(len(grid)):
      for c in range(len(grid[0])):
        if grid[r][c] == val:
          return (r, c)

  def _process_grid(self, grid: list[list[str]]) -> list[list[int]]:
    def process_grid_value(val: str):
      if val == 'S':
        return ord('a')
      elif val == 'E':
        return ord('z')
      else:
        return ord(val)

    return list(map(lambda ls: list(map(lambda val: process_grid_value(val), ls)), grid))


if __name__ == '__main__':
  with open('day12/input.txt') as f:
    lines = f.readlines()
    grid = list(map(lambda line: [c for c in line.strip()], lines))

    # Part 1
    hill = Hill(grid)
    print(hill.min_path_start_to_end())
    print(hill.min_path_end_to_a())