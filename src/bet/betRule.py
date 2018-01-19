from eudplib import *


def pre_init(f, n):
    k = EUDArray(n)

    def _():
        for i in range(n):
            k[i] = EUDFuncPtr(1, 1)(f(i))
    EUDOnStart(_)
    return k


def f_bet_btw(a, b):
    assert 36 % (b - a + 1) == 0
    score = 36 // (b - a + 1)

    @EUDFunc
    def _(x):
        if EUDIf()([a <= x, x <= b]):
            EUDReturn(score)
        if EUDElse()():
            EUDReturn(0)
        EUDEndIf()
    return _


# Bet exacts
def f_bet_exact(a):
    @EUDFunc
    def _(x):
        if EUDIf()(a == x):
            EUDReturn(36)
        if EUDElse()():
            EUDReturn(0)
        EUDEndIf()
    return _


bet_exact = pre_init(f_bet_exact, 37)


def f_bet_corner(a):
    return f_bet_in(a, a + 1, a + 3, a + 4)


bet_corner = pre_init(f_bet_corner, 37)


def f_bet_in(*candidates):
    assert 36 % len(candidates) == 0
    score = 36 // len(candidates)

    @EUDFunc
    def _(x):
        EUDSwitch(x)
        for c in candidates:
            EUDSwitchCase()(c)
            EUDReturn(score)
        EUDSwitchDefault()()
        EUDReturn(0)
        EUDEndSwitch()
    return _


def f_bet_multiple(q, r):
    assert 36 % q == 0

    @EUDFunc
    def _(x):
        if EUDIf()([x >= 1, x % q == r]):
            EUDReturn(q)
        if EUDElse()():
            EUDReturn(0)
        EUDEndIf()
    return _


def f_bet_dark():
    return f_bet_in(1, 12, 14, 16, 18, 19, 21,
                    23, 25, 27, 3, 30, 32, 34, 36, 5, 7, 9)


def f_bet_light():
    return f_bet_in(2, 4, 6, 8, 10, 11, 13, 15, 17,
                    20, 22, 24, 26, 28, 29, 31, 33, 35)
