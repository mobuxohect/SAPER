import pygame as pg
import sys
import saper
from pygame.color import THECOLORS

pg.init()

screen = pg.display.set_mode((300, 400))
screen.fill(THECOLORS['grey43'])
pg.display.set_caption('SAPER')


# upper_stats_bar = pg.Rect(4, 4, 292, 80)
# pg.draw.rect(screen, THECOLORS['grey60'], upper_stats_bar)
#
# pole_rect = pg.Rect(4, 88, 292, 308)
# pg.draw.rect(screen, THECOLORS['grey60'], pole_rect)


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    pg.display.flip()