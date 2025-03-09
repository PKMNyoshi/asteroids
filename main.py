# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
from constants import *
def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	background_color = pygame.Color("black")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
        			return
		screen.fill(background_color)
		print("Starting Asteroids!")
		print(f"Screen width: {SCREEN_WIDTH}")
		print(f"Screen height: {SCREEN_HEIGHT}")
		pygame.display.flip()




if __name__ == "__main__":
    main()
