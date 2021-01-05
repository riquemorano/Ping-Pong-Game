import pygame
import time

class Bola:

    def __init__(self):
        self.ponto_esquerda = 0
        self.ponto_direita = 0
        self.raio = 10
        self.x = x_meio
        self.y = y_meio
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

    def movimenta_bola(self):
        
        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y
        
    def para_bola(self):
           
        self.x = x_meio
        self.y = y_meio
        
        pygame.time.wait(1000)
        

    def marca_pontos(self):

        if self.x >= x_tela - 10:
            self.ponto_esquerda = self.ponto_esquerda + 1
            self.para_bola()
            self.vel_x = velocidade

        elif self.x <= 10:
            self.ponto_direita = self.ponto_direita + 1
            self.para_bola()
            self.vel_x = -velocidade
                        

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

    def movimenta_raquete_auto(self, bola):
        
        self.y = bola.y - (self.y/4)

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

if __name__ == "__main__":

# Cores
    amarelo = (255, 255, 0)
    preto = (0, 0, 0)
    branco = (255, 255, 255)

# Tela
    x_tela = 1000
    y_tela = 500
    x_meio = x_tela/2
    y_meio = y_tela/2

# Velocidade
    velocidade = 1

# Posições
    posicao_esquerda = 10
    posicao_direita = x_tela - 20

# Iniciando Pygame e Objetos
    pygame.init()

    tela = pygame.display.set_mode((x_tela, y_tela), 0)
    fonte = pygame.font.SysFont("arial", 28, True, False)
    tempo = pygame.time.get_ticks()
    
    bola = Bola()

    raquete_esquerda = Raquete(posicao_esquerda)
    raquete_direita = Raquete(posicao_direita)
    
    relogio = pygame.time.Clock()


# Inicia o Jogo

    while True:
    
    #Configura Tempo
    
        tempo_regressivo = pygame.time.get_ticks()
        tempo_segundos = 90
        segundos = int( (tempo_regressivo)/1000 )

        print(f"{segundos} segundos")
        
        texto_segundos =str(tempo_segundos - segundos)
        relogio.tick()
    
    # Configura Velocidade do Jogo
        pygame.time.delay(1)

    # Placar
        texto_placar = f'P1:{bola.ponto_esquerda}        T:{texto_segundos:0>2}       P2:{bola.ponto_direita}'
        
        img_placar = fonte.render(texto_placar, True, (amarelo))

        x_placar = img_placar.get_width()
        
        bola.marca_pontos()
        pygame.display.update()

    # Desenha Objetos
        bola.pinta_bola()
        
        raquete_esquerda.pinta_raquete()
        raquete_direita.pinta_raquete()
        
        tela.blit(img_placar, ((int(x_meio - (x_placar/2))), 10))

    # Movimentos e Colisões
        bola.movimenta_bola()
        bola.colide_tela()

        bola.colide_raquete(raquete_direita)
        bola.colide_raquete(raquete_esquerda)

        raquete_direita.colide_tela()
        raquete_esquerda.colide_tela()

    #Atualiza a Tela
        pygame.display.update()

    # Movimenta Raquete Automáticamente
        #raquete_esquerda.movimenta_raquete_auto(bola)
        #raquete_direita.movimenta_raquete_auto(bola)

    # Eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

        raquete_esquerda.movimenta_raquete(eventos)
        raquete_direita.movimenta_raquete(eventos)

        if velocidade < 4:
            velocidade += 0.00005

        else:
            velocidade = 4
        
        if texto_segundos == "0":
            exit()