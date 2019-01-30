serial = 6878

powers = dict()
def get_power(x, y):
    if (x, y) in powers:
        return powers[(x, y)]
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = 0 if power < 100 else int(str(power)[-3])
    power -= 5
    powers[(x, y)] = power
    return power

max_power = -999
max_x = -1
max_y = -1
max_size = -1

for xs in range(1,301):
    for ys in range(1,301):
        print(xs, ys)
        sz_limit = min(301 - xs, 301 - ys)
        power = 0
        for ss in range(1, sz_limit + 1):
            for x in range(xs, xs+ss):
                power += get_power(x, ys + ss - 1)
            for y in range(ys, ys+ss):
                power += get_power(xs + ss - 1, y)
            power -= get_power(xs + ss - 1, ys + ss - 1)
            if power > max_power:
                max_power = power
                max_x = xs
                max_y = ys
                max_size = ss

print(max_power, max_x, max_y, max_size)
