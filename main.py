#this allows us to use code from
#the open-source pygame library
#throughout this file
import pygame
from constants import * ##import constants from constants.py
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init() #initialize the pygame library
    update_group = pygame.sprite.Group() #create a group to hold all sprites that need to be updated
    draw_group = pygame.sprite.Group() #create a group to hold all sprites that need to be drawn
    asteroids = pygame.sprite.Group() #create a group to hold all asteroids
    Player.containers = (update_group, draw_group) #set the containers for the player class
    Asteroid.containers = (draw_group, update_group, asteroids) #set the containers for the asteroid class
    AsteroidField.containers = (update_group,) ##the comma is important, even for only 1 element
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a window
    dt = 0
    clock = pygame.time.Clock() #create a clock object to track time
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS) #create a player object
    asteroid_field = AsteroidField() #create an asteroid field object

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #exit the game loop if the user closes the window
        screen.fill("black")

        update_group.update(dt) #update all sprites in the update group
        for drawable in draw_group:
            drawable.draw(screen) #draw all sprites in the draw group
        for asteroid in asteroids:
            if player.collision(asteroid):
                return print("Game Over!")

                    
        pygame.display.flip() #update the display, need pygame first
        clock.tick(60) #limit the frame rate to 60 FPS
        dt = clock.get_time() / 1000 #get the time since the last frame in seconds
    

if __name__ == "__main__":
    main()