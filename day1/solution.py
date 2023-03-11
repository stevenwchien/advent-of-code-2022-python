
elves = [0]
idx = 0
with open('day1/input.txt') as f:
  for line in f:
    if line == '\n':
      idx += 1
      elves.append(0)
    else:
      elves[idx] += int(line)

elves.sort()
print(f"Solution Part 1: {elves[-1]}")
print(f"Solution Part 2: {elves[-1] + elves[-2] + elves[-3]}")

