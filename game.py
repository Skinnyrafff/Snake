# game.py
import pygame
from constants import GRID_SIZE, WIDTH, HEIGHT, GREEN, DARK_GREEN, RED, LIGHT_GRAY, SNAKE_SPEED
from utils import place_food, display_text

class SnakeGame:
    def __init__(self):
        self.snake_pos = []
        self.snake_direction = ''
        self.food_pos = []
        self.score = 0
        self.reset_game()

    def reset_game(self):
        self.snake_pos = [[100, 40], [80, 40], [60, 40]]
        self.snake_direction = 'RIGHT'
        self.food_pos = place_food()
        self.score = 0

    def update(self):
        # Mover la serpiente
        head_x, head_y = self.snake_pos[0]
        if self.snake_direction == 'UP':
            new_head = [head_x, head_y - GRID_SIZE]
        elif self.snake_direction == 'DOWN':
            new_head = [head_x, head_y + GRID_SIZE]
        elif self.snake_direction == 'LEFT':
            new_head = [head_x - GRID_SIZE, head_y]
        elif self.snake_direction == 'RIGHT':
            new_head = [head_x + GRID_SIZE, head_y]

        # Lógica para atravesar murallas (wrapping)
        if new_head[0] >= WIDTH:
            new_head[0] = 0
        elif new_head[0] < 0:
            new_head[0] = WIDTH - GRID_SIZE
        if new_head[1] >= HEIGHT:
            new_head[1] = 0
        elif new_head[1] < 0:
            new_head[1] = HEIGHT - GRID_SIZE

        self.snake_pos.insert(0, new_head) # Añadir nueva cabeza

        # Comprobar si la serpiente choca consigo misma
        if new_head in self.snake_pos[1:]:
            return False # Game Over

        # Comprobar si la serpiente come la comida
        if new_head == self.food_pos:
            self.score += 1
            self.food_pos = place_food()
        else:
            self.snake_pos.pop() # Eliminar la cola (solo si no ha comido)
        return True # Game continues

    def draw(self, screen):
        # Dibujar la cuadrícula
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, LIGHT_GRAY, (0, y), (WIDTH, y))

        # Dibujar la comida (manzana)
        pygame.draw.circle(screen, RED, (self.food_pos[0] + GRID_SIZE // 2, self.food_pos[1] + GRID_SIZE // 2), GRID_SIZE // 2)

        # Dibujar la serpiente
        for i, segment in enumerate(self.snake_pos):
            if i == 0: # Cabeza de la serpiente
                pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
            else: # Cuerpo de la serpiente
                pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

        
