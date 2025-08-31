import pygame
from constants import GRID_SIZE, GAME_AREA_WIDTH, GAME_AREA_HEIGHT, GREEN, DARK_GREEN, RED, LIGHT_GRAY, DIFFICULTY_EASY, DIFFICULTY_MEDIUM, DIFFICULTY_HARD, FOOD_TYPE_REGULAR, FOOD_TYPE_POISON, BLACK
from utils import place_food, display_text

class SnakeGame:
    def __init__(self):
        self.snake_pos = []
        self.snake_direction = ''
        self.food_positions = [] # Ahora es una lista
        self.score = 0
        self.current_difficulty_str = "Fácil" # Almacenar la dificultad actual
        self.reset_game(self.current_difficulty_str) # Dificultad inicial

    def _generate_initial_food(self, num_food_items):
        self.food_positions = []
        for _ in range(num_food_items):
            self.food_positions.append(place_food())

    def reset_game(self, difficulty_str):
        # Posición inicial de la serpiente dentro del área de juego
        self.snake_pos = [[100, 40], [80, 40], [60, 40]] 
        self.snake_direction = 'RIGHT'
        self.score = 0
        self.current_difficulty_str = difficulty_str # Actualizar la dificultad

        # Ajustar velocidad y cantidad de frutas según la dificultad
        if difficulty_str == "Fácil":
            self.current_speed = 7
            self._generate_initial_food(3)
        elif difficulty_str == "Medio":
            self.current_speed = 10
            self._generate_initial_food(3)
        elif difficulty_str == "Difícil":
            self.current_speed = 12 # Velocidad ajustada para difícil
            self._generate_initial_food(1) # Solo 1 fruta en difícil

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

        # Lógica para atravesar murallas (wrapping) - Solo si no es dificultad Fácil
        if self.current_difficulty_str != "Fácil":
            if new_head[0] >= GAME_AREA_WIDTH:
                return False # Game Over si choca con pared en Medio/Difícil
            elif new_head[0] < 0:
                return False # Game Over si choca con pared en Medio/Difícil
            if new_head[1] >= GAME_AREA_HEIGHT:
                return False # Game Over si choca con pared en Medio/Difícil
            elif new_head[1] < 0:
                return False # Game Over si choca con pared en Medio/Difícil
        else: # Dificultad Fácil: atraviesa murallas
            if new_head[0] >= GAME_AREA_WIDTH:
                new_head[0] = 0
            elif new_head[0] < 0:
                new_head[0] = GAME_AREA_WIDTH - GRID_SIZE
            if new_head[1] >= GAME_AREA_HEIGHT:
                new_head[1] = 0
            elif new_head[1] < 0:
                new_head[1] = GAME_AREA_HEIGHT - GRID_SIZE

        self.snake_pos.insert(0, new_head) # Añadir nueva cabeza

        # Comprobar si la serpiente choca consigo misma
        if new_head in self.snake_pos[1:]:
            return False # Game Over si choca consigo misma

        # Comprobar si la serpiente come la comida
        food_eaten_index = -1
        for i, food in enumerate(self.food_positions):
            if new_head == food[:2]: # Comparar solo coordenadas (x, y)
                food_eaten_index = i
                break

        if food_eaten_index != -1:
            food_eaten = self.food_positions[food_eaten_index]
            if food_eaten[2] == FOOD_TYPE_POISON: # Si es fruta venenosa
                return False # Game Over
            else: # Fruta regular
                self.score += 1
                self.food_positions.pop(food_eaten_index)
                self.food_positions.append(place_food()) # Reemplazar la fruta comida
        else:
            self.snake_pos.pop() # Eliminar la cola (solo si no ha comido)
        return True # Game continues

    def draw(self, screen):
        # Dibujar la cuadrícula
        for x in range(0, GAME_AREA_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, GAME_AREA_HEIGHT))
        for y in range(0, GAME_AREA_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, LIGHT_GRAY, (0, y), (GAME_AREA_WIDTH, y))

        # Dibujar todas las comidas (manzanas)
        for food_data in self.food_positions:
            food_pos = food_data[:2] # Coordenadas
            food_type = food_data[2] # Tipo
            color = RED if food_type == FOOD_TYPE_REGULAR else BLACK # Rojo para regular, Negro para venenosa
            pygame.draw.circle(screen, color, (food_pos[0] + GRID_SIZE // 2, food_pos[1] + GRID_SIZE // 2), GRID_SIZE // 2)

        # Dibujar la serpiente
        for i, segment in enumerate(self.snake_pos):
            if i == 0: # Cabeza de la serpiente
                pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
            else: # Cuerpo de la serpiente
                pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

        