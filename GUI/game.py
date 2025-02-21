import pygame as pg
import sys
from pygame.color import THECOLORS
import saper


pg.init()


screen = pg.display.set_mode((294, 362))
screen.fill(THECOLORS['whitesmoke'])
pg.display.set_caption('SAPER')

with open('D:/PyCharmPr/SAPER/GUI/borders.txt', encoding='utf-8') as const:
    const_list = const.readlines()
    ### NE TROGATb SLOVAR
    BORDERS = {s[:s.find('=')].rstrip(): int(s[s.find('= '):].lstrip('= ')) for s in const_list} ### polny pizdec
    ### NE TROGATb SLOVAR
    inner = BORDERS['inner']
    outer = BORDERS['outer']

bg_rect = pg.Rect(outer, outer, 286, 354)
pg.draw.rect(screen, THECOLORS['grey76'], bg_rect)

upper_stats_bar = pg.Rect(outer+inner, outer+inner, 270, 60)
pg.draw.rect(screen, THECOLORS['grey60'], upper_stats_bar)

pole_rect = pg.Rect(outer+inner, outer+inner+inner+60, 270, 270)
pg.draw.rect(screen, THECOLORS['grey60'], pole_rect)

# FIXME
# POLE_GAME = saper.GamePole(9, 10)
# for i in range(len(POLE_GAME.pole)):
#     for j in range(len(POLE_GAME.pole[i])):
#         cell = pg.Rect((outer+inner), 30, 30)
#         pg.draw.rect(screen, THECOLORS['black'], cell)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
    pg.display.flip()