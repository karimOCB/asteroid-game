import pygame
import sys
from constants import * 
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def run_game(screen, clock):
    dt = 0 
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                return "game_over"

            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000 

def show_game_over(screen, clock):
    font_big = pygame.font.Font(None, 74)
    font_small = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        text = font_big.render("GAME OVER", True, (255, 0, 0))
        restart_text = font_small.render("Press R to Restart", True, (255, 255, 255))
        
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40))
        
        screen.blit(text, text_rect)
        screen.blit(restart_text, restart_rect)
        pygame.display.flip()

        # Check for key press to restart
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return "restart"

        clock.tick(30)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting Asteroids!")

    while True:
        result = run_game(screen, clock)
        if result == "game_over":
            result = show_game_over(screen, clock)
            if result == "restart":
                continue
       
    


if __name__ == "__main__":
    main()
