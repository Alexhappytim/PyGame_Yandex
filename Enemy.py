import random

from sprites import *
from constant import *

enemy_sprites = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(enemy_sprites)
        self.x, self.y = pos_x, pos_y
        print(pos_x, pos_y)
        while pos_x - width // 2 < self.x < pos_x + width // 2 and pos_y - height // 2 < self.y < pos_y + height // 2:
            self.x = random.randrange(pos_x - width, pos_x + width)
            self.y = random.randrange(pos_x - height, pos_x + height)

        self.start_x = self.x
        self.start_y = self.y
        self.sprite = AnimatedSprite(load_image("animation/enemy/front.png"), 2, 1, self.x, self.y)
        self.rect = self.sprite.rect.move(self.x, self.y)
        self.mask = pygame.mask.from_surface(self.sprite.image)

        self.speed = 4
        self.error = 2
        self.go = 50
        self.health = 10

    def update(self, x, y):
        args = [[]]
        if self.x + self.go < x:
            args[0].append('d')
        elif self.x - self.go > x:
            args[0].append('a')
        if self.y + self.go < y:
            args[0].append('s')
        elif self.y - self.go > y:
            args[0].append('w')
        koef = 1
        if len(args[0]) > 1:
            koef = 3 / 4
        koef *= 0.75
        if "s" in args[0]:
            self.y += int(random.randrange(self.speed - self.error, self.speed + self.error) * koef)
        if "a" in args[0]:
            self.x -= int(random.randrange(self.speed - self.error, self.speed + self.error) * koef)
        if "d" in args[0]:
            self.x += int(random.randrange(self.speed - self.error, self.speed + self.error) * koef)
        if "w" in args[0]:
            self.y -= int(random.randrange(self.speed - self.error, self.speed + self.error) * koef)
        self.sprite.pos = (self.x, self.y)
        self.rect = self.sprite.rect
        # self.rect = pygame.rect.Rect(self.x, self.y, self.rect.w, self.rect.h)
        if self.health < 1:
            print(self.health)
            self.sprite.kill()
            self.kill()