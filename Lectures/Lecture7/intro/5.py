import pygame

pygame.init() # initializies all
# pygame submodules

# create our game window (game surface)
screen = pygame.display.set_mode((800, 480))

running = True # variable responsible for our game loop

is_yellow = False

# game loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_yellow = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_yellow = False

    # fill the screen with a color to wipe away anything from last frame
    if is_yellow:
        screen.fill("yellow")
    else:
        screen.fill("purple")

    # updates the screen (game window)
    pygame.display.flip()