from eudplib import *

x = open('t1', 'rb').read()
k = []
for i in range(65536):
    j = b2i2(x, i * 2)
    k.append(j)


def tindex(x, y):
    return y * 256 + x


def tn(a, b):
    return a * 16 + b


wTileNo = tn(16, 0)
lTileNo = tn(195, 1)
dTileNo = tn(0, 0)
zTileNo = tn(1, 0)

tConvMap = {
    tn(195, 1): tn(8, 0),  # Light tile
    tn(0, 0): tn(2, 0),  # Dark tile
    tn(16, 0): tn(0, 0),  # Number font
}


for x in range(256):
    for y in range(256):
        dist = ((x - 128) ** 2 + (y - 128) ** 2) ** 0.5 / 2
        if 54.5 <= dist <= 63.5:
            ti = tindex(x, y)
            k[ti] = tConvMap.get(k[ti], k[ti])


x = b''.join(i2b2(y) for y in k)
print(len(x))
if len(x) == 131072:
    schk = bytearray(open('../scenario.chk', 'rb').read())
    tileSec = schk.index(b'TILE') + 8
    schk[tileSec: tileSec + len(x)] = x
    open('../scenario2.chk', 'wb').write(schk)
