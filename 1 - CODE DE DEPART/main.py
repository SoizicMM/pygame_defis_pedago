# Les imports
import pygame, sys
from pygame.locals import QUIT

# Initialiser pygame
pygame.init()

# Création de la fenetre de jeu en pixels
fenetre = pygame.display.set_mode((400, 300))
# Titre dans la fenetre de jeu
pygame.display.set_caption('Mon jeu avec Pygame')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Mettre à jour l'affichage 
    pygame.display.update()