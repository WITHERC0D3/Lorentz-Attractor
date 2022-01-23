import pygame
from random import uniform,randint

#Lorentz variables
sigma = 10
beta = 8/3
rho = 28
WHITE = (255,255,255)
class Particle():
    def __init__(self,xpos,ypos,zpos):
        self.pos = pygame.Vector3(xpos,ypos,zpos)
        self.dt = 0.01
        self.dx,self.dy,self.dz = 0,0,0
        #self.velocity = pygame.Vector2(uniform(-1,1),uniform(-1,1))
        self.radius = 2
        self.scale= 2.55
       # self.lifeTime = randint(50,100)
    
    def Draw(self,surface):
        pygame.draw.circle(surface,(255,255,255),(self.scale*(self.pos.x)+100,self.scale*((-1)*self.pos.z)+150),self.radius)
        self.dx = sigma*(self.pos.y-self.pos.x)*self.dt
        self.dy = (self.pos.x*(rho-self.pos.z)-self.pos.y)*self.dt 
        self.dz = (self.pos.x*self.pos.y-beta*self.pos.z)*self.dt
        self.pos.x+=self.dx
        self.pos.y+=self.dy
        self.pos.z+=self.dz
