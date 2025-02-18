import pygame
import time
import math
import random
import requests
import io
from urllib.request import urlopen
from ui.game_interface import PokemonInterface  # Import UI module

# Initialize Pygame
pygame.init()

# Game settings
game_width, game_height = 500, 500
game = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Pokemon Battle')

# Colors
BLACK, GOLD, GREY, GREEN, RED, WHITE = (0, 0, 0), (218, 165, 32), (200, 200, 200), (0, 200, 0), (200, 0, 0), (255, 255, 255)

# Base API URL
BASE_URL = 'https://pokeapi.co/api/v2'

class Move:
    def __init__(self, url):
        req = requests.get(url)
        data = req.json()
        self.name = data['name']
        self.power = data['power'] or 0
        self.type = data['type']['name']

class Pokemon:
    def __init__(self, name, level, x, y):
        req = requests.get(f'{BASE_URL}/pokemon/{name.lower()}')
        data = req.json()
        self.name = name
        self.level = level
        self.x, self.y = x, y
        self.num_potions = 3
        
        # Stats
        stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
        self.max_hp = stats['hp'] + level
        self.current_hp = self.max_hp
        self.attack = stats['attack']
        self.defense = stats['defense']
        self.speed = stats['speed']
        self.types = [t['type']['name'] for t in data['types']]
        
        # Sprite
        self.image = self.load_sprite(data['sprites']['front_default'])
        
        # Moves
        self.moves = self.get_moves(data['moves'])
    
    def load_sprite(self, url):
        image_stream = urlopen(url).read()
        image_file = io.BytesIO(image_stream)
        return pygame.image.load(image_file).convert_alpha()
    
    def get_moves(self, moves_data):
        moves = []
        for move in moves_data:
            move_url = move['move']['url']
            move_obj = Move(move_url)
            if move_obj.power:
                moves.append(move_obj)
        return random.sample(moves, min(4, len(moves)))
    
    def attack_opponent(self, opponent, move):
        damage = max(1, ((2 * self.level / 5 + 2) * move.power * self.attack / opponent.defense) / 50 + 2)
        if move.type in self.types:
            damage *= 1.5  # STAB bonus
        if random.random() < 0.0625:
            damage *= 1.5  # Critical hit
        opponent.take_damage(math.floor(damage))
    
    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)
    
    def use_potion(self):
        if self.num_potions > 0:
            self.current_hp = min(self.max_hp, self.current_hp + 30)
            self.num_potions -= 1
    
class Battle:
    def __init__(self, player_pokemon, enemy_pokemon):
        self.player_pokemon = player_pokemon
        self.enemy_pokemon = enemy_pokemon

    def start_battle(self):
        print(f"Battle started between {self.player_pokemon.name} and {self.enemy_pokemon.name}")
        # Implement the battle logic here
    
    def take_turn(self):
        if self.player_pokemon.speed >= self.enemy_pokemon.speed:
            self.player_attack()
            if self.enemy_pokemon.current_hp > 0:
                self.enemy_attack()
        else:
            self.enemy_attack()
            if self.player_pokemon.current_hp > 0:
                self.player_attack()
    
    def player_attack(self):
        move = random.choice(self.player_pokemon.moves)
        self.player_pokemon.attack_opponent(self.enemy_pokemon, move)
    
    def enemy_attack(self):
        move = random.choice(self.enemy_pokemon.moves)
        self.enemy_pokemon.attack_opponent(self.player_pokemon, move)
    
class Game:
    def __init__(self):
        self.running = True
        self.level = 30
        self.interface = PokemonInterface()
        self.available_pokemon = [Pokemon('Bulbasaur', self.level, 50, 150), Pokemon('Charmander', self.level, 250, 150)]
    
    def run(self):
        while self.running:
            action = self.interface.main_menu()
            if action == 0:  # "Start Game"
                player_pokemon = self.interface.choose_pokemon(self.available_pokemon)
                rival_pokemon = Pokemon('Charmander', self.level, 250, 150)
                self.start_battle(player_pokemon, rival_pokemon)
            elif action == 3:
                self.running = False
    
    def start_battle(self, player_pokemon, rival_pokemon):
        battle = Battle(player_pokemon, rival_pokemon)
        while player_pokemon.current_hp > 0 and rival_pokemon.current_hp > 0:
            battle.take_turn()
        print("Battle Over")

if __name__ == '__main__':
    Game().run()
    pygame.quit()



# import json
# import random
# import pygame
# from pokemon import Pokemon

# # Screen dimensions for pygame
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# def load_pokemon_from_json(filepath):
#     with open(filepath, "r") as file:
#         data = json.load(file)
#     pokemons = []
#     for p in data["pokemon"]:
#         pokemons.append(Pokemon(
#             id=p["id"],
#             name=p["name"],
#             base_experience=p["base_experience"],
#             types=p["types"],
#             stats=p["stats"],
#             abilities=p["abilities"],
#             moves=p["moves"],
#             sprites=p["sprites"]
#         ))
#     return pokemons

# def battle(screen, pokemon1, pokemon2):
#     font = pygame.font.Font(None, 36)
#     clock = pygame.time.Clock()

#     print(f"A wild battle begins between {pokemon1.name} and {pokemon2.name}!")
    
#     while not pokemon1.is_fainted() and not pokemon2.is_fainted():
#         screen.fill((255, 255, 255))  # Clear screen with white background

#         # Display Pokémon images and names
#         screen.blit(pokemon1.back_image, (100, 300))  # Player's Pokémon (back image)
#         screen.blit(pokemon2.front_image, (500, 100))  # Opponent's Pokémon (front image)

#         player_text = font.render(f"{pokemon1.name} HP: {pokemon1.hp}", True, (0, 0, 0))
#         opponent_text = font.render(f"{pokemon2.name} HP: {pokemon2.hp}", True, (0, 0, 0))
        
#         screen.blit(player_text, (50, 50))
#         screen.blit(opponent_text, (500, 50))

#         pygame.display.flip()

#         # Pokémon 1 attacks Pokémon 2
#         move1 = random.choice(pokemon1.moves)
#         if pokemon1.attack(move1, pokemon2):
#             break
        
#         # Pokémon 2 attacks Pokémon 1 (if still alive)
#         if not pokemon2.is_fainted():
#             move2 = random.choice(pokemon2.moves)
#             pokemon2.attack(move2, pokemon1)

#         clock.tick(1)  # Pause for a second between turns

# def main():
#     # Initialize pygame
#     pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Pokémon Battle")

#     pokemons = load_pokemon_from_json("pokemons.json")
    
#     # Display all loaded Pokémon in the terminal for selection
#     print("Available Pokémon:")
#     for i, p in enumerate(pokemons):
#         print(f"{i + 1}. {p.name}")

#     # Let the player choose their Pokémon
#     choice1 = int(input("Choose your Pokémon (enter number): ")) - 1
#     player_pokemon = pokemons[choice1]

#     # Randomly select an opponent Pokémon
#     opponent_pokemon = random.choice(pokemons)

#     # Display chosen Pokémon stats in the terminal
#     print("\nYour Pokémon:")
#     player_pokemon.display_stats()
    
#     print("\nOpponent's Pokémon:")
#     opponent_pokemon.display_stats()

#     # Start the battle loop with visuals
#     battle(screen, player_pokemon, opponent_pokemon)

# if __name__ == "__main__":
#     main()

