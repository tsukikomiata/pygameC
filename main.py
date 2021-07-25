import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 10
size = (500, 500)
x, y, w, h = 0, 0, 0, 0
screen = pg.display.set_mode(size)
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
            x, y = event.pos
        if event.type == pg.MOUSEBUTTONUP:
            arr.append((x, y, w, h))
            drawing = False
        if event.type == pg.MOUSEMOTION:
            w, h = event.pos[0] - x, event.pos[1] - y
        if event.type == pg.KEYDOWN and event.mod == pg.KMOD_LCTRL and event.key == pg.K_z:
            cancel()
    screen.fill(pg.Color('black'))
    if drawing:
        pg.draw.rect(screen, (0, 255, 127), ((x, y), (w, h)), 1)
    for coords in arr:
        pg.draw.rect(screen, (0, 255, 127), coords, 1)
    pg.display.flip()

pg.quit()