line = open('day6/input.txt').readline()

def first_n_unique_characters(line: str, n: int) -> int:
  ptr = n

  while len(set(line[ptr-n:ptr])) != n:
    ptr += 1

  return ptr

print(f'Solution Part 1: {first_n_unique_characters(line, 4)}')
print(f'Solution Part 2: {first_n_unique_characters(line, 14)}')
