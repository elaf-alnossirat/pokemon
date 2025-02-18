import requests
import pygame
from utils.json_manager import JSONManager
from models.pokemon import Pokemon
from ui.game_interface import PokemonInterface
from models.battle import Battle
#from utils.move_manager import get_move_details


# class PokemonGame:
#     def __init__(self):
#         pygame.init()
#         self.json_manager = JSONManager()
#         self.interface = PokemonInterface()
#         self.available_pokemon = self.load_pokemon()

#     def load_pokemon(self):
#         return self.json_manager.load_pokemon()

#     def add_new_pokemon(self, name, pokemon_type, hp, attack, defense):
#         new_pokemon = Pokemon(name, pokemon_type, hp, attack, defense)
#         self.json_manager.add_pokemon(new_pokemon)
#         self.available_pokemon.append(new_pokemon)

#     def start_game(self):
#         while True:
#             action = self.interface.main_menu()
#             print(f"Chosen action: {action}")

#             if action == "battle":
#                 self.interface.start_battle(self.available_pokemon)

#             elif action == "add_pokemon":
#                 # Interface to add a new Pokémon
#                 pass

#             elif action == "pokedex":
#                 self.interface.show_pokedex()

#             elif action == "quit":
#                 break
    
#     def start_battle(self):
#         # Load two Pokémon (e.g., Pikachu and Charmander)
#         pokemon1 = self.load_pokemon_from_json("Pikachu")
#         pokemon2 = self.load_pokemon_from_json("Charmander")

#         # Create a Battle instance
#         battle = Battle(pokemon1, pokemon2)

#         # Start the battle
#         battle.start_battle()
        
    
#     def load_pokemon_from_json(self, pokemon_name):
#         with open("Pokemon.Json", "r") as file:
#             data = json.load(file)
#             for pokemon_data in data["pokemon"]:
#                 if pokemon_data["name"] == pokemon_name.lower():
#                     return Pokemon(
#                         name=pokemon_data["name"],
#                         pokemon_type=pokemon_data["types"][0]["type"].capitalize(),
#                         hp=pokemon_data["stats"]["hp"],
#                         attack=pokemon_data["stats"]["attack"],
#                         defense=pokemon_data["stats"]["defense"]
#                     )
#         raise ValueError(f"Pokémon {pokemon_name} not found in the JSON file.")   


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
                enemy_pokemon = self.load_pokemon_from_json("Charmander")  # Example enemy Pokémon
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
        battle.start_battle()
        
    def load_pokemon_from_json(self, pokemon_name):
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
 
       
                    
def main():
    game = PokemonGame()
    game.start_game()

if __name__ == "__main__":
    main()
()