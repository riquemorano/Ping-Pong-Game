import pygame

amarelo = (255, 255, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

velocidade = 1

x_tela = 1000
y_tela = 500

tela = pygame.display.set_mode((x_tela, y_tela), 0)

class Bola:

    def __init__(self):
        
        self.raio = 10
        self.x = x_tela/2
        self.y = y_tela/2
        self.vel_x = velocidade
        self.vel_y = velocidade

    def pinta_bola(self):
        tela.fill(preto)
        pygame.draw.circle(
            tela, branco, (int(self.x), int(self.y)), self.raio, 0)

    def colide_bola(self):

        if self.x + self.raio > x_tela:
            self.vel_x = -velocidade

        if self.x - self.raio < 0:
            self.vel_x = velocidade

        if self.y + self.raio > y_tela:
            self.vel_y = -velocidade

        if self.y - self.raio < 0:
            self.vel_y = velocidade

    
    def movimenta_bola(self):
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y


class Raquete:
    
    def __init__(self, x, Bola):
        
        self.bola = Bola
        self.x = x
        self.y = y_tela/2
        self.largura = 10
        self.altura = 90

    def pinta_raquete(self):
        pygame.draw.rect(tela, branco, (int(self.x), int(
            self.y), int(self.largura), int(self.altura)), 5)
            

    def colide_raquete(self):
        if self.x < x_tela/2:
            if self.bola.x - self.bola.raio < self.x + self.largura:
                if self.bola.y - self.bola.raio < self.y + self.altura:
                    if self.bola.y + self.bola.raio > self.y:
                        self.bola.vel_x = velocidade

        else:
            if self.bola.x + self.bola.raio > self.x + self.largura:
                if self.bola.y - self.bola.raio < self.y + self.altura:
                    if self.bola.y + self.bola.raio > self.y:
                        self.bola.vel_x = -velocidade
                        
    def movimenta_raquete(self):
        self.y = self.bola.y - (self.y/4)

pygame.init()

bola = Bola()

raquete = Raquete(10, bola)
raquete2 = Raquete(980, bola)

while True:

    #Pinta
    bola.pinta_bola()
    raquete.pinta_raquete()
    raquete2.pinta_raquete()
    pygame.display.update()
    
    bola.movimenta_bola()
    bola.colide_bola()
    raquete.colide_raquete()
    raquete2.colide_raquete()
    raquete.movimenta_raquete()
    raquete2.movimenta_raquete()
    

    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
