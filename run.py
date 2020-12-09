import pygame, sys
from random import randint
from player import Player
from apple import Apple
from collision import Collision

class Game:

    def __init__(self):
        # Config
        # tps = ticks per second
        self.tps_max = 50.0
        self.screen_width = 800
        self.screen_height = 600

        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake by Max')

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Player(3)
        self.apple = Apple(5,5)
        self.collision = Collision()

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # Drawing
            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            self.apple.draw(self.screen)
            pygame.display.flip()

    def tick(self):
        # Checking inputs
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.moveLeft()
        elif keys[pygame.K_RIGHT]:
            self.player.moveRight()
        elif keys[pygame.K_UP]:
            self.player.moveUp()
        elif keys[pygame.K_DOWN]:
            self.player.moveDown()

        self.player.update()

        # does snake eat apple?
        for i in range(0, self.player.length):
            if self.collision.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 50):
                self.apple.x = randint(1, 14) * 50
                self.apple.y = randint(1, 10) * 50
                self.player.length = self.player.length + 1

        # does snake collide with itself?
        for i in range(2, self.player.length):
            if self.collision.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)

if __name__ == "__main__":
    Game()
