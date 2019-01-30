rounds = 704321

scores = [3, 7]
idx1 = 0
idx2 = 1

while len(scores) < rounds + 10:
    new_scores = [int(c) for c in str(scores[idx1] + scores[idx2])]
    scores.extend(new_scores)
    idx1 = (idx1 + scores[idx1] + 1) % len(scores)
    idx2 = (idx2 + scores[idx2] + 1) % len(scores)

print("".join(str(i) for i in scores[-10:]))
