# SNAKE FLAKKO

Este es un juego de Snake desarrollado con Pygame.

## Características y Mejoras Recientes:

*   **Área de Juego Centrada y con Borde:** El área de juego principal ahora está centrada en la ventana y cuenta con un borde visual claro. Este borde se muestra solo en las dificultades "Medio" y "Difícil".
*   **Jugabilidad de Pantalla Completa:** Se ha eliminado el muro interno que dividía el nivel, permitiendo que toda el área de juego de 400x400 píxeles sea un espacio único y completamente jugable.
*   **Ajustes de Velocidad por Dificultad:**
    *   **Fácil:** Velocidad 6
    *   **Medio:** Velocidad 8
    *   **Difícil:** Velocidad 10
*   **Sistema de Menús Mejorado:**
    *   Integración de la librería `pygame-menu` para un menú principal más atractivo y funcional.
    *   Nuevo menú de "Game Over" con opciones claras para "Reiniciar", "Elegir Nivel" o "Salir del juego".
    *   Funcionalidad de la tecla `ESC`: Permite pausar el juego y volver al menú principal, o regresar al menú desde la pantalla de "Game Over".
*   **Generación de Comida Inteligente:** La comida ahora aparece únicamente en áreas accesibles y jugables del mapa.
*   **Colisión con la Propia Serpiente:** La serpiente pierde si choca consigo misma en todas las dificultades.
*   **Nombre de la Aplicación:** El título de la ventana del juego ha sido cambiado a "SNAKE FLAKKO".

## Cómo Jugar:

1.  Asegúrate de tener Python instalado.
2.  Instala Pygame y Pygame-Menu:
    ```bash
    pip install pygame pygame-menu
    ```
3.  Ejecuta el juego:
    ```bash
    python main.py
    ```

¡Disfruta de SNAKE FLAKKO!