# 5. část - zvuky
import pygame

# Inicializace hry
pygame.init()

# Obrazovku
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Game")

# Barvy
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Barva pozadí
screen.fill(black)

# Fonty
custom_font = pygame.font.Font("fonts/Harry.ttf", 50)

# Font a text
custom_text = custom_font.render("Harry Potter Game", True, green)
custom_text_rect = custom_text.get_rect()
custom_text_rect.midtop = (width//2, 5)

# Tvary
pygame.draw.line(screen, green, (0, 60), (width, 60), 2)

# Nahrání zvuky
sound_boom = pygame.mixer.Sound("media/boom.wav")
sound_noise = pygame.mixer.Sound("media/noise.wav")

# Přehrání zvuku
sound_boom.play()
pygame.time.delay(2000)
sound_noise.play()
pygame.time.delay(2000)

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Text
    screen.blit(custom_text, custom_text_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení hry
pygame.quit()
