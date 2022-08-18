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
distance = 5

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

        if event.type == pygame.KEYDOWN:
            # print(pygame.key.name(event.key))
            if event.key == pygame.K_UP:
                # potter_image_rect.y = potter_image_rect.y - 10
                potter_image_rect.y -= distance
            elif event.key == pygame.K_DOWN:
                # potter_image_rect.y = potter_image_rect.y + 10
                potter_image_rect.y += distance
            elif event.key == pygame.K_LEFT:
                potter_image_rect.x -= distance
            elif event.key == pygame.K_RIGHT:
                potter_image_rect.x += distance

    # Vyplnění obrazovky černou barvou
    screen.fill((0, 0, 0))

    # Obrázky
    screen.blit(potter_image, potter_image_rect)

    # update obrazovky
    pygame.display.update()

# Ukončení hry
pygame.quit()
