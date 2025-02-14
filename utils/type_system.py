class TypeSystem:
    TYPES = {
        'Normal': {},
        'Fire': {'Grass': 2, 'Ice': 2, 'Water': 0.5},
        'Water': {'Fire': 2, 'Rock': 2, 'Grass': 0.5},
        'Grass': {'Water': 2, 'Rock': 2, 'Fire': 0.5},
        'Electric': {'Water': 2, 'Flying': 2},
        # Add other types...
    }

    @classmethod
    def calculate_multiplier(cls, attacking_type, defending_type):
        return cls.TYPES.get(attacking_type, {}).get(defending_type, 1)

    @classmethod
    def is_effective(cls, attacking_type, defending_type):
        multiplier = cls.calculate_multiplier(attacking_type, defending_type)
        return multiplier > 1
