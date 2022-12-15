class Operation:
  def __init__(self, op: str):
    self.op = op

  def operate(self, item: int) -> int:
    tokens = self.op.split(' ')
    val = 0
    thing_to_do = '+'

    for token in tokens:
      if token.strip() == 'old':
        val = self.update(thing_to_do, val, item)
      elif token.strip().isnumeric():
        val = self.update(thing_to_do, val, int(token))
      else:
        thing_to_do = token
    
    return val

  def update(self, operation, ls, rs) -> int:
    if operation == '+':
      return ls + rs
    elif operation == '*':
      return ls * rs

class Monkey:
  def __init__(self, items_queue: list[int], operation: Operation, divisible_by: int, true_to: int, false_to: int):
    self.items_queue = items_queue
    self.operation: Operation = operation
    self.divisible_by: int = divisible_by
    self.true_to: int = true_to
    self.false_to: int = false_to
    self.inspected: int = 0

class MonkeysInTheMiddle:
  def __init__(self, monkeys: list[Monkey]):
    self.monkeys: list[Monkey] = monkeys

  def round(self):
    for monkey in self.monkeys:
      while(len(monkey.items_queue) > 0):
        item = monkey.items_queue.pop(0)
        new_item = monkey.operation.operate(item)
        new_item = new_item // 3

        if new_item % monkey.divisible_by == 0:
          self.monkeys[monkey.true_to].items_queue.append(new_item)
        else:
          self.monkeys[monkey.false_to].items_queue.append(new_item)

        monkey.inspected += 1

  def inspected_vals(self) -> list[int]:
    return list(map(lambda monkey: monkey.inspected, self.monkeys))

monkeys = []
starting_items = []
operation = ''
divisible_by = 0
throw_to_true = -1
throw_to_false = -1

file = open('inputs/day11.txt')
while file:
    line = file.readline()
    if line == "":
      monkey = Monkey(starting_items, Operation(operation), divisible_by, throw_to_true, throw_to_false)
      monkeys.append(monkey)
      break
    elif line == '\n':
      monkey = Monkey(starting_items, Operation(operation), divisible_by, throw_to_true, throw_to_false)
      monkeys.append(monkey)
    elif line.startswith('Monkey'):
      continue
    elif line.startswith('  Starting items:'):
      starting_items = list(map(lambda val_str: int(val_str), line.split('Starting items: ')[1].split(', ')))
    elif line.startswith('  Operation:'):
      operation = line.split('  Operation: new = ')[1]
    elif line.startswith('  Test: '):
      divisible_by = int(line.split('  Test: divisible by ')[1])
    elif line.startswith('    If true: '):
      throw_to_true = int(line.split('    If true: throw to monkey ')[1])
    elif line.startswith('    If false: '):
      throw_to_false = int(line.split('    If false: throw to monkey ')[1])

file.close()
print(len(monkeys))
monkeys_in_the_middle = MonkeysInTheMiddle(monkeys)
for i in range(20):
  monkeys_in_the_middle.round()

print(f'Part 1 Vals: {monkeys_in_the_middle.inspected_vals()}')
