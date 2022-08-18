# 3. část - obrázky
# https://iconarchive.com/
import pygame

# Inicializace
pygame.init()

# Obrazovka
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Barva pozadí
screen.fill(black)

# Tvar
# pygame.draw.rect(screen, white, (200, 100, 100, 100))

# Obrázky
harry_potter_image = pygame.image.load("img/harryPotter.png")
harry_potter_rect = harry_potter_image.get_rect()
harry_potter_rect.top = 300
harry_potter_rect.left = 200

coin_image = pygame.image.load("img/coin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (width//2, height//2)

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Přidání obrázků
    screen.blit(harry_potter_image, harry_potter_rect)
    screen.blit(coin_image, coin_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení
pygame.quit()