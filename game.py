import pygame
from constants import GRID_SIZE, GAME_AREA_WIDTH, GAME_AREA_HEIGHT, GREEN, DARK_GREEN, RED, LIGHT_GRAY, BLACK, WHITE, MAX_MUSIC_VOLUME, MUSIC_VOLUME_INCREMENT_PER_FRUIT, INITIAL_SFX_VOLUME, TOTAL_CELLS
from utils import place_food, display_text

class SnakeGame:
    def __init__(self, eat_sound):
        self.snake_pos = []
        self.snake_direction = ''
        self.food_positions = []
        self.score = 0
        self.current_difficulty_str = "Fácil"
        self.eat_sound = eat_sound # Store eat sound
        self.initial_eat_sound_volume = INITIAL_SFX_VOLUME # Store initial SFX volume
        self.reset_game(self.current_difficulty_str)

    def _generate_initial_food(self, num_food_items):
        self.food_positions = []
        for _ in range(num_food_items):
            self.food_positions.append(place_food())

    def reset_game(self, difficulty_str):
        self.snake_pos = [[100, 40], [80, 40], [60, 40]]
        self.snake_direction = 'RIGHT'
        self.score = 0
        self.current_difficulty_str = difficulty_str
        self.eat_sound.set_volume(self.initial_eat_sound_volume) # Reset eat sound volume

        if difficulty_str == "Fácil":
            self.current_speed = 6
            self._generate_initial_food(3)
        elif difficulty_str == "Medio":
            self.current_speed = 8
            self._generate_initial_food(3)
        elif difficulty_str == "Difícil":
            self.current_speed = 10
            self._generate_initial_food(1)

    def update(self):
        head_x, head_y = self.snake_pos[0]
        if self.snake_direction == 'UP':
            new_head = [head_x, head_y - GRID_SIZE]
        elif self.snake_direction == 'DOWN':
            new_head = [head_x, head_y + GRID_SIZE]
        elif self.snake_direction == 'LEFT':
            new_head = [head_x - GRID_SIZE, head_y]
        elif self.snake_direction == 'RIGHT':
            new_head = [head_x + GRID_SIZE, head_y]

        if self.current_difficulty_str != "Fácil":
            if new_head[0] >= GAME_AREA_WIDTH or new_head[0] < 0 or new_head[1] >= GAME_AREA_HEIGHT or new_head[1] < 0:
                return False
        else:
            if new_head[0] >= GAME_AREA_WIDTH:
                new_head[0] = 0
            elif new_head[0] < 0:
                new_head[0] = GAME_AREA_WIDTH - GRID_SIZE
            if new_head[1] >= GAME_AREA_HEIGHT:
                new_head[1] = 0
            elif new_head[1] < 0:
                new_head[1] = GAME_AREA_HEIGHT - GRID_SIZE

        self.snake_pos.insert(0, new_head)

        if new_head in self.snake_pos[1:]:
            return False

        food_eaten_index = -1
        for i, food in enumerate(self.food_positions):
            if new_head == food[:2]:
                food_eaten_index = i
                break

        if food_eaten_index != -1:
            food_eaten = self.food_positions[food_eaten_index]
            if food_eaten[2] == 'poison':
                return False
            else:
                self.score += 1
                self.eat_sound.play() # Play eat sound
                
                # Increase eat sound volume
                current_eat_sound_volume = self.eat_sound.get_volume()
                new_eat_sound_volume = min(MAX_MUSIC_VOLUME, current_eat_sound_volume + MUSIC_VOLUME_INCREMENT_PER_FRUIT)
                self.eat_sound.set_volume(new_eat_sound_volume)

                self.food_positions.pop(food_eaten_index)
                self.food_positions.append(place_food())
        else:
            self.snake_pos.pop()
        return True

    def draw(self, screen):
        screen.fill(WHITE)

        for x in range(0, GAME_AREA_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, GAME_AREA_HEIGHT))
        for y in range(0, GAME_AREA_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, LIGHT_GRAY, (0, y), (GAME_AREA_WIDTH, y))

        for food_data in self.food_positions:
            food_pos = food_data[:2]
            food_type = food_data[2]
            color = RED if food_type == 'regular' else BLACK
            pygame.draw.circle(screen, color, (food_pos[0] + GRID_SIZE // 2, food_pos[1] + GRID_SIZE // 2), GRID_SIZE // 2)

        for i, segment in enumerate(self.snake_pos):
            if i == 0:
                pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))
            else:
                pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))