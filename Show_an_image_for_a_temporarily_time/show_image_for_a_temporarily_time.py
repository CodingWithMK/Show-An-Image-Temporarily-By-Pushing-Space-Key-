## Display image with "SPACE" key push

import pygame

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Patlama Resmi")

image = pygame.image.load("resizeexplosion.png")

x = 50
y = 50

def show_image():
    screen.blit(image, (305, 230))
    pygame.display.update()

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            show_image()
            pygame.time.wait(1000)

    screen.fill((0, 0, 0))
    pygame.display.update()

pygame.quit()