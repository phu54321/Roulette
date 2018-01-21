from eudplib import *


@EUDFunc
def f_getstringaddr(strid):
    strsection_addr = f_dwread_epd(EPD(0x5993D4))
    stroffset = f_wread(strsection_addr + 2 * strid)
    return strsection_addr + stroffset


def f_p(*args):
    bufStrID = EncodeString("_" * 1000)
    dst = f_getstringaddr(bufStrID)

    args = FlattenList(args)
    for arg in args:
        if isUnproxyInstance(arg, bytes):
            dst = f_dbstr_addstr(dst, Db(arg + b'\0'))
        elif isUnproxyInstance(arg, str):
            dst = f_dbstr_addstr(dst, Db(u2utf8(arg) + b'\0'))
        elif isUnproxyInstance(arg, DBString):
            dst = f_dbstr_addstr(dst, arg.GetStringMemoryAddr())
        elif isUnproxyInstance(arg, int):
            # int and EUDVariable should act the same if possible.
            # EUDVariable has a value of 32bit unsigned integer.
            # So we adjust arg to be in the same range.
            dst = f_dbstr_addstr(dst, Db(
                u2b(str(arg & 0xFFFFFFFF)) + b'\0'))
        elif isUnproxyInstance(arg, EUDVariable):
            dst = f_dbstr_adddw(dst, arg)
        elif IsConstExpr(arg):
            dst = f_dbstr_adddw(dst, arg)
        elif isUnproxyInstance(arg, hptr):
            dst = f_dbstr_addptr(dst, arg._value)
        else:
            raise EPError(
                'Object wit unknown parameter type %s given to f_eudprint.'
                % type(arg)
            )

    DoActions(DisplayText(bufStrID))


def f_b(*args):
    for i in EUDLoopRange(6):
        f_setcurpl(i)
        f_p(*args)
