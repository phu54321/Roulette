from eudplib import *

x = open('tiledata', 'rb').read()
k = []
for i in range(65536):
    j = b2i2(x, i * 2)
    if j == 0x1AA3:
        j = 0x0100
    k.append(j)

x0 = 128 - 8 * 6
y0 = 128 - 4 * 3

def tindex(x, y):
    return y * 256 + x

tb = [
    32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
    24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26,
]

for megax in range(12):
    for megay in range(3):
        n = megax * 3 + megay + 1
        if tb.index(n) % 2 == 0:
            t = 0x20
        else:
            t = 0x80
        for subx in range(1, 8):
            for suby in range(1, 8):
                ti = tindex(x0 + megax * 8 + subx, y0 + (2 - megay) * 8 + suby)
                if k[ti] != 0x47a8:
                    k[ti] = t
                else:
                    k[ti] = 0x10

x = b''.join(i2b2(y) for y in k)
print(len(x))
open('td2', 'wb').write(x)
