# Skill class
class Skill:
    # Default attributes
    def __init__(self, name, level=1, description=""):
        self.name = name
        self.level = level
        self.description = description

    # Function that will return if the skill leveled up
    def level_up(self):
        self.level += 1
        print(f"Skill '{self.name}' leveled up! It is now level {self.level}.")

    # If the skill is called
    def __str__(self):
        return f"{self.name} (Level {self.level}): {self.description}"

# Skills Class
class Skills:
    # Default attributes
    def __init__(self):
        self.skills = {}

    # Function to add skill
    def add_skill(self, name, description=""):
        if name in self.skills:
            print(f"Skill '{name}' already exists.")
        else:
            self.skills[name] = Skill(name, description=description)
            print(f"Skill '{name}' added to your skill set.")

    # Function to remove skill
    def remove_skill(self, name):
        if name in self.skills:
            del self.skills[name]
            print(f"Skill '{name}' has been removed.")
        else:
            print(f"Skill '{name}' does not exist.")

    # Function to level up skill, uses the level up function from the Skill class
    def level_up_skill(self, name):
        if name in self.skills:
            self.skills[name].level_up()
        else:
            print(f"Skill '{name}' does not exist.")

    # Function to display skills
    def display_skills(self):
        if not self.skills:
            print("You have no skills.")
        else:
            print("Your Skills:")
            for skill in self.skills.values():
                print(f"- {skill}")

    # Checks if there is a particular skill possessed by the user
    def get_skill(self, name):
        return self.skills.get(name, None)

# Inventory class
class Inventory:
    # Inventory stores items as a dictionary: {item_name: quantity}
    def __init__(self):
        self.items = {}

    # Adds an item to the inventory.
    def add_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    # Removes an item to the inventory.
    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]
        else:
            print(f"Item '{item_name}' not found in inventory.")

    # Display the contents of the inventory.
    def display_inventory(self):
        print("Inventory:")
        if not self.items:
            print("  Your inventory is empty.")
        else:
            for item, quantity in self.items.items():
                print(f"  {item}: {quantity}")

    # Checks if the inventory contains at least a certain quantity of an item.
    def has_item(self, item_name, quantity=1):
        return self.items.get(item_name, 0) >= quantity

# Character class
class Character:
    def __init__(self, name="", isHero=False, isEvil=False, isNeutral=False):
        # Basic Info
        self.name = name
        self.isHero = isHero
        self.isEvil = isEvil
        self.isNeutral = isNeutral

        # Inventory and Skill System
        self.inventory = Inventory()
        self.skills = Skills()

        # Attributes
        self.level = 1
        self.experience = 0
        self.health = 100
        self.max_health = self.health
        self.attack = 10
        self.defense = 3

    # Returns particular value depending on their path
    def path(self):
        if self.isNeutral:
            return "Neutral Path"
        elif self.isHero:
            return "Hero Path"
        elif self.isEvil:
            return "Evil Path"
        else:
            return "Unknown"

    # Function to set name of the user
    def set_name(self, name):
        self.name = name

    # Function to get the name of the user
    def get_name(self):
        return self.name

    # Function to rectify their paths
    def set_fate(self, isHero=False, isEvil=False, isNeutral=False):
        self.isHero = isHero
        self.isEvil = isEvil
        self.isNeutral = isNeutral

    # Adds experience points and handles level-up logic.
    def gain_experience(self, exp):
        self.experience += exp
        print(f"{self.name} gained {exp} experience points!")
        while self.experience >= self._experience_to_next_level():
            self.level_up()

    # Handles leveling up and attribute increases.
    def level_up(self):
        self.level += 1
        self.experience -= self._experience_to_next_level()
        self.max_health = 100 + (10 * self.level)
        self.health = self.max_health
        self.attack += 5 + (3 * self.level)
        self.defense += 3 + (1.5 * self.level)
        print(f"{self.name} leveled up to Level {self.level}! {self.name} will have to gain {self._experience_to_next_level()} experience points to level up to level {self.level + 1}! Current: {self.experience // -1 - self.experience // -1}/{self._experience_to_next_level()}")
        print(f"New Stats - Health: {self.max_health}, Attack: {self.attack}, Defense: {self.defense}")

    # Returns the experience required to level up.
    def _experience_to_next_level(self):
        return 100 * self.level

    # Reduces health based on incoming damage and defense.
    def take_damage(self, damage):
        damage_taken = max(0, damage - self.defense)
        self.health -= damage_taken
        print(f"{self.name} took {damage_taken} damage. Remaining health: {self.health}/{self.max_health}")
        if self.health <= 0:
            self.die()

    # Handles character death.
    def die(self):
        print(f"{self.name} has died.")

    # Handles the max health variable (since there are some instances that health does not equal to max health before, so this function was made).
    def update_character(self):
        self.max_health = self.health

    # Handles particular item blessings.
    def implement_blessing(self):
        if self.inventory.has_item("SLIME HELMET"):
            self.health += 50
        return self.health

    # Handles particular item blessings.
    def implement_curse(self):
        if self.inventory.has_item("IRON GAUNTLETS"):
            self.health += 50
        return self.health

    # Will return if called
    def __str__(self):
        return (
            f"Name: {self.name}, Path: {self.path()}, Level: {self.level}, "
            f"Health: {self.health}/{self.max_health}, Attack: {self.attack}, Defense: {self.defense}"
        )

def display_character_status(character):
    # Displays the character's status.
    print(f"Name: {character.name}, Path: {character.path()}, Level: {character.level}, ")
    print(f"Health: {character.health}/{character.max_health}, Attack: {character.attack}, Defense: {character.defense}")

    # Display inventory
    print("\n--- Inventory ---")
    character.inventory.display_inventory()

    # Display skills
    print("\n--- Skills ---")
    character.skills.display_skills()