# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

x1 = int(input("x1:"))
x2 = int(input("x2:"))
y1 = int(input("y1:"))
y2 = int(input("y2:"))
z1 = int(input("z1:"))
z2 = int(input("z2:"))

def distance(xa, ya, xb, yb):
  return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

ab = distance(x1,y1,x2,y2)
bc = distance(y1,z1,y2,z2)
ac = distance(x1,z1,x2,z2)

min_dist = ab
name = "ab"
if bc < min_dist:
    min_dist = bc
    name = "bc"
if ac < min_dist:
    min_dist = ac
    name = "ac"

print("Самый короткий отрезок:", name)  # Выводим название отрезка, например “АС”.
