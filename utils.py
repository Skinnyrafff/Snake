# utils.py
import pygame
import random
from constants import GAME_AREA_WIDTH, GAME_AREA_HEIGHT, GRID_SIZE, FOOD_TYPE_REGULAR, FOOD_TYPE_POISON, POISON_FOOD_PROBABILITY # Importar constantes

def place_food():
    x = random.randrange(0, GAME_AREA_WIDTH // GRID_SIZE) * GRID_SIZE
    y = random.randrange(0, GAME_AREA_HEIGHT // GRID_SIZE) * GRID_SIZE

    # Decidir si la fruta es regular o venenosa
    food_type = FOOD_TYPE_REGULAR
    if random.random() < POISON_FOOD_PROBABILITY: # random.random() devuelve un float entre 0.0 y 1.0
        food_type = FOOD_TYPE_POISON

    return [x, y, food_type]

def display_text(screen, text, size, x, y, color):
    font = pygame.font.SysFont("Arial", size) # Usar una fuente específica
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)