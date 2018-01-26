from eudplib import *

stringTable = EUDArray([
    EncodeString("\x03※※ \x04룰렛 번호는 \x07[%d]\x04입니다. \x03※※" % i)
    for i in range(37)
])
