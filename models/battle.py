import random
from models.pokemon import Pokemon
from ui.game_interface import PokemonInterface
import json


class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def display_status(self):
        print(f"{self.pokemon1.name} (HP: {self.pokemon1.current_hp}/{self.pokemon1.max_hp}) vs {self.pokemon2.name} (HP: {self.pokemon2.current_hp}/{self.pokemon2.max_hp})")

    def turn(self):
        # Pokémon 1 attacks first
        damage = self.pokemon1.attack(self.pokemon2)
        if damage == 0:
            print(f"{self.pokemon1.name} misses the attack!")
        else:
            print(f"{self.pokemon1.name} attacks {self.pokemon2.name} and deals {damage} damage!")

        if self.pokemon2.is_knocked_out():
            print(f"{self.pokemon2.name} is KO!")
            return self.pokemon1

        # Pokémon 2 attacks next
        damage = self.pokemon2.attack(self.pokemon1)
        if damage == 0:
            print(f"{self.pokemon2.name} misses the attack!")
        else:
            print(f"{self.pokemon2.name} attacks {self.pokemon1.name} and deals {damage} damage!")

        if self.pokemon1.is_knocked_out():
            print(f"{self.pokemon1.name} is KO!")
            return self.pokemon2

        return None

    def start_battle(self):
        print(f"The battle begins between {self.pokemon1.name} and {self.pokemon2.name}!")
        while True:
            self.display_status()
            winner = self.turn()
            if winner:
                print(f"{winner.name} wins the battle!")
                return winner
            print("")

def load_pokemon_from_json(pokemon_name):
    with open("Pokemon.Json", "r") as file:
        data = json.load(file)
        for pokemon_data in data["pokemon"]:
            if pokemon_data["name"] == pokemon_name.lower():
                return Pokemon(
                    name=pokemon_data["name"],
                    pokemon_type=pokemon_data["types"][0]["type"].capitalize(),
                    hp=pokemon_data["stats"]["hp"],
                    attack=pokemon_data["stats"]["attack"],
                    defense=pokemon_data["stats"]["defense"]
                )
    raise ValueError(f"Pokémon {pokemon_name} not found in the JSON file.")

if __name__ == "__main__":
    # Load two Pokémon from the JSON file
    pokemon1 = load_pokemon_from_json("Pikachu")
    pokemon2 = load_pokemon_from_json("Charmander")

    # Start the battle
    battle = Battle(pokemon1, pokemon2)
    battle.start_battle()




