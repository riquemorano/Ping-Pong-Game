import pygame
from network import Network
from player import Bola

win = pygame.display.set_mode((1000, 500), 0)
pygame.display.set_caption("Client")

'''with open('loc.txt','r') as loc:
    x,y = loc.read().split(',')'''

bola = Bola()



def redrawWindow(win, player, player2, bola):

    win.fill((0,0,0))

    player.pinta_raquete(win)
    player2.pinta_raquete(win)
    player.colide_tela()
    player2.colide_tela()

    bola.colide_tela()
    bola.colide_raquete(player)
    bola.colide_raquete(player2)
    bola.pinta_bola(win)

    pygame.display.update()


if __name__ == "__main__":
    def main():
        run = True

        n = Network()
        p = n.getP()

        clock = pygame.time.Clock()


        while run:
            pygame.time.delay(1)
            clock.tick(60)
            pygame.time.delay(1)
            p2 = n.send(p)

            eventos = pygame.event.get()
            for e in eventos:
                print(e)
                if e.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            bola.movimenta_bola()
            p.movimenta_raquete()

            redrawWindow(win, p, p2,bola)

            with open('loc.txt','w') as loc:
                loc.write(f'{bola.x},{bola.y}')


    main()