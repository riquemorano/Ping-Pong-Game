import pygame

amarelo = (255, 255, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)

velocidade = 1
x_tela = 1000
y_tela = 500



class Bola:

    def __init__(self):
        self.ponto_esquerda = 0
        self.ponto_direita = 0
        self.raio = 10
        self.x = x_tela/2
        self.y = y_tela/2
        self.vel_x = velocidade
        self.vel_y = velocidade

    def pinta_bola(self):
        tela.fill(preto)
        pygame.draw.circle(
            tela, branco, (int(self.x), int(self.y)), self.raio, 0)

    def colide_tela(self):

        if self.x + self.raio > x_tela:
            self.vel_x = -velocidade

        if self.x - self.raio < 0:
            self.vel_x = velocidade

        if self.y + self.raio > y_tela:
            self.vel_y = -velocidade

        if self.y - self.raio < 0:
            self.vel_y = velocidade

    def colide_raquete(self, raquete):
        if raquete.x < x_tela/2:
            if self.x - self.raio < raquete.x + raquete.largura:
                if self.y - self.raio < raquete.y + raquete.altura:
                    if self.y + self.raio > raquete.y:
                        self.vel_x = velocidade

        else:
            if self.x + self.raio > raquete.x + raquete.largura - 10:
                if self.y - self.raio < raquete.y + raquete.altura:
                    if self.y + self.raio > raquete.y:
                        self.vel_x = -velocidade

        # Colisão com a Tela
    def movimenta_bola(self):
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y
    
    def marca_pontos(self):
        
        if self.x >= x_tela - 10:
            self.ponto_esquerda = self.ponto_esquerda + 1
            
        elif self.x <= 10:
            self.ponto_direita = self.ponto_direita + 1
            

class Raquete:

    def __init__(self, x):

        self.x = x
        self.y = y_tela/2
        self.largura = 10
        self.altura = 90
        self.vel_y = 0

    def pinta_raquete(self):
        pygame.draw.rect(tela, branco, (int(self.x), int(
            self.y), int(self.largura), int(self.altura)), 5)

    def colide_tela(self):

        if self.y + 90 > y_tela:
            self.y = y_tela - 90

        elif self.y < 0:
            self.y = 0

    def movimenta_raquete_auto(self):
        self.y = self.bola.y - (self.y/4)

    def movimenta_raquete(self, eventos):
        self.y = self.y + self.vel_y
        if self.x < x_tela/2:
            for e in eventos:

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_w:
                        self.vel_y = -velocidade

                    elif e.key == pygame.K_s:
                        self.vel_y = velocidade

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_w:
                        self.vel_y = 0
                    elif e.key == pygame.K_s:
                        self.vel_y = 0
        else:
            for e in eventos:

                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_DOWN:
                        self.vel_y = velocidade

                    elif e.key == pygame.K_UP:
                        self.vel_y = -velocidade

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_DOWN:
                        self.vel_y = 0
                    elif e.key == pygame.K_UP:
                        self.vel_y = 0


pygame.init()
tela = pygame.display.set_mode((x_tela, y_tela), 0)
fonte = pygame.font.SysFont('arial', 25)



if __name__ == "__main__":
    bola = Bola()

    posicao_esquerda = 10
    posicao_direita = x_tela - 20

    raquete_esquerda = Raquete(posicao_esquerda)
    raquete_direita = Raquete(posicao_direita)
    
    while True:

        # Pinta
        bola.pinta_bola()
        raquete_esquerda.pinta_raquete()
        raquete_direita.pinta_raquete()

        pygame.time.delay(3)
        pygame.display.update()

        bola.movimenta_bola()
        bola.colide_tela()

        bola.colide_raquete(raquete_direita)
        bola.colide_raquete(raquete_esquerda)

        raquete_direita.colide_tela()
        raquete_esquerda.colide_tela()

        bola.marca_pontos()
        # raquete_esquerda.movimenta_raquete_auto()
        # raquete_esquerda.movimenta_raquete_auto()

        # Eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

        raquete_esquerda.movimenta_raquete(eventos)
        raquete_direita.movimenta_raquete(eventos)

        if velocidade < 4:
            velocidade += 0.00015

        else:
            velocidade = 4
