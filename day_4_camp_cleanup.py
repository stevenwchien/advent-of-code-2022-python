class Range:
  def __init__(self, line):
    [start, end] = line.split('-')

    self.start: int = int(start)
    self.end: int = int(end)

  def contains(self, other):
    return self.start <= other.start and self.end >= other.end

  def overlaps(self, other):
    return self.start <= other.start and self.end >= other.end or self.start <= other.end and self.end >= other.end

contains_count = 0
overlaps_count = 0
with open('inputs/day4.txt') as f:
  for line in f:
    [r1, r2] = line.split(',')
    range1 = Range(r1)
    range2  = Range(r2)
    
    if range1.contains(range2) or range2.contains(range1):
      contains_count += 1

    if range1.overlaps(range2) or range2.overlaps(range1):
      overlaps_count += 1

print(f'Solution 1: {contains_count}')
print(f'Solution 2: {overlaps_count}')
