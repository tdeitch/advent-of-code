import time

def get_points():
    points = []
    with open('day10-input.txt') as f:
        for line in f:
            points.append(tuple(int(x) for x in line.strip().split(',')))
    return points

def get_pos_at(t, init_points):
    pos = []
    for point in init_points:
        pos.append((point[0] + point[2] * t, point[1] + point[3] * t))
    return pos

def get_size_at(t, init_points):
    minx = 99999999999
    miny = 99999999999
    maxx = -99999999999
    maxy = -99999999999
    for point in init_points:
        x = point[0] + point[2] * t
        y = point[1] + point[3] * t
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
    return (minx, miny, maxx, maxy)

def get_canvas_at(t, init_points):
    pos = get_pos_at(t, init_points)
    minx, miny, maxx, maxy = get_size_at(t, init_points)
    canvas = [['.']*(maxx-minx+1) for _ in range(maxy-miny+1)]
    for p in pos:
        canvas[p[1]-miny][p[0]-minx] = '#'
    return canvas

def print_canvas(canvas):
    for line in canvas:
        print("".join(line))

points = get_points()
old_size = get_size_at(0, points)
for i in range(1,1000000):
    size = get_size_at(i, points)
    if (size[2] - size[0] > old_size[2] - old_size[0] or size[3] - size[1] > old_size[3] - old_size[1]):
        print()
        print_canvas(get_canvas_at(i-1, points))
        print(i-1)
        break
    old_size = size
