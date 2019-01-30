from enum import Enum, auto

class Turn(Enum):
    left = auto()
    right = auto()
    straight = auto()

class Cart:
    def __init__(self, ch):
        self.ch = ch
        self.next_turn = Turn.left
    def __repr__(self):
        return self.ch

tracks = []
carts = dict()

with open('day13-input.txt') as f:
    tracks = [list(line.strip("\n")) for line in f.readlines()]

for y_pos, line in enumerate(tracks):
    for x_pos, ch in enumerate(line):
        if ch in ["<", ">", "^", "v"]:
            carts[(x_pos, y_pos)] = Cart(ch)
            if ch in ["<", ">"]:
                tracks[y_pos][x_pos] = "-"
            else:
                tracks[y_pos][x_pos] = "|"

found = False
while not found:
    for (x, y), cart in sorted(carts.items(), key=lambda x:(x[0][1], x[0][0])):
        old_ch = cart.ch
        old_pos = (x, y)
        new_pos = (x, y)
        track = tracks[y][x]
        if track == "\\":
            if cart.ch == "<":
                cart.ch = "^"
            elif cart.ch == ">":
                cart.ch = "v"
            elif cart.ch == "^":
                cart.ch = "<"
            elif cart.ch == "v":
                cart.ch = ">"
        elif track == "/":
            if cart.ch == "<":
                cart.ch = "v"
            elif cart.ch == ">":
                cart.ch = "^"
            elif cart.ch == "^":
                cart.ch = ">"
            elif cart.ch == "v":
                cart.ch = "<"
        elif track == "+":
            if cart.next_turn == Turn.left:
                cart.next_turn = Turn.straight
                if cart.ch == "<":
                    cart.ch = "v"
                elif cart.ch == ">":
                    cart.ch = "^"
                elif cart.ch == "^":
                    cart.ch = "<"
                elif cart.ch == "v":
                    cart.ch = ">"
            elif cart.next_turn == Turn.right:
                cart.next_turn = Turn.left
                if cart.ch == "<":
                    cart.ch = "^"
                elif cart.ch == ">":
                    cart.ch = "v"
                elif cart.ch == "^":
                    cart.ch = ">"
                elif cart.ch == "v":
                    cart.ch = "<"
            elif cart.next_turn == Turn.straight:
                cart.next_turn = Turn.right
        if cart.ch == "<":
            new_pos = (x-1, y)
        elif cart.ch == ">":
            new_pos = (x+1, y)
        elif cart.ch == "^":
            new_pos = (x, y-1)
        elif cart.ch == "v":
            new_pos = (x, y+1)
        if new_pos in carts:
            print(new_pos)
            found = True
            break
        del carts[old_pos]
        carts[new_pos] = cart
