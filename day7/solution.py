class File:
  def __init__(self, name, size, parent):
    self.name: str = name
    self.size: int = size
    self.parent: Directory = parent

  def is_dir(self) -> bool:
    return False

  def get_size(self) -> int:
    return self.size

  def get_small_size(self) -> int:
    return self.size

class Directory:
  def __init__(self, name, parent):
    self.name = name
    self.parent: Directory | None = parent
    self.children: dict[str, Directory | File] = {}

  def smallest_directory_larger_than(self, size):
    min_above = self.get_size()
    min_above_dirname = ''
    for name, value in self.children.items():
      if value.is_dir():
        dir_min_size = value.smallest_directory_larger_than(size)
        if dir_min_size >= size and dir_min_size < min_above:
          min_above = dir_min_size
          min_above_dirname = name

    return min_above

  def is_dir(self) -> bool:
    return True

  def get_size(self) -> int:
    return sum(list(map(lambda child : child.get_size(), iter(self.children.values()))))

  def get_small_size(self) -> int:
    total = 0
    my_size = self.get_size()
    if self.get_size() < 100000:
      total += my_size

    for name, value in self.children.items():
      if value.is_dir():
        total += value.get_small_size()

    return total

class FileSystem:
  def __init__(self):
    self.root: Directory = Directory('/', None)
    self.path: str = '/'
    self.wd: Directory = self.root

  def smallest_directory_larger_than(self, size):
    return self.root.smallest_directory_larger_than(size)
    return 1

  def get_small_size(self):
    return self.root.get_small_size()

  def get_size(self):
    return self.root.get_size()

  def cd(self, directory):
    if directory == '..':
      self.wd = self.wd.parent
    else:
      self.wd = self.wd.children[directory]

  def ls(self, contents: list[str]):
    for content in contents:
      if content.startswith('dir'):
        dirname = content.split(' ')[1]
        self.wd.children[dirname] = Directory(dirname, self.wd)
      else:
        [filesize, filename] = content.split(' ')
        self.wd.children[filename] = File(filename, int(filesize), self.wd)

with open('day7/input.txt') as f:
  file_system = FileSystem()
  lines = f.readlines()
  i = 1
  while i < len(lines):
    line = lines[i].strip()
    if line.startswith('$ cd'):
      file_system.cd(line[2:].split(' ')[1])
    elif line.startswith('$ ls'):
      j = i + 1

      contents = []
      while j < len(lines) and not lines[j].startswith('$'):
        contents.append(lines[j].strip())
        j += 1
      file_system.ls(contents)

      i = j - 1

    i +=1

print(file_system.get_small_size())
needed = 30000000 - (70000000 - file_system.get_size())
print(file_system.smallest_directory_larger_than(needed))
