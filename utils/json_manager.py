import json
import os
from models.pokemon import Pokemon

class JSONManager:
    @staticmethod
    def load_pokemon(file='data/pokemon.json'):
        if not os.path.exists(file):
            return []
        
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return [Pokemon.from_dict(pokemon) for pokemon in data]

    @staticmethod
    def add_pokemon(pokemon, file='data/pokemon.json'):
        existing_pokemon = JSONManager.load_pokemon(file)
        
        # Check for duplicates
        if not any(p.name == pokemon.name for p in existing_pokemon):
            existing_pokemon.append(pokemon)
        
        with open(file, 'w', encoding='utf-8') as f:
            json.dump([p.to_dict() for p in existing_pokemon], f, indent=4, ensure_ascii=False)

    @staticmethod
    def save_pokedex(pokemons, file='data/pokedex.json'):
        data = {
            "captured_pokemon": [
                {
                    "name": p.name,
                    "level": p.level
                } for p in pokemons
            ]
        }
        
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
