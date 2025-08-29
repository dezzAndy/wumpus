import pygame

# Setup de Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.polygon(screen, (255, 255, 255), ((640.0, 110.0),
                                                    (877.55, 277.64),
                                                    (791.11, 552.36),
                                                    (488.89, 552.36),
                                                    (402.45, 277.64)), 5)
    pygame.draw.polygon(screen, (255, 255, 255), [(640.00, 110.00),
                                                    (493.05, 157.75),
                                                    (402.24, 282.75),
                                                    (402.24, 437.25),
                                                    (493.05, 562.25),
                                                    (640.00, 610.00),
                                                    (786.95, 562.25),
                                                    (877.76, 437.25),
                                                    (877.76, 282.75),
                                                    (786.95, 157.75)], 5)

    pygame.draw.circle(screen, "red", player_pos, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()