# 6. část - události na klávesnici

import pygame

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Základní nastavení
distance = 10
fps = 60
clock = pygame.time.Clock()

# Obrázek
potter_image = pygame.image.load("img/harryPotter.png")
potter_image_rect = potter_image.get_rect()
potter_image_rect.center = (width//2, height//2)

# Hlavní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # w - nahoru, s - dolů, a - vlevo, d - vpravo
    # Pohybujeme obrázkem
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and potter_image_rect.top > 0:
        potter_image_rect.y -= distance
    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and potter_image_rect.bottom < height:
        potter_image_rect.y += distance
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and potter_image_rect.left > 0:
        potter_image_rect.x -= distance
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and potter_image_rect.right < width:
        potter_image_rect.x += distance

    # Vyplnění obrazovky černou barvou
    screen.fill((0, 0, 0))

    # Obrázky
    screen.blit(potter_image, potter_image_rect)

    # update obrazovky
    pygame.display.update()

    # tikání hodin
    clock.tick(fps)

# Ukončení hry
pygame.quit()