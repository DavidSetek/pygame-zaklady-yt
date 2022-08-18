# Small Game
import pygame
import random

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry Potter Small Game")

# Nastavení hry
distance = 5
clock = pygame.time.Clock()
fps = 60
score = 0

# Barvy
# https://0to255.com/
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
dark_yellow = pygame.Color("#938f0c")

# Hudba v pozadí
pygame.mixer.music.load("media/bg-music-hp.wav")
# Přehrání hudby v pozadí
pygame.mixer.music.play(-1, 0.0)
# Nahrání zvuku
hedvika_sound = pygame.mixer.Sound("media/hedvika-sound.mp3")
hedvika_sound.set_volume(0.1)

# Nastavení fontu
font_harry = pygame.font.Font("fonts/Harry.ttf", 30)
# Texty
potter_text = font_harry.render("Harry Potter Game", True, dark_yellow)
potter_text_rect = potter_text.get_rect()
potter_text_rect.centerx = width//2
potter_text_rect.top = 10

# Obrázky
potter_image = pygame.image.load("img/harryPotter.png")
potter_image_rect = potter_image.get_rect()
potter_image_rect.center = (width//2, height//2)

hedvika_image = pygame.image.load("img/owl-icon.png")
hedvika_image_rect = hedvika_image.get_rect()
hedvika_image_rect.center = (50, height//2)

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and potter_image_rect.top > 50:
        potter_image_rect.y -= distance
    elif keys[pygame.K_DOWN] and potter_image_rect.bottom < height:
        potter_image_rect.y += distance
    elif keys[pygame.K_LEFT] and potter_image_rect.left > 0:
        potter_image_rect.x -= distance
    elif keys[pygame.K_RIGHT] and potter_image_rect.right < width:
        potter_image_rect.x += distance

    # Kontrola kolize
    if potter_image_rect.colliderect(hedvika_image_rect):
        hedvika_image_rect.centerx = random.randint(0 + 16, width - 16)
        hedvika_image_rect.centery = random.randint(50 + 16, height - 16)
        score += 1
        hedvika_sound.play()

    # Vykreslení obrazovky
    screen.fill(black)

    # Tvary
    # pygame.draw.rect(screen, red, potter_image_rect, 1)
    # pygame.draw.rect(screen, green, hedvika_image_rect, 1)
    pygame.draw.line(screen, dark_yellow, (0, 50), (width, 50), 2)

    # Texty
    score_text = font_harry.render(f"Score: {score}", True, dark_yellow)
    score_text_rect = score_text.get_rect()
    score_text_rect.x = 10
    score_text_rect.y = 10

    # Obrázky
    screen.blit(potter_image, potter_image_rect)
    screen.blit(hedvika_image, hedvika_image_rect)
    screen.blit(potter_text, potter_text_rect)
    screen.blit(score_text, score_text_rect)

    # Update obrazovky
    pygame.display.update()

    # Tikání hodin
    clock.tick(fps)

# Ukončení hry
pygame.quit()
