# import random
# import json

# class Pokemon:
#     TYPES = [
#         'Normal', 'Fire', 'Water', 'Grass', 'Electric', 
#         'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 
#         'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 
#         'Dark', 'Steel', 'Fairy'
#     ]

#     TYPE_EFFECTIVENESS = {
#         "Normal": {"Rock": 0.5, "Ghost": 0, "Steel": 0.5},
#         "Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2, "Ice": 2, "Bug": 2, "Rock": 0.5, "Dragon": 0.5, "Steel": 2},
#         "Water": {"Fire": 2, "Water": 0.5, "Grass": 0.5, "Ground": 2, "Rock": 2, "Dragon": 0.5},
#         "Electric": {"Water": 2, "Electric": 0.5, "Grass": 0.5, "Ground": 0, "Flying": 2, "Dragon": 0.5},
#         "Grass": {"Fire": 0.5, "Water": 2, "Grass": 0.5, "Poison": 0.5, "Ground": 2, "Flying": 0.5, "Bug": 0.5, "Rock": 2, "Dragon": 0.5, "Steel": 0.5},
#         "Ice": {"Fire": 0.5, "Water": 0.5, "Ice": 0.5, "Grass": 2, "Ground": 2, "Flying": 2, "Dragon": 2, "Steel": 0.5},
#         "Fighting": {"Normal": 2, "Ice": 2, "Rock": 2, "Dark": 2, "Steel": 2, "Poison": 0.5, "Flying": 0.5, "Psychic": 0.5, "Bug": 0.5, "Fairy": 0.5, "Ghost": 0},
#         "Poison": {"Grass": 2, "Fairy": 2, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, "Ghost": 0.5, "Steel": 0},
#         "Ground": {"Fire": 2, "Electric": 2, "Grass": 0.5, "Poison": 2, "Flying": 0, "Bug": 0.5, "Rock": 2, "Steel": 2},
#         "Flying": {"Electric": 0.5, "Fighting": 2, "Grass": 2, "Bug": 2, "Rock": 0.5, "Steel": 0.5},
#         "Psychic": {"Fighting": 2, "Poison": 2, "Psychic": 0.5, "Dark": 0, "Steel": 0.5},
#         "Bug": {"Fire": 0.5, "Grass": 2, "Fighting": 0.5, "Poison": 0.5, "Flying": 0.5, "Psychic": 2, "Ghost": 0.5, "Dark": 2, "Steel": 0.5, "Fairy": 0.5},
#         "Rock": {"Fire": 2, "Ice": 2, "Fighting": 0.5, "Ground": 0.5, "Flying": 2, "Bug": 2, "Steel": 0.5},
#         "Ghost": {"Normal": 0, "Psychic": 2, "Ghost": 2, "Dark": 0.5},
#         "Dragon": {"Dragon": 2, "Steel": 0.5, "Fairy": 0},
#         "Dark": {"Fighting": 0.5, "Psychic": 2, "Ghost": 2, "Dark": 0.5, "Fairy": 0.5},
#         "Steel": {"Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Ice": 2, "Rock": 2, "Steel": 0.5, "Fairy": 2},
#         "Fairy": {"Fighting": 2, "Dragon": 2, "Dark": 2, "Fire": 0.5, "Poison": 0.5, "Steel": 0.5}
#     }

#     def __init__(self, name, pokemon_type, hp, attack, defense, level=1):
#         self.name = name
#         self.pokemon_type = pokemon_type
#         self.max_hp = hp
#         self.current_hp = hp
#         self.attack = attack
#         self.defense = defense
#         self.level = level

#     def attack_opponent(self, opponent):
#         base_damage = self.attack
#         multiplier = self.TYPE_EFFECTIVENESS.get(self.pokemon_type, {}).get(opponent.pokemon_type, 1)
#         final_damage = base_damage * multiplier
        
#         if random.random() < 0.1:
#             return 0  # The attack misses
        
#         damage_after_defense = max(1, final_damage - opponent.defense)  # Minimum damage of 1
#         opponent.current_hp = max(0, opponent.current_hp - damage_after_defense)
        
#         return damage_after_defense

#     def is_knocked_out(self):
#         return self.current_hp <= 0

#     def heal(self):
#         self.current_hp = self.max_hp

#     def to_dict(self):
#         return {
#             "name": self.name,
#             "type": self.pokemon_type,
#             "hp": self.max_hp,
#             "attack": self.attack,
#             "defense": self.defense,
#             "level": self.level
#         }

#     @classmethod
#     def from_dict(cls, data):
#         return cls(
#             name=data['name'],
#             pokemon_type=data['type'],
#             hp=data['hp'],
#             attack=data['attack'],
#             defense=data['defense'],
#             level=data.get('level', 1)
#         )


import random
import pygame

class Pokemon:
    def __init__(self, id, name, base_experience, types, stats, abilities, moves, sprites):
        self.id = id
        self.name = name
        self.base_experience = base_experience
        self.types = [t["type"] for t in types]
        self.stats = stats
        self.abilities = abilities
        self.moves = moves
        self.sprites = sprites
        self.hp = stats["hp"]  # Initialize current HP to max HP

        # Load Pokémon images using pygame
        self.front_image = pygame.image.load(sprites["front_default"])
        self.back_image = pygame.image.load(sprites["back_default"])

    def attack(self, move, target):
        if move not in self.moves:
            print(f"{self.name} doesn't know {move}!")
            return False

        damage = random.randint(10, 30)  # Simulate damage calculation
        target.hp -= damage
        target.hp = max(0, target.hp)  # Ensure HP doesn't go below 0
        print(f"{self.name} used {move}! It dealt {damage} damage to {target.name}.")
        print(f"{target.name}'s HP is now {target.hp}.")
        
        if target.hp == 0:
            print(f"{target.name} fainted!")
            return True
        
        return False

    def is_fainted(self):
        return self.hp <= 0

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Types: {', '.join(self.types)}")
        print("Stats:")
        for stat, value in self.stats.items():
            print(f"  {stat.capitalize()}: {value}")
        print(f"Abilities: {[ability['name'] for ability in self.abilities]}")
