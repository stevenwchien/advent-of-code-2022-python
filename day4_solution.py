def range_contains(range1, range2):
  [low1,high1] = range1.split('-')
  [low2,high2] = range2.split('-')

  return int(low1.strip()) <= int(low2.strip()) and  int(high1.strip()) >= int(high2.strip())

count = 0
with open('inputs/day4.txt') as f:
  for line in f:
    [range1, range2] = line.split(',')
    if range_contains(range1, range2) or range_contains(range2, range1):
      count += 1

print(f'Solution 1: {count}')



def overlaps(range1, range2):
  [low1,high1] = range1.split('-')
  [low2,high2] = range2.split('-')

  return (int(low1.strip()) <= int(low2.strip()) and  int(high1.strip()) >= int(low2.strip())) or (int(low1.strip()) <= int(high2.strip()) and  int(high1.strip()) >= int(high2.strip()))

count = 0
with open('inputs/day4.txt') as f:
  for line in f:
    [range1, range2] = line.split(',')
    if overlaps(range1, range2) or overlaps(range2, range1):
      count += 1

print(f'Solution 2: {count}')