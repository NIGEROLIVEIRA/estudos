xs = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
def x():
    for x in xs:
        lista.append(x)
        xs.pop(0)
        break
ys = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
def y():
    for y in ys:
        lista.append(y)
        ys.pop(0)
        break
zs = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
def z():
    for z in zs:
        lista.append(z)
        zs.pop(0)
        break


lista = []
for c in range(1, 11):
    x()
    y()
    z()
print(lista)