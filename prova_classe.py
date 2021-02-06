import pygame
from pygame import *
from pygame import event

pygame.init()

LARGHEZZA = 250
ALTEZZA = 200
SCHERMO = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption ("Gioco del 15")
tempo = pygame.time.Clock()
FPS = 60        # Questa variabile definirà quanti frame aggiorneremo al secondo.

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
ROSSO = (255, 0, 0)
VERDE = (0, 255, 0)
BLU = (0, 0, 255)
GIALLO = (255, 255, 0)

SCHERMO.fill(GIALLO)

fnt = pygame.font.SysFont("Times New Roman", 32)

riquadro = pygame.draw.rect(SCHERMO, ROSSO, (48, 48, 104, 104), 4)

def evento_uscita():
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

def muovi_tasto():
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = evento.pos
            if tasto3.collidepoint(click):
                tasto3.
                pass

            r1=pygame.Rect()
            r1.tasto()
            #s=pygame.Surface((w,l))
            #s.fill(RED)
            r1=r1.move(evento.pos)


class Tasto():

    def __init__(self, coord_x, coord_y, num):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.num = num

    def tasto(self):
        self.aspetto = pygame.Surface((48, 48))
        self.aspetto.fill(BLU)
        self.oggetto = self.aspetto.get_rect()
        self.oggetto.topleft = (self.coord_x, self.coord_y)
        SCHERMO.blit(self.aspetto, self.oggetto)
        self.testo_aspetto = fnt.render(self.num, True, (GIALLO))
        self.testo_oggetto = self.testo_aspetto.get_rect()
        self.testo_oggetto.center = (self.coord_x+25, self.coord_y+25)
        SCHERMO.blit(self.testo_aspetto, self.testo_oggetto)
        self.riquadro_tasto = pygame.draw.rect(SCHERMO, GIALLO, (self.coord_x, self.coord_y, 50, 50), 1)

while True:
    x = 50
    y = 50
    tempo.tick(FPS)
    evento_uscita()
    tasto1 = Tasto(x, y, "1")
    tasto1.tasto()
    tasto2 = Tasto(x+50, y, "2")
    tasto2.tasto()
    tasto3 = Tasto(x, y+50, "3")
    tasto3.tasto()
    muovi_tasto()
    pygame.display.flip()