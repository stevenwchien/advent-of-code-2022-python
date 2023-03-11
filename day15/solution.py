import re

REGEXP = r'Sensor at x=(?P<x1>-?\d+), y=(?P<y1>-?\d+): closest beacon is at x=(?P<x2>-?\d+), y=(?P<y2>-?\d+)'

class Sensor:
  def __init__(self, pos_x: int, pos_y: int, beacon_x: int, beacon_y: int):
    self.x = pos_x
    self.y = pos_y
    self.beacon_x = beacon_x
    self.beacon_y = beacon_y
    self.closest_dist = abs(beacon_x - pos_x) + abs(beacon_y - pos_y)

  def diff_from_x(self, y_row: int):
    return self.closest_dist - abs(self.y - y_row)

  def num_impossible_spots(self, y_row: int):
    return max(self.diff_from_x(y_row) * 2 + 1, 0)

  def impossible_spots_range(self, y_row: int):
    diff_x = self.diff_from_x(y_row)
    if self.num_impossible_spots(y_row) == 0:
      return None
    else:
      return (self.x-diff_x, self.x+diff_x)

  def __str__(self):
    return f'Sensor: ({self.x},{self.y}). Closest beacon: ({self.beacon_x},{self.beacon_y}). Dist: {self.closest_dist}'

def impossible_range_len(sensors: list[Sensor], y_row: int) -> int:
  ranges = []

  for sensor in sensors:
    impossible_range = sensor.impossible_spots_range(y_row)
    if impossible_range != None:
      ranges.append(impossible_range)

  ranges.sort()

  combined_range_len = 0
  prev_s = ranges[0][0]
  prev_e = ranges[0][1]
  for idx in range(1,len(ranges)):
    (curr_s, curr_e) = ranges[idx]
    if curr_s > prev_e:
      combined_range_len += (prev_e - prev_s)
      prev_s = curr_s
      prev_e = curr_e
    elif curr_s <= prev_e:
      prev_e = max(prev_e, curr_e)

  combined_range_len += (prev_e - prev_s)

  return combined_range_len

def impossible_range(sensors: list[Sensor], y_row: int) -> list:
  ranges = []

  for sensor in sensors:
    impossible_range = sensor.impossible_spots_range(y_row)
    if impossible_range != None:
      ranges.append(impossible_range)

  ranges.sort()

  combined_ranges = []
  prev_s = ranges[0][0]
  prev_e = ranges[0][1]
  for idx in range(1,len(ranges)):
    (curr_s, curr_e) = ranges[idx]
    if curr_s > prev_e:
      combined_ranges.append((prev_s, prev_e))
      prev_s = curr_s
      prev_e = curr_e
    elif curr_s <= prev_e:
      prev_e = max(prev_e, curr_e)

  combined_ranges.append((prev_s, prev_e))

  return combined_ranges

# Part 1
y_row = 2000000
sensors = []
with open('input.txt') as f:
  for line in f:
    m = re.match(REGEXP, line)
    if m == None:
      raise ValueError

    sensor = Sensor(int(m.group('x1')), int(m.group('y1')), int(m.group('x2')), int(m.group('y2')))
    sensors.append(sensor)

  print(impossible_range_len(sensors, y_row))

# Part 2
sensors = []
with open('input.txt') as f:
  for line in f:
    m = re.match(REGEXP, line)
    if m == None:
      raise ValueError

    sensor = Sensor(int(m.group('x1')), int(m.group('y1')), int(m.group('x2')), int(m.group('y2')))
    sensors.append(sensor)

# Run this loop to get: 2753392
# Took a couple minutes
# for y in range(4000000):
#   if len(impossible_range(sensors, 2753392)) > 1:
#     print(y)
#     break

beacon_y_value = 2753392
TUNING_FREQUENCY_MULTIPLIER = 4000000
ranges = impossible_range(sensors, beacon_y_value)
print(impossible_range(sensors, beacon_y_value))
print((ranges[0][1]+1) * TUNING_FREQUENCY_MULTIPLIER + beacon_y_value)
