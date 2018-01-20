from eudplib import *
import math


subSubAngleNum = 2
subAngleNum = 20
angleNum = 37 * subAngleNum


def signedDiv(x, y):
    if EUDIf()(x >= 0x80000000):
        x << -(-x // y)
    if EUDElse()():
        x << x // y
    EUDEndIf()
    return x


@EUDFunc
def f_roulette_lengthdir(length, angle):
    # sin, cos table
    clist = []
    slist = []
    dangle = 2 * math.pi / angleNum

    for i in range(angleNum):
        clist.append(math.floor(math.cos(dangle * (i - 7)) * 65536 + 0.5))
        slist.append(math.floor(math.sin(dangle * (i - 7)) * 65536 + 0.5))

    cdb = EUDArray(clist)
    sdb = EUDArray(slist)

    # MAIN LOGIC
    angle %= angleNum

    tablecos = cdb[angle]
    tablesin = sdb[angle]
    ldir_x = signedDiv(tablecos * length, 65536)
    ldir_y = signedDiv(tablesin * length, 65536)

    return ldir_x, ldir_y
