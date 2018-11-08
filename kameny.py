#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
import random
from math import sin, cos, radians, pi

window = pyglet.window.Window(1000, 800)
batch = pyglet.graphics.Batch()   # pro optimalizované vyreslování objektů


class Stone(object):
    def __init__(self, x=None, y=None, direction=None, speed=None):
        'pokud není atribut zadán vytvořím ho náhodně'
        self.x = x or random.randint(0, window.width)
        if y:
            self.y = y
        else:
            self.y = random.randint(0, window.height)
        self.direction = direction or random.randint(0, 360)
        self.speed = speed or random.randint(30, 150)
        self.rspeed = random.randint(-100, 100)

        'nečtu obrázek'
        num = random.choice(range(0, 20))
        self.image = pyglet.image.load('meteors/{}.png'.format(num))
        'střed otáčení dám na střed obrázku'
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        'z obrázku vytvořím sprite'
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        'správně nastavím souřednice sprite'
        self.sprite.x = self.x
        self.sprite.y = self.y

    def tick(self, dt):
        'do prom. dt se uloží doba od posledního tiknutí'
        self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
        self.sprite.x = self.x
        self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
        self.sprite.y = self.y
        self.sprite.rotation += 0.01 * self.rspeed


stones = []
for i in range(30):
    stone = Stone()
    pyglet.clock.schedule_interval(stone.tick, 1 / 30)
    stones.append(stone)


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
