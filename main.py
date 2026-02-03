import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	
	
	print("Starting Asteroids with pygame version:", pygame.version.ver)
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		dt = clock.tick(60) / 1000
		log_state()
		screen.fill("black")
		pygame.display.flip()
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


	

if __name__ == "__main__":
    main()
