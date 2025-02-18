import json
import os

class Pokedex:
    def __init__(self, file_path='data/pokedex.json'):
        self.file_path = file_path
        self.captured_pokemon = []
        self.load()

    def add_pokemon(self, pokemon):
        # Check for duplicates by name
        if not any(p.name == pokemon.name for p in self.captured_pokemon):
            self.captured_pokemon.append(pokemon)
            self.save()

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.captured_pokemon = [
                    Pokemon.from_dict(pokemon_data) 
                    for pokemon_data in data
                ]

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump([
                pokemon.to_dict() 
                for pokemon in self.captured_pokemon
            ], f, indent=4)

    def display_pokemon(self):
        for pokemon in self.captured_pokemon:
            print(f"{pokemon.name} (Level {pokemon.level})")
