import pygame
from particles import Particle
from random import uniform
pygame.init()
RUN = True
SCREEN = pygame.display.set_mode((200,200))
BLACK = (0,0,0)
def main():
    global RUN,SCREEN
    TIME = pygame.time.Clock()
    particle_list = []
    for i in range(50):
        particle_list.append(Particle(1,1,uniform(0,0.5)))
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        TIME.tick(60)
        SCREEN.fill(BLACK)
        for particle in particle_list:
            particle.Draw(SCREEN)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()