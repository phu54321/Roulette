import math
import cairo

# draw player

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 256, 256)
ctx = cairo.Context(surface)
ctx.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
ctx.scale(2, 2)

nums = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
    24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

COLOR_ZERO = (0, 1, 0)
COLOR_OPOS = (0, 0, 0)
COLOR_EPOS = (1, 0, 0)


def drawSeg(r1, r0, dangle):
    ctx.arc(
        64, 64, r1,
        -dangle / 2 - math.pi / 2,
        dangle / 2 - math.pi / 2
    )
    ctx.arc_negative(
        64, 64, r0,
        dangle / 2 - math.pi / 2,
        -dangle / 2 - math.pi / 2
    )


ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(7)

ctx.rectangle(0, 0, 128, 128)
ctx.set_source_rgb(.1, .1, .1)
ctx.fill()

for i, num in enumerate(nums):
    dangle = 2 * math.pi / len(nums)
    sangle = -dangle * i

    ctx.save()
    ctx.translate(64, 64)
    ctx.rotate(sangle)
    ctx.translate(-64, -64)

    # Draw wood boundary/inner thing
    ctx.set_source_rgb(150 / 255, 80 / 255, 20 / 255)
    drawSeg(64, 63, dangle)
    ctx.fill()

    drawSeg(55, 45, dangle * 1.01)
    ctx.fill()

    # Draw surrounding blocks
    drawSeg(63, 55, dangle)

    if num == 0:
        ctx.set_source_rgb(*COLOR_ZERO)
    elif i % 2 == 0:
        ctx.set_source_rgb(*COLOR_EPOS)
    else:
        ctx.set_source_rgb(*COLOR_OPOS)

    ctx.fill()

    # Draw seg text
    cellText = str(num)
    (x, y, width, height, dx, dy) = ctx.text_extents(cellText)

    ctx.move_to(64 - width / 2 - x / 2, 7.5)
    ctx.set_source_rgb(1, 1, 1)
    ctx.show_text(cellText)
    ctx.fill()

    # Draw inner seperator
    drawSeg(54, 47, dangle * .7)
    ctx.set_source_rgb(.8, .5, .5)
    ctx.fill()

    ctx.restore()

surface.write_to_png("output2.png")
