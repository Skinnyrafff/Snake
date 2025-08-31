# main.py
import pygame
from constants import WIDTH, HEIGHT, BLACK, WHITE, SNAKE_SPEED, GAME_STATE_MENU, GAME_STATE_PLAYING, GAME_STATE_GAME_OVER
from utils import display_text
from game import SnakeGame

def main():
    pygame.init()
    pygame.font.init() # Inicializar el módulo de fuentes
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de la Serpiente")
    clock = pygame.time.Clock()

    game = SnakeGame() # Instancia del juego
    game_state = GAME_STATE_MENU # Empezar en el estado de menú

    running = True # Este 'running' controla el bucle principal de la aplicación
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == GAME_STATE_MENU:
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE): # Iniciar con Enter o Espacio
                    game_state = GAME_STATE_PLAYING
                    game.reset_game() # Reiniciar variables del juego al empezar
                elif event.type == pygame.MOUSEBUTTONDOWN: # Iniciar con click del ratón
                    game_state = GAME_STATE_PLAYING
                    game.reset_game()
            elif game_state == GAME_STATE_PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and game.snake_direction != 'DOWN':
                        game.snake_direction = 'UP'
                    if event.key == pygame.K_DOWN and game.snake_direction != 'UP':
                        game.snake_direction = 'DOWN'
                    if event.key == pygame.K_LEFT and game.snake_direction != 'RIGHT':
                        game.snake_direction = 'LEFT'
                    if event.key == pygame.K_RIGHT and game.snake_direction != 'LEFT':
                        game.snake_direction = 'RIGHT'
            elif game_state == GAME_STATE_GAME_OVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: # Reiniciar
                        game_state = GAME_STATE_PLAYING
                        game.reset_game()
                    elif event.key == pygame.K_q: # Salir
                        running = False

        screen.fill(WHITE) # Rellenar el fondo para todos los estados

        if game_state == GAME_STATE_MENU:
            display_text(screen, "Juego de la Serpiente", 50, WIDTH // 2, HEIGHT // 2 - 50, BLACK)
            display_text(screen, "Presiona ENTER, ESPACIO o haz click para iniciar", 25, WIDTH // 2, HEIGHT // 2 + 20, BLACK)
        elif game_state == GAME_STATE_PLAYING:
            # Actualizar y dibujar el juego
            if not game.update(): # Si update devuelve False, es Game Over
                game_state = GAME_STATE_GAME_OVER
            game.draw(screen)

            # Mostrar puntuación
            display_text(screen, f"Puntuación: {game.score}", 20, 70, 20, BLACK)
            clock.tick(SNAKE_SPEED) # Controlar la velocidad del juego solo en PLAYING

        elif game_state == GAME_STATE_GAME_OVER:
            display_text(screen, "GAME OVER", 50, WIDTH // 2, HEIGHT // 2 - 50, RED)
            display_text(screen, f"Puntuación final: {game.score}", 30, WIDTH // 2, HEIGHT // 2, BLACK)
            display_text(screen, "Presiona R para reiniciar o Q para salir", 25, WIDTH // 2, HEIGHT // 2 + 50, BLACK)
            clock.tick(10) # Controlar la velocidad de la pantalla de Game Over (más lenta)

    pygame.quit()

if __name__ == "__main__":
    main()
