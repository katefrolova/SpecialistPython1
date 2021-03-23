# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(xa, ya, xb, yb):
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

def in_circle(x1, y1, r1, x2, y2, r2):
    return distance(x1, y1, x2, y2) <= abs(r1 - r2)

print(in_circle(2, 0, 0, 0, 4, 1))
