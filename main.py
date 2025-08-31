import pygame
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, GAME_AREA_WIDTH, GAME_AREA_HEIGHT, BLACK, WHITE, RED, GAME_STATE_MENU, GAME_STATE_PLAYING, GAME_STATE_GAME_OVER, GAME_STATE_PAUSED, LIGHT_SILVER
from utils import display_text
from game import SnakeGame

def main():
    pygame.init()
    pygame.font.init() # Inicializar el módulo de fuentes
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Juego de la Serpiente")
    clock = pygame.time.Clock()

    # Crear una superficie para el área de juego
    game_surface = pygame.Surface((GAME_AREA_WIDTH, GAME_AREA_HEIGHT))
    game_area_x = (WINDOW_WIDTH - GAME_AREA_WIDTH) // 2
    game_area_y = (WINDOW_HEIGHT - GAME_AREA_HEIGHT) // 2
    border_width = 5 # Aumentar el grosor del borde

    game = SnakeGame() # Instancia del juego
    game_state = GAME_STATE_MENU # Empezar en el estado de menú
    menu_options = ["Fácil", "Medio", "Difícil"]
    selected_option_index = 0

    pause_menu_options = ["Reanudar", "Salir"]
    selected_pause_option_index = 0

    running = True # Este 'running' controla el bucle principal de la aplicación
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == GAME_STATE_MENU:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option_index = (selected_option_index - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_option_index = (selected_option_index + 1) % len(menu_options)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        game_state = GAME_STATE_PLAYING
                        game.reset_game(menu_options[selected_option_index])
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    game_state = GAME_STATE_PLAYING
                    game.reset_game(menu_options[selected_option_index])
            elif game_state == GAME_STATE_PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Pausar el juego
                        game_state = GAME_STATE_PAUSED
                        selected_pause_option_index = 0 # Resetear la selección del menú de pausa
                    elif event.key == pygame.K_UP and game.snake_direction != 'DOWN':
                        game.snake_direction = 'UP'
                    elif event.key == pygame.K_DOWN and game.snake_direction != 'UP':
                        game.snake_direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and game.snake_direction != 'RIGHT':
                        game.snake_direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and game.snake_direction != 'LEFT':
                        game.snake_direction = 'RIGHT'
            elif game_state == GAME_STATE_PAUSED: # Nuevo estado: Pausado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_pause_option_index = (selected_pause_option_index - 1) % len(pause_menu_options)
                    elif event.key == pygame.K_DOWN:
                        selected_pause_option_index = (selected_pause_option_index + 1) % len(pause_menu_options)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        if pause_menu_options[selected_pause_option_index] == "Reanudar":
                            game_state = GAME_STATE_PLAYING
                        elif pause_menu_options[selected_pause_option_index] == "Salir":
                            game_state = GAME_STATE_MENU
                            game.reset_game(menu_options[selected_option_index]) # Reiniciar para el menú principal
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_menu_options[selected_pause_option_index] == "Reanudar":
                        game_state = GAME_STATE_PLAYING
                    elif pause_menu_options[selected_pause_option_index] == "Salir":
                        game_state = GAME_STATE_MENU
                        game.reset_game(menu_options[selected_option_index]) # Reiniciar para el menú principal
            elif game_state == GAME_STATE_GAME_OVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: # Reiniciar
                        game_state = GAME_STATE_PLAYING
                        game.reset_game(menu_options[selected_option_index]) # Reiniciar con la última dificultad seleccionada
                    elif event.key == pygame.K_q: # Salir
                        running = False

        screen.fill(LIGHT_SILVER) # Rellenar el fondo para todos los estados

        if game_state == GAME_STATE_MENU:
            display_text(screen, "Juego de la Serpiente", 50, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 100, BLACK)
            for i, option in enumerate(menu_options):
                color = RED if i == selected_option_index else BLACK
                display_text(screen, option, 35, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30 + i * 40, color)
            display_text(screen, "Presiona ENTER o haz click para iniciar", 25, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100, BLACK)
        elif game_state == GAME_STATE_PLAYING or game_state == GAME_STATE_PAUSED or game_state == GAME_STATE_GAME_OVER:
            # Dibujar el borde del área de juego
            pygame.draw.rect(screen, BLACK, 
                             (game_area_x - border_width, game_area_y - border_width,
                              GAME_AREA_WIDTH + border_width * 2, GAME_AREA_HEIGHT + border_width * 2), border_width)

            # Actualizar y dibujar el juego en su propia superficie
            if game_state == GAME_STATE_PLAYING:
                if not game.update(): # Si update devuelve False, es Game Over
                    game_state = GAME_STATE_GAME_OVER
            
            game.draw(game_surface)
            screen.blit(game_surface, (game_area_x, game_area_y))

            # Mostrar puntuación en el área de UI
            display_text(screen, f"Puntuación: {game.score}", 25, WINDOW_WIDTH // 2, 50, BLACK)

            if game_state == GAME_STATE_PAUSED:
                # Dibujar overlay de pausa
                overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 150)) # Negro semi-transparente
                screen.blit(overlay, (0, 0))

                display_text(screen, "PAUSA", 50, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80, WHITE)
                for i, option in enumerate(pause_menu_options):
                    color = RED if i == selected_pause_option_index else WHITE
                    display_text(screen, option, 35, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20 + i * 40, color)

            if game_state == GAME_STATE_GAME_OVER:
                display_text(screen, "GAME OVER", 50, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50, RED)
                display_text(screen, f"Puntuación final: {game.score}", 30, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BLACK)
                display_text(screen, "Presiona R para reiniciar o Q para salir", 25, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50, BLACK)


        pygame.display.flip() # Actualizar la pantalla

        if game_state == GAME_STATE_PLAYING:
            clock.tick(game.current_speed) # Usar la velocidad de la dificultad
        elif game_state == GAME_STATE_GAME_OVER:
            clock.tick(10)
        elif game_state == GAME_STATE_PAUSED: # Controlar velocidad en pausa
            clock.tick(30)
        else: # GAME_STATE_MENU
            clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
