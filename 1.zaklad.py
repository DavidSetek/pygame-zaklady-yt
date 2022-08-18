import pygame

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Hlavní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Updatujeme obrazovku
    pygame.display.update()

# Ukončení hry
pygame.quit()
