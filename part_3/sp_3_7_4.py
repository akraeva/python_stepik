n = int(input())  # число команд
x = 0
y = 0

for i in range(n):
    direction, steps = input().split()
    steps = int(steps)

    if direction == 'восток':
        dx = steps
    elif direction == 'запад':
        dx = steps * (-1)
    else:
        dx = 0

    if direction == 'север':
        dy = steps
    elif direction == 'юг':
        dy = steps * (-1)
    else:
        dy = 0

    x += dx
    y += dy

print(x, y)
