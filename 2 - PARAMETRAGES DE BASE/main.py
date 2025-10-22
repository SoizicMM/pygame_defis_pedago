import pygame, sys
from pygame.locals import QUIT
# DEFI5bis (1/3) : calculer la durée d'execution 
import time

pygame.init()

fenetre = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Mon jeu avec Pygame')

# Initialiser les variables
# DEFI5 (1/3) : Limiter le framerate 
FPS = 60
#DEFI5 (2/3) :Limiter le framerate 
horloge = pygame.time.Clock()

while True:
    # DEFI5bis (2/3) : calculer la durée d'execution #2/3
    temps = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # DEFI5 (3/3) :Limiter le framerate # 3/3
    horloge.tick(FPS)
    # DEFI5bis (3/3) : calculer la durée d'execution #3/3
    print("Duree en (s) : ", time.time() - temps)

    ### DEFI4 changer la couleur de fond de la fenetre 
    fenetre.fill("#dc0110")
    
    pygame.display.update()