import random
import json

class Pokemon:
    TYPES = [
        'Normal', 'Feu', 'Eau', 'Plante', 'Électrique', 
        'Glace', 'Combat', 'Poison', 'Sol', 'Vol', 
        'Psy', 'Insecte', 'Roche', 'Spectre', 'Dragon', 
        'Ténèbres', 'Acier', 'Fée'
    ]

    TYPE_EFFECTIVENESS = {
        "Normal": {"Roche": 0.5, "Spectre": 0, "Acier": 0.5},
        "Feu": {"Feu": 0.5, "Eau": 0.5, "Plante": 2, "Glace": 2, "Insecte": 2, "Roche": 0.5, "Dragon": 0.5, "Acier": 2},
        "Eau": {"Feu": 2, "Eau": 0.5, "Plante": 0.5, "Sol": 2, "Roche": 2, "Dragon": 0.5},
        "Électrique": {"Eau": 2, "Électrique": 0.5, "Plante": 0.5, "Sol": 0, "Vol": 2, "Dragon": 0.5},
        "Plante": {"Feu": 0.5, "Eau": 2, "Plante": 0.5, "Poison": 0.5, "Sol": 2, "Vol": 0.5, "Insecte": 0.5, "Roche": 2, "Dragon": 0.5, "Acier": 0.5},
        "Glace": {"Feu": 0.5, "Eau": 0.5, "Glace": 0.5, "Plante": 2, "Sol": 2, "Vol": 2, "Dragon": 2, "Acier": 0.5},
        "Combat": {"Normal": 2, "Glace": 2, "Roche": 2, "Ténèbres": 2, "Acier": 2, "Poison": 0.5, "Vol": 0.5, "Psy": 0.5, "Insecte": 0.5, "Fée": 0.5, "Spectre": 0},
        "Poison": {"Plante": 2, "Fée": 2, "Poison": 0.5, "Sol": 0.5, "Roche": 0.5, "Spectre": 0.5, "Acier": 0},
        "Sol": {"Feu": 2, "Électrique": 2, "Plante": 0.5, "Poison": 2, "Vol": 0, "Insecte": 0.5, "Roche": 2, "Acier": 2},
        "Vol": {"Électrique": 0.5, "Combat": 2, "Plante": 2, "Insecte": 2, "Roche": 0.5, "Acier": 0.5},
        "Psy": {"Combat": 2, "Poison": 2, "Psy": 0.5, "Ténèbres": 0, "Acier": 0.5},
        "Insecte": {"Feu": 0.5, "Plante": 2, "Combat": 0.5, "Poison": 0.5, "Vol": 0.5, "Psy": 2, "Spectre": 0.5, "Ténèbres": 2, "Acier": 0.5, "Fée": 0.5},
        "Roche": {"Feu": 2, "Glace": 2, "Combat": 0.5, "Sol": 0.5, "Vol": 2, "Insecte": 2, "Acier": 0.5},
        "Spectre": {"Normal": 0, "Psy": 2, "Spectre": 2, "Ténèbres": 0.5},
        "Dragon": {"Dragon": 2, "Acier": 0.5, "Fée": 0},
        "Ténèbres": {"Combat": 0.5, "Psy": 2, "Spectre": 2, "Ténèbres": 0.5, "Fée": 0.5},
        "Acier": {"Feu": 0.5, "Eau": 0.5, "Électrique": 0.5, "Glace": 2, "Roche": 2, "Acier": 0.5, "Fée": 2},
        "Fée": {"Combat": 2, "Dragon": 2, "Ténèbres": 2, "Feu": 0.5, "Poison": 0.5, "Acier": 0.5}
    }

    def __init__(self, nom, type_pokemon, pv, attaque, defense, niveau=1):
        self.nom = nom
        self.type_pokemon = type_pokemon
        self.pv_max = pv
        self.pv_actuels = pv
        self.attaque = attaque
        self.defense = defense
        self.niveau = niveau

    def attaquer(self, adversaire):
        degats_base = self.attaque
        multiplicateur = self.TYPE_EFFECTIVENESS.get(self.type_pokemon, {}).get(adversaire.type_pokemon, 1)
        degats_finaux = degats_base * multiplicateur
        
        if random.random() < 0.1:
            return 0  # L'attaque échoue
        
        degats_apres_defense = max(1, degats_finaux - adversaire.defense)  # Dégâts minimum de 1
        adversaire.pv_actuels = max(0, adversaire.pv_actuels - degats_apres_defense)
        
        return degats_apres_defense

    def est_ko(self):
        return self.pv_actuels <= 0

    def guerir(self):
        self.pv_actuels = self.pv_max

    def to_dict(self):
        return {
            "nom": self.nom,
            "type": self.type_pokemon,
            "pv": self.pv_max,
            "attaque": self.attaque,
            "defense": self.defense,
            "niveau": self.niveau
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nom=data['nom'],
            type_pokemon=data['type'],
            pv=data['pv'],
            attaque=data['attaque'],
            defense=data['defense'],
            niveau=data.get('niveau', 1)
        )