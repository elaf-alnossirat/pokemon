import pygame
from utils.json_manager import JSONManager
from models.pokemon import Pokemon
from ui.game_interface import InterfacePokemon

class JeuPokemon:
    def __init__(self):
        pygame.init()
        self.json_manager = JSONManager()
        self.interface = InterfacePokemon()
        self.pokemon_disponibles = self.charger_pokemon()

    def charger_pokemon(self):
        return self.json_manager.charger_pokemon()

    def ajouter_nouveau_pokemon(self, nom, type_pokemon, pv, attaque, defense):
        nouveau_pokemon = Pokemon(nom, type_pokemon, pv, attaque, defense)
        self.json_manager.ajouter_pokemon(nouveau_pokemon)
        self.pokemon_disponibles.append(nouveau_pokemon)

    def lancer_jeu(self):
        while True:  # ✅ Maintenant c'est dans la méthode
            action = self.interface.menu_principal()
            print(f"Action choisie : {action}")

            if action == "combat":
                self.interface.lancer_combat(self.pokemon_disponibles)

            elif action == "ajouter_pokemon":
                # Interface pour ajouter un nouveau Pokémon
                pass

            elif action == "pokedex":
                self.interface.afficher_pokedex()

            elif action == "quitter":
                break

def main():
    jeu = JeuPokemon()
    jeu.lancer_jeu()

if __name__ == "__main__":
    main()
