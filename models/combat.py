import random
from models.pokemon import Pokemon
from ui.game_interface import InterfacePokemon
import json

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def afficher_statut(self):
        print(f"{self.pokemon1.nom} (PV: {self.pokemon1.pv_actuels}/{self.pokemon1.pv_max}) vs {self.pokemon2.nom} (PV: {self.pokemon2.pv_actuels}/{self.pokemon2.pv_max})")

    def tour(self):
        # Pokémon 1 attaque en premier
        degats = self.pokemon1.attaquer(self.pokemon2)
        if degats == 0:
            print(f"{self.pokemon1.nom} rate son attaque!")
        else:
            print(f"{self.pokemon1.nom} attaque {self.pokemon2.nom} et lui inflige {degats} points de dégâts!")

        if self.pokemon2.est_ko():
            print(f"{self.pokemon2.nom} est K.O.!")
            return self.pokemon1

        # Pokémon 2 attaque ensuite
        degats = self.pokemon2.attaquer(self.pokemon1)
        if degats == 0:
            print(f"{self.pokemon2.nom} rate son attaque!")
        else:
            print(f"{self.pokemon2.nom} attaque {self.pokemon1.nom} et lui inflige {degats} points de dégâts!")

        if self.pokemon1.est_ko():
            print(f"{self.pokemon1.nom} est K.O.!")
            return self.pokemon2

        return None

    def lancer_combat(self):
        print(f"Le combat commence entre {self.pokemon1.nom} et {self.pokemon2.nom}!")
        while True:
            self.afficher_statut()
            gagnant = self.tour()
            if gagnant:
                print(f"{gagnant.nom} remporte le combat!")
                return gagnant
            print("")

def charger_pokemon_depuis_json(nom_pokemon):
    with open("Pokemon.Json", "r") as fichier:
        data = json.load(fichier)
        for pokemon_data in data["pokemon"]:
            if pokemon_data["name"] == nom_pokemon.lower():
                return Pokemon(
                    nom=pokemon_data["name"],
                    type_pokemon=pokemon_data["types"][0]["type"].capitalize(),
                    pv=pokemon_data["stats"]["hp"],
                    attaque=pokemon_data["stats"]["attack"],
                    defense=pokemon_data["stats"]["defense"]
                )
    raise ValueError(f"Pokémon {nom_pokemon} non trouvé dans le fichier JSON.")

if __name__ == "__main__":
    # Charger deux Pokémon depuis le fichier JSON
    pokemon1 = charger_pokemon_depuis_json("Pikachu")
    pokemon2 = charger_pokemon_depuis_json("Charmander")

    # Lancer le combat
    combat = Combat(pokemon1, pokemon2)
    combat.lancer_combat()