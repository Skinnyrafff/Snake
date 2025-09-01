import pygame
import pygame_menu
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, GAME_AREA_WIDTH, GAME_AREA_HEIGHT, BLACK, WHITE, RED, LIGHT_SILVER, INITIAL_MUSIC_VOLUME, INITIAL_SFX_VOLUME, TOTAL_CELLS
from utils import display_text, load_unlocked_difficulty, save_unlocked_difficulty
from game import SnakeGame

def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init() # Initialize mixer

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("SNAKE FLAKKO")
    clock = pygame.time.Clock()

    # Load sounds
    pygame.mixer.music.load("assets/sounds/background_music.mp3")
    eat_sound = pygame.mixer.Sound("assets/sounds/eat_sound.mp3")
    game_over_sound = pygame.mixer.Sound("assets/sounds/game_over_sound.mp3")

    # Set initial volumes
    pygame.mixer.music.set_volume(INITIAL_MUSIC_VOLUME)
    eat_sound.set_volume(INITIAL_SFX_VOLUME)
    game_over_sound.set_volume(INITIAL_SFX_VOLUME)

    # Play background music
    pygame.mixer.music.play(-1, 2.0) # -1 means loop indefinitely, start 2 seconds in

    game = SnakeGame(eat_sound) # Pass eat_sound to game

    # Game state variables
    game_running = False
    game_over_score = 0

    # Difficulty unlocking
    unlocked_difficulty = load_unlocked_difficulty()
    difficulty_levels = ["Fácil", "Medio", "Difícil"]

    def update_menu_buttons():
        # Get current unlocked level index
        unlocked_index = difficulty_levels.index(unlocked_difficulty)

        # Enable/disable buttons based on unlocked level
        for i, level in enumerate(difficulty_levels):
            button = menu.get_widget(level) # Get button by its title (which is the level name)
            if i <= unlocked_index:
                button.enable()
            else:
                button.disable()

    def start_the_game(difficulty):
        nonlocal game_running
        game.reset_game(difficulty)
        game_running = True
        menu.disable()
        pygame.mixer.music.set_volume(INITIAL_MUSIC_VOLUME) # Reset music volume on new game

    def restart_game_callback():
        nonlocal game_running
        game.reset_game(game.current_difficulty_str)
        game_running = True
        game_over_menu.disable()
        game_won_menu.disable()
        pygame.mixer.music.set_volume(INITIAL_MUSIC_VOLUME) # Reset music volume on restart

    def choose_level_callback():
        nonlocal game_running
        game_running = False # Exit game loop
        menu.enable()
        game_over_menu.disable()
        game_won_menu.disable()
        update_menu_buttons() # Update button states when returning to menu
        pygame.mixer.music.set_volume(INITIAL_MUSIC_VOLUME) # Reset music volume on choosing level

    def exit_game_callback():
        nonlocal running
        running = False
        game_over_menu.disable()
        game_won_menu.disable()

    def set_music_volume(value, **kwargs):
        pygame.mixer.music.set_volume(value / 100.0)

    def set_sfx_volume(value, **kwargs):
        eat_sound.set_volume(value / 100.0)
        game_over_sound.set_volume(value / 100.0)

    def format_int_value(value):
        return str(int(value))

    # Main Menu
    menu = pygame_menu.Menu('SNAKE FLAKKO', WINDOW_WIDTH, WINDOW_HEIGHT,
                           theme=pygame_menu.themes.THEME_BLUE)

    
    menu.add.button('Fácil', lambda: start_the_game('Fácil'), _id='Fácil')
    menu.add.button('Medio', lambda: start_the_game('Medio'), _id='Medio')
    menu.add.button('Difícil', lambda: start_the_game('Difícil'), _id='Difícil')
    menu.add.range_slider('Música', default=int(INITIAL_MUSIC_VOLUME * 100), range_values=(0, 100), increment=1, onchange=set_music_volume, value_format=format_int_value)
    menu.add.range_slider('Efectos', default=int(INITIAL_SFX_VOLUME * 100), range_values=(0, 100), increment=1, onchange=set_sfx_volume, value_format=format_int_value)
    menu.add.button('Salir', pygame_menu.events.EXIT)

    # Initial update of menu buttons
    update_menu_buttons()

    # Game Over Menu
    game_over_menu = pygame_menu.Menu('GAME OVER', WINDOW_WIDTH, WINDOW_HEIGHT,
                                      theme=pygame_menu.themes.THEME_BLUE)
    
    score_label_game_over = game_over_menu.add.label(f'Puntuación final: {game_over_score}', font_size=30, font_color=BLACK, background_color=None)
    game_over_menu.add.button('Reiniciar', restart_game_callback)
    game_over_menu.add.button('Elegir Nivel', choose_level_callback)
    game_over_menu.add.button('Salir', exit_game_callback)

    # Game Won Menu
    game_won_menu = pygame_menu.Menu('¡HAS GANADO!', WINDOW_WIDTH, WINDOW_HEIGHT,
                                     theme=pygame_menu.themes.THEME_BLUE)
    score_label_game_won = game_won_menu.add.label(f'Puntuación final: {game_over_score}', font_size=30, font_color=BLACK, background_color=None)
    game_won_menu.add.button('Reiniciar', restart_game_callback)
    game_won_menu.add.button('Elegir Nivel', choose_level_callback)
    game_won_menu.add.button('Salir', exit_game_callback)

    game_surface = pygame.Surface((GAME_AREA_WIDTH, GAME_AREA_HEIGHT))
    game_area_x = (WINDOW_WIDTH - GAME_AREA_WIDTH) // 2
    game_area_y = (WINDOW_HEIGHT - GAME_AREA_HEIGHT) // 2
    border_width = 5

    running = True
    while running:
        # Main Menu Loop
        if menu.is_enabled():
            menu.mainloop(screen)

        # Game Loop
        if game_running:
            while game_running:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.QUIT:
                        running = False
                        game_running = False
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_running = False # Exit game loop to go back to main menu
                            menu.enable()

                        elif event.key == pygame.K_UP and game.snake_direction != 'DOWN':
                            game.snake_direction = 'UP'
                        elif event.key == pygame.K_DOWN and game.snake_direction != 'UP':
                            game.snake_direction = 'DOWN'
                        elif event.key == pygame.K_LEFT and game.snake_direction != 'RIGHT':
                            game.snake_direction = 'LEFT'
                        elif event.key == pygame.K_RIGHT and game.snake_direction != 'LEFT':
                            game.snake_direction = 'RIGHT'

                screen.fill(LIGHT_SILVER)

                # Draw game elements
                if game.current_difficulty_str != "Fácil":
                    pygame.draw.rect(screen, BLACK, 
                                     (game_area_x - border_width, game_area_y - border_width,
                                      GAME_AREA_WIDTH + border_width * 2, GAME_AREA_HEIGHT + border_width * 2), border_width)

                game_status = game.update() # Get game status
                if game_status == False: # Game Over (Loss)
                    game_running = False # Exit game loop
                    game_over_score = game.score # Store final score
                    score_label_game_over.set_title(f'Puntuación final: {game_over_score}') # Update score in menu
                    game_over_menu.enable() # Enable game over menu
                    game_over_sound.play() # Play game over sound
                    pygame.time.wait(2000) # Delay for game over sound
                elif game_status == "win": # Game Over (Win)
                    game_running = False # Exit game loop
                    game_over_score = game.score # Store final score
                    score_label_game_won.set_title(f'Puntuación final: {game_over_score}') # Update score in menu
                    game_won_menu.enable() # Enable game won menu
                    # No sound for win yet, can add later
                    pygame.time.wait(2000) # Delay for win screen
                    
                game.draw(game_surface)
                screen.blit(game_surface, (game_area_x, game_area_y))

                display_text(screen, f"Puntuación: {game.score}", 25, WINDOW_WIDTH // 2, 50, BLACK)

                pygame.display.flip()
                clock.tick(game.current_speed)

        # Game Over Menu Loop
        if game_over_menu.is_enabled():
            try:
                game_over_menu.mainloop(screen)
            except Exception as e:
                print(f"Error in game_over_menu.mainloop: {e}")
                running = False # Exit the main loop to prevent further crashes

        # Game Won Menu Loop
        if game_won_menu.is_enabled():
            try:
                game_won_menu.mainloop(screen)
            except Exception as e:
                print(f"Error in game_won_menu.mainloop: {e}")
                running = False # Exit the main loop to prevent further crashes

    pygame.quit()

if __name__ == "__main__":
    main()
