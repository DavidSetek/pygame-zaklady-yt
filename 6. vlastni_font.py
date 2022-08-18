# 4. část - fonty a texty
import pygame

# Inicializace hry
pygame.init()

# Obrazovka
width = 600
height = 300
screen = pygame.display.set_mode((width, height))

# Barvy
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Systémové fonty
# fonts = pygame.font.get_fonts()
# for one_font in fonts:
#     print(one_font)

# Nastavení fontu
system_font = pygame.font.SysFont("kokila", 50)
system_font_2 = pygame.font.SysFont("vivaldi", 50)
custom_font = pygame.font.Font("fonts/Harry.ttf", 50)

# Font a text
# system_text = system_font.render("Harry Potter", True, white, red)
# system_text_rect = system_text.get_rect()
# system_text_rect.center = (width//2, height//2)

system_text_2 = system_font_2.render("Albus Brumbál", True, white, green)
system_text_2_rect = system_text_2.get_rect()
system_text_2_rect.topleft = (0, 0)

custom_text = custom_font.render("Harry Potter", True, white, red)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (width//2, height//2)

# Hlavní cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False

    # Text
    # screen.blit(system_text, system_text_rect)
    screen.blit(system_text_2, system_text_2_rect)
    screen.blit(custom_text, custom_text_rect)

    # Update obrazovky
    pygame.display.update()

# Ukončení hry
pygame.quit()
