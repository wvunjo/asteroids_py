# Asteroids Game

A classic Asteroids-style arcade game built with Python and Pygame. Navigate your ship through an asteroid field, shoot incoming asteroids, and try to survive as long as possible!

## Overview

This is a real-time space shooter game where you control a triangular ship that can rotate and move through space. Asteroids continuously spawn from the edges of the screen and move toward the center. Your goal is to destroy them by shooting while avoiding collisions. When you hit an asteroid, it splits into smaller pieces. If your ship collides with an asteroid, the game ends.

## Requirements

- **Python**: 3.13 or higher
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (recommended) or pip
- **Dependencies**:
  - `pygame==2.6.1`

## Installation

### Using uv (Recommended)

If you have `uv` installed, the dependencies will be automatically managed:

```bash
# Clone or download the repository
git clone <repository-url>
cd asteroids_py/asteroids_py

# Run the game (uv will handle dependencies automatically)
uv run main.py
```

### Using pip

If you prefer using pip:

```bash
# Clone or download the repository
git clone <repository-url>
cd asteroids_py/asteroids_py

# Install dependencies
pip install -r requirements.txt
# Or install directly:
pip install pygame==2.6.1

# Run the game
python main.py
```

## Running the Game

### With uv (Recommended)

```bash
uv run main.py
```

### With Python directly

```bash
python main.py
```

## Controls

- **W** / **S**: Move forward / backward
- **A** / **D**: Rotate left / right
- **SPACE**: Shoot
- **Close Window**: Exit the game

## What to Expect

When you run the game:

1. A black game window will open (1280x720 pixels)
2. Your white triangular ship will appear in the center of the screen
3. Asteroids will start spawning from the edges of the screen every 0.8 seconds
4. Asteroids move at varying speeds and angles toward the center
5. You can shoot asteroids - when hit, they split into smaller pieces
6. If your ship collides with an asteroid, you'll see "Game over!" and the game will exit
7. The game runs at 60 FPS for smooth gameplay

### Game Features

- **Asteroid Spawning**: Asteroids continuously spawn from random edges of the screen
- **Asteroid Splitting**: When shot, large asteroids split into smaller ones (down to a minimum size)
- **Collision Detection**: Circle-based collision detection for ship-asteroid and shot-asteroid interactions
- **Shooting Cooldown**: There's a 0.3 second cooldown between shots to prevent spam
- **Logging**: The game logs state and events to JSONL files (`game_state.jsonl` and `game_events.jsonl`) for the first 16 seconds of gameplay

## Project Structure

- `main.py` - Main game loop and entry point
- `player.py` - Player ship class with movement and shooting mechanics
- `asteroid.py` - Asteroid class with splitting behavior
- `asteroidfield.py` - Manages asteroid spawning from screen edges
- `shot.py` - Projectile class for player shots
- `circleshape.py` - Base class for circular game objects with collision detection
- `constants.py` - Game configuration constants (screen size, speeds, etc.)
- `logger.py` - Game state and event logging system
- `pyproject.toml` - Project configuration and dependencies

## Game Configuration

You can modify game parameters in `constants.py`:
- Screen dimensions
- Player speed and turn rate
- Asteroid spawn rate and sizes
- Shot speed and cooldown
- And more...

## Notes

- The game uses Pygame's sprite system for efficient rendering and collision detection
- Game state logging is automatically enabled and writes to JSONL files
- The game window must be closed manually to exit (or collide with an asteroid)
