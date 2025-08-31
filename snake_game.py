import pygame

# --- Constantes del juego ---
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_SPEED = 10

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Juego de la Serpiente")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK) # Rellenar la pantalla de negro
        pygame.display.flip() # Actualizar la pantalla

        clock.tick(SNAKE_SPEED) # Controlar la velocidad del juego

    pygame.quit()

if __name__ == "__main__":
    main()
