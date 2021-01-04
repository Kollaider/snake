import pygame

size = [600, 800]

screen = pygame.display.set_mode(size)      #creating window
pygame.display.set_caption('Snake')         #setting caption

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()