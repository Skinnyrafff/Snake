# utils.py
import pygame
import random
from constants import WIDTH, HEIGHT, GRID_SIZE # Importar constantes

def place_food():
    x = random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE
    y = random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE
    return [x, y]

def display_text(screen, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
