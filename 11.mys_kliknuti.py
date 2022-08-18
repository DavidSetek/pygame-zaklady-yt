# 7. část - události myš
import pygame

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Obrázek
potter_image = pygame.image.load("img/harryPotter.png")
potter_image_rect = potter_image.get_rect()
potter_image_rect.midtop = (width//2, 0)

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            potter_image_rect.centerx = event.pos[0]
            potter_image_rect.centery = event.pos[1]

    # Obnova obrazovky
    screen.fill((0, 0, 0))

    # Obrázky
    screen.blit(potter_image, potter_image_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení hry
pygame.quit()
