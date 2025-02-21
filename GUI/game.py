import pygame as pg
import sys
import saper
from pygame.color import THECOLORS

pg.init()

screen = pg.display.set_mode((294, 362))
screen.fill(THECOLORS['whitesmoke'])
pg.display.set_caption('SAPER')

bg_rect = pg.Rect(4, 4, 286, 354)
pg.draw.rect(screen, THECOLORS['grey76'], bg_rect)

upper_stats_bar = pg.Rect(12, 12, 270, 60)
pg.draw.rect(screen, THECOLORS['grey60'], upper_stats_bar)

pole_rect = pg.Rect(12, 12+60+8, 270, 270)
pg.draw.rect(screen, THECOLORS['grey60'], pole_rect)


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    pg.display.flip()