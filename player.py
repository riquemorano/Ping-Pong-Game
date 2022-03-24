import pygame
class Bola():
    def __init__(self, raio = 10,x = 500,y = 250):
        self.raio = raio
        self.x = x
        self.y = y
        self.vel_x = 4
        self.vel_y = 4
        self.desenho = ((self.x,self.y),self.raio,0)

    def pinta_bola(self,win):
        pygame.draw.circle(win, (255,255,255), (self.x,self.y),10,0)

    def colide_tela(self):

        if self.x + self.raio > 1000:
            self.vel_x = -self.vel_x

        if self.x - self.raio < 0:
            self.vel_x = -self.vel_x

        if self.y + self.raio > 500:
            self.vel_y = -self.vel_y

        if self.y - self.raio < 0:
            self.vel_y = -self.vel_y

    def movimenta_bola(self):

        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y

    def colide_raquete(self, raquete):

        if raquete.x < 100 / 2:
            if self.x - self.raio < raquete.x + raquete.largura:
                if self.y - self.raio < raquete.y + raquete.altura:
                    if self.y + self.raio > raquete.y:
                        self.vel_x = -self.vel_x

        else:
            if self.x + self.raio > raquete.x + raquete.largura - 10:
                if self.y - self.raio < raquete.y + raquete.altura:
                    if self.y + self.raio > raquete.y:
                        self.vel_x = -self.vel_x

class Player():

    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.desenho = (x, y, largura, altura)
        self.vel_y = 5

    def pinta_raquete(self,win):
        pygame.draw.rect(win, (255, 255, 255), self.desenho, 5)

    def colide_tela(self):

        if self.y + 90 > 500:
            self.y = 500 - 90

        elif self.y < 0:
            self.y = 0

    def movimenta_raquete(self):


        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= self.vel_y

        if keys[pygame.K_DOWN]:
            self.y += self.vel_y

        self.update()

    def update(self):
        self.desenho = (self.x, self.y, self.largura, self.altura)