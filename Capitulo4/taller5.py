X = 7
Y = 8
caballo_x = 0
caballo_y = 0
print(f'({caballo_x}, {caballo_y})', end=' ')
movimiento = True
while caballo_x != X and caballo_y != Y:
    if movimiento:
        caballo_x += 1
        caballo_y += 2
    else:
        caballo_x += 2
        caballo_y += 1
    print(f'({caballo_x}, {caballo_y})', end=' ')
    movimiento = not movimiento