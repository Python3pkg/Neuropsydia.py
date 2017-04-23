# -*- coding: utf-8 -*-
"""
Module initializing screen object and screen values.
"""
import pygame
from .path import *

if __name__ == "__main__":  # This is to avoid sphinx to run this code, otherwise the documentations fails to be built
    # Add icon to the window
    pygame.display.set_icon(pygame.image.load(Path.logo() + 'icon.png'))

    # Create screen
    screen = pygame.display.set_mode((0,0), pygame.SRCALPHA | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)

    # Name the screen
    pygame.display.set_caption('Neuropsydia')

    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    monitor_diagonal = 24  # inch
