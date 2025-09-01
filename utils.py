# utils.py
import pygame
import random
from constants import GAME_AREA_WIDTH, GAME_AREA_HEIGHT, GRID_SIZE, FOOD_TYPE_REGULAR, FOOD_TYPE_POISON, POISON_FOOD_PROBABILITY

# Cache for fonts
_font_cache = {}

def place_food():
    """Coloca una fruta en una posición aleatoria del mapa."""
    x = random.randrange(0, GAME_AREA_WIDTH // GRID_SIZE) * GRID_SIZE
    y = random.randrange(0, GAME_AREA_HEIGHT // GRID_SIZE) * GRID_SIZE

    food_type = FOOD_TYPE_REGULAR
    if random.random() < POISON_FOOD_PROBABILITY:
        food_type = FOOD_TYPE_POISON

    return [x, y, food_type]

def display_text(screen, text, size, x, y, color):
    """Muestra texto en la pantalla."""
    font_key = (size) # Use size as key for caching
    if font_key not in _font_cache:
        _font_cache[font_key] = pygame.font.SysFont("Arial", size)
    font = _font_cache[font_key]
    
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)