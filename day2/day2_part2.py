number_of_cubes_limit = {"red": 12, "blue": 14, "green": 13}
text_file = "day2_input.txt"
# text_file = "day2_input_test.txt"
def find_min_power_set(line):
  games = line.split(':')[1].split(';')
  dict_of_cubes = {}
  for game in games:
    cubes = game.split(",")
  
    for cube in cubes:
      trimmed_cube = cube.strip()
      num_of_cubes, color = trimmed_cube.split(' ') 
      
      if color not in dict_of_cubes:
        dict_of_cubes[color] = int(num_of_cubes)
      else:
        dict_of_cubes[color] = max(dict_of_cubes[color], int(num_of_cubes))
        
  power_set = 1
  
  for color in dict_of_cubes:
    power_set *= dict_of_cubes[color]
    
  return power_set


def get_game_id(line):
  return line.split(':')[0].split(" ")[1] 

def find_power_set_sum():
  power_set_sum = 0
  with open(text_file) as f:
    lines = f.readlines()
    for line in lines:
      power_set = find_min_power_set(line.strip())
      power_set_sum += power_set
  
  return power_set_sum

print(find_power_set_sum())
