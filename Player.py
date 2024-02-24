import pygame

class Player:
    def __init__(self, x, y, width, height, color, window_width, window_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.step = 5
        self.window_width = window_width
        self.window_height = window_height


    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x - self.step > 0:
            self.x -= self.step
        elif keys[pygame.K_RIGHT] and self.x + self.step + self.width < self.window_width:
            self.x += self.step
        elif keys[pygame.K_UP] and self.y - self.step > 0:
            self.y -= self.step
        elif keys[pygame.K_DOWN] and self.y + self.step + self.height < self.window_height:
            self.y += self.step

        self.rect = (self.x, self.y, self.width, self.height)


