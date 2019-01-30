plants = set()
rules = dict()

def get_state_around(plant):
  s = []
  for i in range(plant - 4, plant + 5):
    s.append(i in plants)
  return tuple(s)

def parse_initial_state(s):
  for i, ch in enumerate(s):
    if ch == "#":
      plants.add(i)

def read_rules():
  with open('day12-input.txt') as f:
    for line in f:
      rule_cond = []
      for ch in line[:5]:
        rule_cond.append(ch == "#")
      rules[tuple(rule_cond)] = line.strip()[-1] == "#"

parse_initial_state("###.#..#..##.##.###.#.....#.#.###.#.####....#.##..#.#.#..#....##..#.##...#.###.#.#..#..####.#.##.#")
read_rules()

num_gens = 500
for t in range(1,num_gens + 1):
  new_plants = set()
  for plant in plants:
    state = get_state_around(plant)
    for i in range(5):
      if rules[state[i:i+5]]:
        new_plants.add(plant + i - 2)
  plants = new_plants
  print(sum(plants))
