# Automated Snake Game with Advanced Pathfinding

This project offers an enhanced version of the classic Snake game, featuring sophisticated automated pathfinding to navigate the snake towards food while avoiding collisions. Implemented in Python using Pygame, this version employs a greedy best-first search algorithm and matrix representations for real-time decision making and navigation, showcasing an effective application of algorithmic strategies in game development.

## Requirements

- Python 3.x
- Pygame

To install Pygame, use pip:


## Installation and Running the Game

Download `snake.py` or clone this repository, then start the game with:


## About the Automated Pathfinding

The snake's movements are controlled by a greedy best-first search algorithm, which uses a matrix to represent the game area. This approach allows for dynamic navigation towards food, prioritizing safety and efficiency without manual player input.

### Matrix Representation

- The game grid is represented as a matrix.
- Different values within the matrix identify the snake, empty space, and food.
- The snake's body is marked with higher values to avoid collisions, with values decreasing as they move away to lessen the risk of trapping.

### Greedy Best-First Search Algorithm

- Calculates the shortest path to food using the Pythagorean theorem to determine the direct distance from each grid cell to the food.
- Chooses paths that minimize this distance, dynamically adjusting as the game progresses.

### Automated Navigation and Safety

- Avoids immediate and potential future collisions by marking the snake's body and adjacent areas with higher values.
- This strategy not only prevents running into walls or the snake itself but also aims to avoid paths that could lead to entrapment.

## Game Features

- **Automated Pathfinding**: Watch as the snake independently finds its way through the game grid to the food.
- **Dynamic Navigation**: The pathfinding algorithm updates paths based on the game's current state, ensuring the snake moves efficiently and safely.
- **Strategic Collision Avoidance**: The game logic includes mechanisms to minimize the risk of the snake colliding with itself or the game boundaries.

## Code Structure

The game is structured around several core components:
- **Pygame Initialization**: Setting up the game environment and variables.
- **Matrix Representation**: For dynamic game state management and pathfinding.
- **Main Loop**: Integrating automated navigation with event handling and rendering.

## Future Enhancements

Planned updates include more advanced pathfinding strategies, performance optimizations, and new gameplay features such as obstacles.

## Credits

Developed with Pygame, this project is an example of applying algorithmic problem-solving to game development, demonstrating the potential of mathematical and computational concepts in creating engaging gameplay experiences.
