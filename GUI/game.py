import pygame as pg
import sys
from pygame.color import THECOLORS
import saper
import settings

pg.init()

screen = pg.display.set_mode((settings.GameSettings.screen_height, settings.GameSettings.screen_width))
screen.fill(THECOLORS['whitesmoke'])
pg.display.set_caption('SAPER')

outer = settings.GameSettings.BORDERS['outer']
inner = settings.GameSettings.BORDERS['inner']

bg_rect = pg.Rect(outer, outer, 286, 354)
pg.draw.rect(screen, THECOLORS['grey76'], bg_rect)

upper_stats_bar = pg.Rect(outer+inner, outer+inner, 270, 60)
pg.draw.rect(screen, THECOLORS['grey60'], upper_stats_bar)

pole_rect = pg.Rect(outer+inner-2, outer+inner+inner+58, 274, 274)
pg.draw.rect(screen, THECOLORS['grey60'], pole_rect)

gp_00_coords = {'x': outer+inner,
                'y': outer+inner*2+60}

POLE = saper.GamePole(settings.GameSettings.POLE_N, settings.GameSettings.MINES)
POLE.init()
for line in POLE.pole:
    for cell in line:
        cell_rect = pg.Rect(gp_00_coords['x']+(cell.x*30), gp_00_coords['y']+(cell.y*30), 30, 30)
        pg.draw.rect(screen, THECOLORS['grey88'], cell_rect, width=2)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    pg.display.update()