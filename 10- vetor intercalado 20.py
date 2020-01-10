
xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
def x():
    for x in xs:
        lista.append(x)
        xs.pop(0)
        break
ys = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def y():
    for y in ys:
        lista.append(y)
        ys.pop(0)
        break

lista = []
for c in range(1, 11):
    x()
    y()
print(lista)