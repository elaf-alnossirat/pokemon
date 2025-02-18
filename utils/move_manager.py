import requests

def get_move_details(move_name):
    url = f"https://pokeapi.co/api/v2/move/{move_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "power": data.get("power"),
            "accuracy": data.get("accuracy"),
            "pp": data.get("pp"),
            "damage_class": data["damage_class"]["name"],
        }
    else:
        raise ValueError(f"the attack {move_name} is not found on PokéAPI")
