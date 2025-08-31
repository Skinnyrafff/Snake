# constants.py

# --- Constantes del juego ---
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600 # Tamaño de la ventana
GAME_AREA_WIDTH, GAME_AREA_HEIGHT = 400, 400 # Área de juego
GRID_SIZE = 20

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0) # Un verde más oscuro para la cabeza
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200) # Color para las líneas de la cuadrícula

# Estados del juego
GAME_STATE_MENU = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2
GAME_STATE_PAUSED = 3

# Dificultades
DIFFICULTY_EASY = 0
DIFFICULTY_MEDIUM = 1
DIFFICULTY_HARD = 2

# Tipos de comida
FOOD_TYPE_REGULAR = 'regular'
FOOD_TYPE_POISON = 'poison'
POISON_FOOD_PROBABILITY = 0.1 # 10% de probabilidad de que la fruta sea venenosa