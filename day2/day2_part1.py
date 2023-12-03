number_of_cubes_limit = {"red": 12, "blue": 14, "green": 13}
text_file = "day2_input.txt"
# text_file = "day2_input_test.txt"
def check_valid_game(line):
  games = line.split(':')[1].split(';')
  for game in games:
    cubes = game.split(",")
    
    for cube in cubes:
      trimmed_cube = cube.strip()
      num_of_cubes, color = trimmed_cube.split(' ') 
      if int(num_of_cubes) > number_of_cubes_limit[color]:
        return False
  return True
  
def get_game_id(line):
  return line.split(':')[0].split(" ")[1] 

def count_valid_games():
  num_of_valid_games = 0
  with open(text_file) as f:
    lines = f.readlines()
    for line in lines:
      if check_valid_game(line.strip()):
        num_of_valid_games += int(get_game_id(line.strip()))
  
  return num_of_valid_games

print(count_valid_games())