import pygame

pygame.init() # initializies all
# pygame submodules

# create our game window (game surface)
screen = pygame.display.set_mode((800, 480))

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()