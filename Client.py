import pygame
from Player import Player

width = 750
height = 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNum = 0

def drawWindow(window, player):
    window.fill((255, 255, 255))
    player.draw(window)
    pygame.display.update()


def main():
    player = Player(50, 50, 100, 100, (0, 0, 255), width, height)
    start = True
    clock = pygame.time.Clock()

    while start:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
        player.move()
        drawWindow(window, player)

main()