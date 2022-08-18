# 2. část - Obrazce
import pygame

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Definujeme barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Barva pozadí
screen.fill(black)

# Tvary
# - Čára
pygame.draw.line(screen, white, (0, 0), (width//2, height//2), 5)
# - Kružnice
pygame.draw.circle(screen, red, (width//2, height//2), 100, 2)
# - Kruh
pygame.draw.circle(screen, yellow, (width//2, height//2), 90, 0)
# - Čtverec, Obdélník
pygame.draw.rect(screen, blue, (width//2 - 50, height//2 - 50, 100, 100))

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
