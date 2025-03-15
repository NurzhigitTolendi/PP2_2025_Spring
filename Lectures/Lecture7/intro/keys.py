import pygame

pygame.init() # initializies all
# pygame submodules

# create our game window (game surface)
screen = pygame.display.set_mode((800, 480))

running = True

# game loop
while running:
    # event loop
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        print(keys)
        if event.type == pygame.QUIT:
            running = False