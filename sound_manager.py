# This module manages the custom sound effects and plays them as well

# IMPORTANT NOTE: Run the terminal command "pip install pygame-ce" to install the pygame library first!

import pygame

pygame.init()
pygame.mixer.init() # initiates pygame's sound stuff

def play_sound(file_path):
    sound = pygame.mixer.Sound(file_path)
    sound.play()