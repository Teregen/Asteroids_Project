#this allows us to use code from
#the open-source pygame library
#throughout this file
import pygame
from constants import * ##import constants from constants.py
from circleshape import CircleShape
from player import Player


def main():
    pygame.init() #initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a window
    dt = 0
    clock = pygame.time.Clock() #create a clock object to track time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS) #create a player object

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #exit the game loop if the user closes the window
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip() #update the display, need pygame first
        clock.tick(60) #limit the frame rate to 60 FPS
        dt = clock.get_time() / 1000 #get the time since the last frame in seconds
    

if __name__ == "__main__":
    main()