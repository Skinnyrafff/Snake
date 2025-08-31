# utils.py
import pygame
import random
from constants import GAME_AREA_WIDTH, GAME_AREA_HEIGHT, GRID_SIZE, FOOD_TYPE_REGULAR, FOOD_TYPE_POISON, POISON_FOOD_PROBABILITY

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
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)