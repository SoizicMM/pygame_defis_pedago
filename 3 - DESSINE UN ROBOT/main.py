import pygame, sys
from pygame.locals import QUIT
# calculer la durée d'execution #1/3
import time

pygame.init()

#initialisation des variables
fenetre = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Mon jeu avec Pygame')
FPS = 60
horloge = pygame.time.Clock()


#Les fonctions 
def dessiner():
    ### changer la couleur de fond de la fenetre 
    fenetre.fill("#9EF9CE")
    # Rectangle
    pygame.draw.rect(fenetre, "#F9DF9E", (50,10,200,250))
    # Cercle
    pygame.draw.circle(fenetre, "#9EF9F5", (200,60), 40, 4)
    pygame.draw.circle(fenetre, "#9EF9F5", (100,60), 40)  
    # Ligne
    pygame.draw.line(fenetre, "#A70024", (150, 120), (150,150), 4)
    # Ellipse
    pygame.draw.ellipse(fenetre, "#EB9EF9", (60,170,180,80))
    # Afficher les modifications
    pygame.display.update()

        
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        dessiner()
        horloge.tick(FPS)

