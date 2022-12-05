def priority(character):
  if character.isupper():
    return ord(character) - 38
  else:
    return ord(character) - 96

def duplicate_item(line):
  items = set()
  for i in range(len(line)//2):
    items.add(line[i])

  for j in range(len(line)//2, len(line)):
    if line[j] in items:
      return line[j]


priorities = 0

with open('inputs/day3.txt') as f:
  for line in f:
    duplicated_item = duplicate_item(line)
    priorities += priority(duplicated_item)

print(priorities)


priorities2  = 0

with open('inputs/day3.txt') as f:
  lines = [line for line in f]

  for i in range(len(lines) // 3):
    items = set()

    items1 = set(lines[3*i]) - set(['\n'])
    items2  = set(lines[3*i+1]) - set(['\n'])
    items3  = set(lines[3*i+2]) - set(['\n'])

    common = items1.intersection(items2).intersection(items3).pop()
    priorities2 += priority(common)

print(priorities2)