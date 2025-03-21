#this allows us to use code from
#the open-source pygame library
#throughout this file
import pygame
from constants import * ##import constants from constants.py



def main():
    pygame.init() #initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a window

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #exit the game loop if the user closes the window
        screen.fill("black")
        pygame.display.flip() #update the display, need pygame first




    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")











if __name__ == "__main__":
    main()