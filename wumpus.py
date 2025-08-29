import pygame
import poligons

# Setup de Pygame
pygame.init()
screen = pygame.display.set_mode((720, 720))
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

    #Vertices:
    pentagono   = poligons.shape_poligon( 5, screen.get_width() / 2, screen.get_height() / 2, 160)
    decagono    = poligons.shape_poligon(10, screen.get_width() / 2, screen.get_height() / 2, 320)
    # Pentagono:
    pygame.draw.polygon(screen, (255, 255, 255), pentagono, 5)
    
    # Decagono:
    pygame.draw.polygon(screen, (255, 255, 255), decagono, 5)
    
    # Unión de los vértices del pentagono:
    for i in range(len(pentagono)):
        pygame.draw.line(screen, (255, 255, 255), pentagono[i], decagono[2*i], 5)
        
    # Círculos en los vértices
    for i in range(len(pentagono)):
        pygame.draw.circle(screen, (255, 255, 255), pentagono[i], 15)
    for i in range(len(decagono)):
        if i % 2 == 0:
            pygame.draw.circle(screen, (255, 255, 255), decagono[i], 15)

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