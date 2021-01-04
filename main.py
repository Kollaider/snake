import pygame
SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
HEADER_COLOR = (0, 204, 153)
COUNT_BLOCKS = 25
HEADER_MARGIN = 70
MARGIN = 1
size = [SIZE_BLOCK*COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN*SIZE_BLOCK, 800]



screen = pygame.display.set_mode(size)      #creating window
pygame.display.set_caption('Snake')         #setting caption

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column)%2==0:
                color = BLUE
            else:
                color = WHITE
            pygame.draw.rect(screen, color, (SIZE_BLOCK +column*SIZE_BLOCK + MARGIN*(column+1),
                                             HEADER_MARGIN + row * SIZE_BLOCK + MARGIN*(row + 1), SIZE_BLOCK, SIZE_BLOCK))

    pygame.display.flip()