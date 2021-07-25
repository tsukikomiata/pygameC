import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 10
x0, y0, x1, y1 = (0, 0, 0, 0)
size = (500, 500)
screen = pg.display.set_mode(size)
# pg.display.flip()
arr = []
running = True
drawing = False


def cancel():
    if len(arr):
        del arr[len(arr) - 1]


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            drawing = True
            x0, y0 = event.pos

        if event.type == pg.MOUSEBUTTONUP:
            arr.append((x0, y0, x1, y1))
            drawing = False

        if event.type == pg.MOUSEMOTION:
            x1, y1 = event.pos[0] - x0, event.pos[1] - y0

        # if event.type == pg.KEYDOWN and event.mod == pg.KMOD_LCTRL and event.key == pg.K_z:
        #     cancel()

        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()

        if any((keys[pg.K_LCTRL], keys[pg.K_RCTRL])) and keys[pg.K_z]:
            cancel()

    screen.fill(pg.Color('black'))
    if drawing:
        pg.draw.rect(screen, (0, 255, 127), ((x0, y0), (x1, y1)), 1)
    for coords in arr:
        pg.draw.rect(screen, (0, 255, 127), coords, 1)
    pg.display.flip()

pg.quit()