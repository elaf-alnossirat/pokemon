import pygame
from utils.json_manager import JSONManager
from models.pokemon import Pokemon
from ui.game_interface import PokemonInterface
from models.battle import Battle
import json

class PokemonGame:
    def __init__(self):
        pygame.init()
        self.json_manager = JSONManager()
        self.interface = PokemonInterface()
        self.available_pokemon = self.load_pokemon()

    def load_pokemon(self):
        return self.json_manager.load_pokemon()

    def start_game(self):
        while True:
            action = self.interface.main_menu()
            print(f"Chosen action: {action}")

            if action == 0:  # "Start Game" is selected
                player_pokemon = self.interface.choose_pokemon(self.available_pokemon)  # Choose player's Pokémon
                print(f"Player chose: {player_pokemon.name}")
                enemy_pokemon = self.load_pokemon_from_json("Charmander")  # Example enemy Pokémon
                print(f"Enemy Pokémon: {enemy_pokemon.name}")
                self.start_battle(player_pokemon, enemy_pokemon)

            elif action == 1:  # "Add Pokémon" is selected
                # Interface to add a new Pokémon
                pass

            elif action == 2:  # "View Pokédex" is selected
                self.interface.show_pokedex()

            elif action == 3:  # Exit on quitting
                break

    def start_battle(self, player_pokemon, enemy_pokemon):
        # Create the Battle instance with the chosen Pokémon
        battle = Battle(player_pokemon, enemy_pokemon)
        
        # Start the battle
        print("Starting battle...")
        battle.start_battle()
        
    def load_pokemon_from_json(self, pokemon_name):
        with open("Pokemon.Json", "r") as file:
            data = json.load(file)
            for pokemon_data in data["pokemon"]:
                if pokemon_data["name"].lower() == pokemon_name.lower():
                    return Pokemon(
                        name=pokemon_data["name"],
                        pokemon_type=pokemon_data["types"][0]["type"].capitalize(),
                        hp=pokemon_data["stats"]["hp"],
                        attack=pokemon_data["stats"]["attack"],
                        defense=pokemon_data["stats"]["defense"]
                    )
        raise ValueError(f"Pokémon {pokemon_name} not found in the JSON file.")
        
def main():
    game = PokemonGame()
    game.start_game()

if __name__ == "__main__":
    main()

