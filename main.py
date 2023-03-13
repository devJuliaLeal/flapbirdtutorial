import pygame
import neat
import time
import os
import random


WIN_WIDTH = 600
WIN_HEIGHT = 800


BIRD_IMGS = [pygame.tranform.scale2x(pygame.image.load(os.path.join("img", "bird1.png"))), pygame.tranform.scale2x(
    pygame.image.load(os.path.join("img", "bird2.png"))), pygame.tranform.scale2x(pygame.image.load(os.path.join("img", "bird3.png")))]
PIPE_IMG = [pygame.tranform.scale2x(
    pygame.image.load(os.path.join("img", "pipe.png")))]
BASE_IMG = [pygame.tranform.scale2x(
    pygame.image.load(os.path.join("img", "base.png")))]
BACKGROUND_IMG = [pygame.tranform.scale2x(
    pygame.image.load(os.path.join("img", "bg.png")))]


class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TONE = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel*self.tick_count + 1, 5*self.tick_count**2

        if d >= 16:
            d = 16
        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL


def draw(self, win):
    self.img_count += 1

    if self.img_count < self.ANIMATION_TIME:
        self.img = self.IMGS[0]
    elif self. img_count < self. ANIMATION_TIME*2:
        self.img_count = self.IMGS[1]
    elif self. img_count < self. ANIMATION_TIME*3:
        self.img_count = self.IMGS[2]
    elif self. img_count < self. ANIMATION_TIME*4:
        self.img_count = self.IMGS[1]
    elif self. img_count < self. ANIMATION_TIME*4 + 1:
        self.img_count = self.IMGS[0]
        self.img_count = 0

    if self.tilt <= -80:
        self.img = self.IMGS[1]
        self.img_count = self.ANIMATION_TIME*2

    rotated_image = pygame.tranform.rotate(self.img, self.tilt)
    new_rect = rotated_image.get_rect(
        center=self.img.get_rect(topleft=(self.x, self.y)).center)


while True:
    Bird.move()