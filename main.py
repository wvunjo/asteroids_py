import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updatable  = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	print("Starting Asteroids with pygame version:", pygame.version.ver)
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

	
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		dt = clock.tick(60) / 1000
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		log_state()

		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		updatable.update(dt)

		for asteroid in asteroids:
			if player.collide_with(asteroid):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
				return
		
	
		


	

if __name__ == "__main__":
    main()
