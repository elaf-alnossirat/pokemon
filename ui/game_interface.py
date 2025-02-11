    
import pygame
import sys
import random
from models.pokemon import Pokemon

class InterfacePokemon:
    def __init__(self, largeur=1000, hauteur=600):
        pygame.init()
        self.ecran = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Pokémon Battle")
        
        # Charger les ressources
        self.background = pygame.image.load("assets/background.jpg")
        self.background = pygame.transform.scale(self.background, (largeur, hauteur))
        
        # Couleurs
        self.BLANC = (255, 255, 255)
        self.NOIR = (0, 0, 0)
        self.GRIS = (200, 200, 200)
        self.ROUGE = (255, 0, 0)
        self.VERT = (0, 255, 0)
        self.BLEU = (0, 0, 255)
        
        # Polices
        self.police_titre = pygame.font.Font(None, 50)
        self.police_texte = pygame.font.Font(None, 30)
        
    def menu_principal(self):
        clock = pygame.time.Clock()
        animation_alpha = 0  # Animation de fondu
        background_surface = self.background.copy()
        background_surface.set_alpha(animation_alpha)
        
        boutons = [
            ("Démarrer le jeu", (600, 200)),
            ("Ajouter un Pokémon", (600, 300)),
            ("Afficher le Pokédex", (600, 400))
        ]
        
        while True:
            self.ecran.fill(self.BLANC)
            background_surface.set_alpha(animation_alpha)
            self.ecran.blit(background_surface, (0, 0))
            animation_alpha = min(animation_alpha + 5, 255)
            
            titre = self.police_titre.render("Pokémon Battle", True, self.NOIR)
            self.ecran.blit(titre, (250, 50))
            
            for texte, pos in boutons:
                x, y = pos
                bouton_rect = pygame.Rect(x, y, 300, 70)
                couleur = self.GRIS
                
                # Vérifier la position de la souris
                if bouton_rect.collidepoint(pygame.mouse.get_pos()):
                    couleur = self.BLEU
                
                pygame.draw.rect(self.ecran, couleur, bouton_rect, border_radius=10)
                texte_surface = self.police_texte.render(texte, True, self.NOIR)
                # Calculate the center of the button
                text_rect = texte_surface.get_rect(center=bouton_rect.center)
                self.ecran.blit(texte_surface, text_rect)

                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, (texte, pos) in enumerate(boutons):
                        if pygame.Rect(pos[0], pos[1], 200, 50).collidepoint(event.pos):
                            return i  # Retourne l'index de l'option sélectionnée
            
            pygame.display.flip()
            clock.tick(30)
    
    def lancer(self):
        while True:
            choix = self.menu_principal()
            if choix == 0:
                print("Démarrage du jeu...")
            elif choix == 1:
                print("Ajout d'un Pokémon...")
            elif choix == 2:
                print("Affichage du Pokédex...")

if __name__ == "__main__":
    jeu = InterfacePokemon()
    jeu.lancer()
