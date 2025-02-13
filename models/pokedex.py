import json
import os

class Pokedex:
    def __init__(self, fichier='data/pokedex.json'):
        self.fichier = fichier
        self.pokemon_captures = []
        self.charger()

    def ajouter_pokemon(self, pokemon):
        # Vérifier les doublons par nom
        if not any(p.nom == pokemon.nom for p in self.pokemon_captures):
            self.pokemon_captures.append(pokemon)
            self.sauvegarder()

    def charger(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, 'r') as f:
                data = json.load(f)
                self.pokemon_captures = [
                    Pokemon.from_dict(pokemon_data) 
                    for pokemon_data in data
                ]

    def sauvegarder(self):
        with open(self.fichier, 'w') as f:
            json.dump([
                pokemon.to_dict() 
                for pokemon in self.pokemon_captures
            ], f, indent=4)

    def afficher_pokemon(self):
        for pokemon in self.pokemon_captures:
            print(f"{pokemon.nom} (Niveau {pokemon.niveau})")