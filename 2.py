import pygame
import sys
import os

pygame.init()


width, height = 600, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game over")

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image

image = load_image("game_over.png")
image_rect = image.get_rect()


image_rect.x = -image_rect.width

speed = 5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill('blue')


    if image_rect.x < (width // 2 - image_rect.width // 2):
        image_rect.x += speed

    screen.blit(image, image_rect)
    pygame.display.flip()
    pygame.time.Clock().tick(200)

pygame.quit()
sys.exit()