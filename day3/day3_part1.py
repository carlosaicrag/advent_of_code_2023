import re
input = "day3_input_test.txt"
input = "day3_input.txt"
GEAR = "*"
def is_valid_pos(pos, grid):
  x,y = pos
  if x < 0 or y < 0:
    return False
  try:
    grid[x][y]
    return True
  except IndexError:
    return False

def search_for_symbol(curr_number, grid):
  directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
  
  for char_and_pos in curr_number:
    digit, x, y = char_and_pos
    pos = (x,y)
    for direction in directions:
      poss_pos = (pos[0] + direction[0], pos[1] + direction[1])
      if not is_valid_pos(poss_pos, grid):
        continue  
      x,y = poss_pos
      if re.search(r'[^\w.]', grid[x][y]):
        return True
  return False

def find_sum_part_numbers():
  curr_number = []
  part_numbers = []
  sum = 0
  with open(input, "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]
    for i, row in enumerate(grid):
      for j,char in enumerate(row):
        if char.isdigit():
          curr_number.append([char,i,j])
        else:
          if search_for_symbol(curr_number, grid):
            part_numbers.append(curr_number)
          curr_number = []

      if search_for_symbol(curr_number, grid):
        part_numbers.append(curr_number)
      curr_number = []
              
  for chars_and_pos in part_numbers:
    number = ""
    for char_and_pos in chars_and_pos:
      digit, x, y = char_and_pos
      number += digit
    sum += int(number)
  return sum
    
print(find_sum_part_numbers())     
  
