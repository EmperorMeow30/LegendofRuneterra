# Slime enemy
class Slime:
    def __init__(self, name="Slime", level=1):
        self.name = name
        self.level = level
        self.race = "Slime"
        self.health = 50 + (level * 10)  # Base health increases with level
        self.max_health = self.health
        self.attack = 5 + (level * 2)  # Base attack increases with level
        self.defense = 0

    def take_damage(self, damage):
        """Reduces health based on incoming damage and defense."""
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. Remaining health: {self.health}/{self.max_health}")
        if self.health <= 0:
            self.die()

    def reset_stats(self):
        self.health = self.health
        self.max_health = self.health

    def die(self):
        """Handles death."""
        print(f"The {self.name} has been defeated!")

    def attack_target(self, target):
        """Attacks a target, reducing their health, returns damage dealt."""
        damage =  max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.get_name()} for {damage} damage!")
        target.take_damage(damage)
        return damage # Return the damage dealt

    def __str__(self):
        return (
            f"Name: {self.name}, Race = Slime, Level: {self.level}, "
            f"Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}"
        )

# Orc enemy
class Orc:
    def __init__(self, name="Orc", level=1):
        self.name = name
        self.level = level
        self.race = "Orc"
        self.health = 60 + (level * 15)  # Base health increases with level
        self.max_health = self.health
        self.attack = 7 + (level * 3)  # Base attack increases with level
        self.defense = 3

    def take_damage(self, damage):
        """Reduces health based on incoming damage and defense."""
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. Remaining health: {self.health}/{self.max_health}")
        if self.health <= 0:
            self.die()

    def reset_stats(self):
         self.health = 60 + (self.level * 15)
         self.max_health = 60 + (self.level * 15)

    def die(self):
        """Handles death."""
        print(f"The {self.name} has been defeated!")

    def attack_target(self, target):
        """Attacks a target, reducing their health, returns damage dealt."""
        damage = max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.get_name()} for {damage} damage!")
        target.take_damage(damage)
        return damage # Returns the damage dealt

    def __str__(self):
        return (
            f"Name: {self.name}, Race: Orc, Level: {self.level}, "
            f"Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}"
        )

# Orc King enemy
class OrcKing:
    def __init__(self, name="Orcus", level=1):
        self.name = name
        self.level = level
        self.race = "Orc King"
        self.health = 70 + (level * 15)  # Base health increases with level
        self.max_health = self.health
        self.attack = 10 + (level * 3)  # Base attack increases with level
        self.defense = 5 + level  # Base defense increases with level

    def take_damage(self, damage):
        """Reduces health based on incoming damage and defense."""
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. Remaining health: {self.health}/{self.max_health}")
        if self.health <= 0:
            self.die()

    def reset_stats(self):
        self.health = 70 + (self.level * 15)
        self.max_health = 70 + (self.level * 15)

    def die(self):
        """Handles death."""
        print(f"The {self.name} has been defeated!")

    def attack_target(self, target):
        """Attacks a target, reducing their health, returns damage dealt."""
        damage =  max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.get_name()} for {damage} damage!")
        target.take_damage(damage)
        return damage

    def __str__(self):
        return (
            f"Name: {self.name}, Race: Orc, Level: {self.level}, "
            f"Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}"
        )

# Infernal Guard enemy
class InfernalGuard:
    def __init__(self, name="Rathimael", level=1):
        self.name = name
        self.level = level
        self.race = "Demon"
        self.health = 100 + (level * 20)  # Base health increases with level
        self.max_health = self.health
        self.attack = 15 + (level * 5)  # Base attack increases with level
        self.defense = 10 + level  # Base defense increases with level

    def take_damage(self, damage):
        """Reduces health based on incoming damage and defense."""
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. Remaining health: {self.health}/{self.max_health}")
        if self.health <= 0:
            self.die()

    def reset_stats(self):
        self.health = 100 + (self.level * 20)
        self.max_health = self.health

    def die(self):
        """Handles death."""
        print(f"The {self.name} has been defeated!")

    def attack_target(self, target):
        """Attacks a target, reducing their health, returns damage dealt."""
        damage =  max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.get_name()} for {damage} damage!")
        target.take_damage(damage)
        return damage

    def __str__(self):
        return (
            f"Name: {self.name}, Race: Demon, Level: {self.level}, "
            f"Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}"
        )

# Elise enemy
class Elise:
    def __init__(self, name="Elise", level=1):
        self.name = name
        self.level = level
        self.race = "Demon"
        self.health = 150 + (level * 30)  # Base health increases with level
        self.max_health = self.health
        self.attack = 30 + (level * 7)  # Base attack increases with level
        self.defense = 15 + level  # Base defense increases with level

    def take_damage(self, damage):
        """Reduces health based on incoming damage and defense."""
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. Remaining health: {self.health}/{self.max_health}")
        if self.health <= 0:
            self.die()

    def reset_stats(self):
        self.health = 150 + (self.level * 30)
        self.max_health = self.health

    def die(self):
        """Handles death."""
        print(f"The {self.name} has been defeated!")

    def attack_target(self, target):
        """Attacks a target, reducing their health, returns damage dealt."""
        damage =  max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.get_name()} for {damage} damage!")
        target.take_damage(damage)
        return damage

    def __str__(self):
        return (
            f"Name: {self.name}, Race: Demon, Level: {self.level}, "
            f"Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}"
        )

# Elise enemy
class EliseFinalForm:
    def __init__(self, name="Elise (Potential Unlocked)", level=1):
        self.name = name
        self.level = level
        self.race = "Hybrid"
        self.health = 300 + (level * 50)  # Base health increases with level
        self.max_health = self.health
        self.attack = 50 + (level * 10)  # Base attack increases with level
        self.defense = 30 + level  # Base defense increases with level

    def take_damage(self, damage):
        """Reduces health based on incoming damage and defense."""
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. Remaining health: {self.health}/{self.max_health}")
        if self.health <= 0:
            self.die()

    def reset_stats(self):
        self.health = 300 + (self.level * 50)
        self.max_health = self.health

    def die(self):
        """Handles death."""
        print(f"The {self.name} has been defeated!")

    def attack_target(self, target):
        """Attacks a target, reducing their health, returns damage dealt."""
        damage =  max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.get_name()} for {damage} damage!")
        target.take_damage(damage)
        return damage

    def __str__(self):
        return (
            f"Name: {self.name}, Race: Hybrid, Level: {self.level}, "
            f"Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}"
        )