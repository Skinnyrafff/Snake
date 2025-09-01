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
LIGHT_SILVER = (230, 230, 230) # Un color de fondo suave

# Estados del juego
GAME_STATE_MENU = 0
GAME_STATE_PLAYING = 1
GAME_STATE_GAME_OVER = 2
GAME_STATE_PAUSED = 3
GAME_STATE_WON = 4

# Dificultades
DIFFICULTY_EASY = 0
DIFFICULTY_MEDIUM = 1
DIFFICULTY_HARD = 2

# Tipos de comida
FOOD_TYPE_REGULAR = 'regular'
FOOD_TYPE_POISON = 'poison'
POISON_FOOD_PROBABILITY = 0.1 # 10% de probabilidad de que la fruta sea venenosa

# Constantes de Sonido
INITIAL_MUSIC_VOLUME = 0.3 # Volumen inicial de la música (0.0 a 1.0)
INITIAL_SFX_VOLUME = 0.05 # Volumen inicial de los efectos de sonido (0.0 a 1.0)
MAX_MUSIC_VOLUME = 1.0 # Volumen máximo de la música
MUSIC_VOLUME_INCREMENT_PER_FRUIT = 0.01 # Incremento de volumen por fruta comida

# Total cells
TOTAL_CELLS = (GAME_AREA_WIDTH // GRID_SIZE) * (GAME_AREA_HEIGHT // GRID_SIZE)