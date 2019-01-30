magic = [7, 0, 4, 3, 2, 1]

scores = [3, 7]
idx1 = 0
idx2 = 1

while True:
    new_scores = [int(c) for c in str(scores[idx1] + scores[idx2])]
    for score in new_scores:
        scores.append(score)
        if scores[-1*len(magic):] == magic:
            print(len(scores)-len(magic))
    idx1 = (idx1 + scores[idx1] + 1) % len(scores)
    idx2 = (idx2 + scores[idx2] + 1) % len(scores)

