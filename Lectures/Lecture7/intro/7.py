import pygame

pygame.init() # initializies all
# pygame submodules

# create our game window (game surface)
WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True # variable responsible for our game loop

is_yellow = False

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

mov_speed = 1

clock = pygame.time.Clock()

FPS = 60 # Frames per second

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y -= mov_speed
    if keys[pygame.K_DOWN]:
        circle_y += mov_speed
    if keys[pygame.K_RIGHT]:
        circle_x += mov_speed
    if keys[pygame.K_LEFT]:
        circle_x -= mov_speed

    # fill the screen with a color to wipe away anything from last frame
    circle_pos = (circle_x, circle_y)
    if is_yellow:
        screen.fill("yellow")
        pygame.draw.circle(screen, "purple", circle_pos, 40)
    else:
        screen.fill("purple")
        pygame.draw.circle(screen, "yellow", circle_pos, 40)


    # updates the screen (game window)
    pygame.display.flip()

    clock.tick(FPS) # set the FPS limit for the game