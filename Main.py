# ToDo Fire bullets based off right joystick
# ToDo Destroy bullets on map edge
# ToDo Place enemies around map
# ToDo Kill enemies on bullet contact
# ToDo Kill sprite on enemy contact
# ToDo Enemies 'chase' sprite

# ToDo Rotate sprite while moving

import sys
import pygame

# from math import tan


pygame.init()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()

clock = pygame.time.Clock()

size = width, height = 1200, 600
screen = pygame.display.set_mode(size)
center = (width / 2, height / 2)
black = 25, 25, 25
purple = (23, 5, 54)
fps = 30


class Sprite(object):
    def __init__(self):
        self.ship_image = pygame.image.load('Sprite.png').convert()
        self.ship_image = pygame.transform.scale(self.ship_image, (64, 64))
        self.ship_image.set_colorkey(purple)
        self.rot_image = self.ship_image
        self.shiprect = self.ship_image.get_rect(center=center)

    def move_me(self, x, y):
        if self.shiprect.left + x < 0:
            self.shiprect.left = 0
            x = 0
        if self.shiprect.right + x > width:
            self.shiprect.right = width
            x = 0
        if self.shiprect.top + y < 0:
            self.shiprect.top = 0
            y = 0
        if self.shiprect.bottom + y > height:
            self.shiprect.bottom = height
            y = 0
        self.shiprect.move_ip(x, y)

    # try:
    # 	theta = tan(y/x)
    # except ZeroDivisionError:
    # 	theta = 0
    # self.ship_image = pygame.transform.rotate(self.ship_image, theta)
    # self.shiprect = self.ship_image.get_rect(center=self.shiprect.center)


class Bullet(object):
    def __init__(self):
        pass


def game():
    ship = Sprite()
    bullets = []
    enemies = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print 'Exiting'
                sys.exit()

        ship.move_me(int(my_joystick.get_axis(0) * 4) * 7.5, int(my_joystick.get_axis(1) * 4) * 7.5)

        screen.fill(black)
        screen.blit(ship.ship_image, ship.shiprect)
        pygame.display.update()

        clock.tick(fps)


if __name__ == '__main__':
    game()
