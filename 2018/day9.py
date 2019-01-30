players = 405
final_marble = 7170000

one_percent = 7170000//100
scores = [0] * players
circle = [0]
prev_idx = 0

for round in range(1, final_marble+1):
    if round % one_percent == 0:
        print(str(round/one_percent) + "% complete")
    if round % 23 != 0:
        prev_idx = (prev_idx + 2) % len(circle)
        circle.insert(prev_idx, round)
        continue
    player = round % players
    scores[player] += round
    prev_idx = (prev_idx - 7) % len(circle)
    scores[player] += circle.pop(prev_idx)

print(max(scores))
