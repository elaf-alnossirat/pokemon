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





# import pygame
# import sys
# import os
# from typing import Tuple, List

# class Battle:
#     def __init__(self, screen_width=1000, screen_height=600):
#         self.screen_width = screen_width
#         self.screen_height = screen_height
#         self.screen = pygame.display.set_mode((screen_width, screen_height))
#         pygame.display.set_caption("Pokemon Battle")

#         # Colors
#         self.WHITE = (255, 255, 255)
#         self.BLACK = (0, 0, 0)
#         self.RED = (255, 0, 0)
#         self.GREEN = (0, 255, 0)

#         # Load battle background
#         self.background = pygame.image.load("assets/battle-background.png")
#         self.background = pygame.transform.scale(self.background, (screen_width, screen_height))

#         # Font
#         self.font = pygame.font.Font(None, 36)

#         # Battle state
#         self.battle_active = True
#         self.current_turn = "player"
#         self.battle_log = []

#     def load_pokemon_sprites(self, player_pokemon_name: str, enemy_pokemon_name: str) -> Tuple[pygame.Surface, pygame.Surface]:
#         """Load and scale Pokemon sprites."""
#         player_sprite = pygame.image.load(f"assets/pokemon/{player_pokemon_name.lower()}.png")
#         enemy_sprite = pygame.image.load(f"assets/pokemon/{enemy_pokemon_name.lower()}.png")

#         # Scale sprites to appropriate size (adjust sizes as needed)
#         player_sprite = pygame.transform.scale(player_sprite, (200, 200))
#         enemy_sprite = pygame.transform.scale(enemy_sprite, (200, 200))

#         return player_sprite, enemy_sprite

#     def create_health_bar(self, current_hp: int, max_hp: int, position: Tuple[int, int], size: Tuple[int, int]) -> None:
#         """Draw a health bar at the specified position."""
#         x, y = position
#         width, height = size
        
#         # Background (red) rectangle
#         pygame.draw.rect(self.screen, self.RED, (x, y, width, height))
        
#         # Health (green) rectangle
#         health_width = int((current_hp / max_hp) * width)
#         pygame.draw.rect(self.screen, self.GREEN, (x, y, health_width, height))

#     def check_collision(self, rect1: pygame.Rect, rect2: pygame.Rect) -> bool:
#         """Check if two rectangles are colliding."""
#         return rect1.colliderect(rect2)

#     def handle_attack_animation(self, attacker_rect: pygame.Rect, target_rect: pygame.Rect, 
#                               attacker_sprite: pygame.Surface, is_player: bool) -> None:
#         """Handle attack animation with collision detection."""
#         original_pos = attacker_rect.copy()
#         speed = 10
        
#         # Animation frames
#         for _ in range(20):
#             self.screen.blit(self.background, (0, 0))
            
#             # Move sprite
#             if is_player:
#                 attacker_rect.x += speed
#             else:
#                 attacker_rect.x -= speed

#             # Check for collision
#             if self.check_collision(attacker_rect, target_rect):
#                 # Flash the target sprite
#                 pygame.time.delay(50)
#                 # Return to original position
#                 attacker_rect = original_pos
#                 break

#             # Draw sprites
#             self.screen.blit(attacker_sprite, attacker_rect)
#             pygame.display.flip()
#             pygame.time.delay(20)

#     def display_battle_menu(self) -> List[pygame.Rect]:
#         """Display battle menu and return list of button rectangles."""
#         buttons = []
#         menu_items = ["Attack", "Item", "Pokemon", "Run"]
        
#         for i, item in enumerate(menu_items):
#             button_rect = pygame.Rect(700, 400 + (i * 50), 200, 40)
#             pygame.draw.rect(self.screen, self.WHITE, button_rect)
#             text = self.font.render(item, True, self.BLACK)
#             text_rect = text.get_rect(center=button_rect.center)
#             self.screen.blit(text, text_rect)
#             buttons.append(button_rect)
            
#         return buttons

#     def run_battle(self, player_pokemon: 'Pokemon', enemy_pokemon: 'Pokemon') -> None:
#         """Main battle loop."""
#         clock = pygame.time.Clock()
        
#         # Load Pokemon sprites
#         player_sprite, enemy_sprite = self.load_pokemon_sprites(player_pokemon.name, enemy_pokemon.name)
        
#         # Position sprites
#         player_rect = player_sprite.get_rect(center=(250, 400))
#         enemy_rect = enemy_sprite.get_rect(center=(750, 200))

#         while self.battle_active:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
                    
#                 if event.type == pygame.MOUSEBUTTONDOWN and self.current_turn == "player":
#                     mouse_pos = pygame.mouse.get_pos()
#                     buttons = self.display_battle_menu()
                    
#                     # Check which button was clicked
#                     for i, button in enumerate(buttons):
#                         if button.collidepoint(mouse_pos):
#                             if i == 0:  # Attack
#                                 # Player's turn
#                                 damage = player_pokemon.attack_opponent(enemy_pokemon)
#                                 self.handle_attack_animation(player_rect, enemy_rect, player_sprite, True)
#                                 self.battle_log.append(f"{player_pokemon.name} deals {damage} damage!")
                                
#                                 # Enemy's turn
#                                 if not enemy_pokemon.is_knocked_out():
#                                     self.current_turn = "enemy"
#                                     damage = enemy_pokemon.attack_opponent(player_pokemon)
#                                     self.handle_attack_animation(enemy_rect, player_rect, enemy_sprite, False)
#                                     self.battle_log.append(f"{enemy_pokemon.name} deals {damage} damage!")
#                                     self.current_turn = "player"

#             # Draw background
#             self.screen.blit(self.background, (0, 0))
            
#             # Draw Pokemon sprites
#             self.screen.blit(player_sprite, player_rect)
#             self.screen.blit(enemy_sprite, enemy_rect)
            
#             # Draw health bars
#             self.create_health_bar(player_pokemon.current_hp, player_pokemon.max_hp, (100, 450), (200, 20))
#             self.create_health_bar(enemy_pokemon.current_hp, enemy_pokemon.max_hp, (700, 50), (200, 20))
            
#             # Display battle menu
#             if self.current_turn == "player":
#                 self.display_battle_menu()
            
#             # Display battle log
#             for i, log in enumerate(self.battle_log[-3:]):  # Show last 3 messages
#                 text = self.font.render(log, True, self.WHITE)
#                 self.screen.blit(text, (50, 50 + (i * 30)))
            
#             # Check for battle end
#             if player_pokemon.is_knocked_out() or enemy_pokemon.is_knocked_out():
#                 winner = enemy_pokemon.name if player_pokemon.is_knocked_out() else player_pokemon.name
#                 self.battle_log.append(f"{winner} wins the battle!")
#                 pygame.time.delay(2000)  # Show result for 2 seconds
#                 self.battle_active = False
            
#             pygame.display.flip()
#             clock.tick(60)

# def initialize_battle():
#     """Initialize and start a battle."""
#     pygame.init()
#     battle_system = BattleSystem()
#     return battle_system
