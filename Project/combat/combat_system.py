# Module/Imports/Libraries
import sys
import os
import random
import time
from nltk.corpus import words
from Project.util.character import Inventory

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ANSI color codes for terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Initialize inventory
items = Inventory()

# Valid words variable
VALID_WORDS = set(words.words())

def health_bar(current, max_health, bar_length=20):
    """Generates a health bar string."""
    filled_bar = int(current / max_health * bar_length)
    bar = "█" * filled_bar + "-" * (bar_length - filled_bar)
    return f"[{bar}] {current}/{max_health}"

def calculate_damage(word, character, enemy):
    """Calculate damage based on word length, character's attack, skills, and critical hits."""
    base_damage = len(word) + character.attack
    bonus_damage = 0
    critical_hit = False

    # Skill based bonuses
    if character.inventory.has_item("SWORD OF LIGHT"):
        bonus_damage += 20

    if character.inventory.has_item("BOW OF CHAOS"):
        bonus_damage += 20

    if character.inventory.has_item("FLAME SWORD") or character.inventory.has_item("SHADOW BLADE"):
        bonus_damage += 30

    if character.skills.get_skill("BLESSING OF ARCANUS") or character.skills.get_skill("BLESSING OF SATURNUS"):
        path_blessing = character.skills.get_skill("BLESSING OF ARCANUS") or character.skills.get_skill("BLESSING OF SATURNUS")
        bonus_damage += 5 * path_blessing.level

    # Critical Hit Chance
    critical_skill = character.skills.get_skill("CRITICAL EYE") or character.skills.get_skill("DARK VISION")
    if critical_skill:
        critical_chance = critical_skill.level # Get the level of the skill
    else:
        critical_chance = 0

    if random.random() < critical_chance * 0.01:
        critical_hit = True
        bonus_damage = (base_damage + bonus_damage) * 2 # Apply multiplier to base damage also
        print(f"{CYAN}Critical hit!{RESET}")
    damage = base_damage + bonus_damage
    return damage, critical_hit

def display_letter_pool(letter_pool):
    """Display the letter pool in a 4x4 grid format."""
    print("\nYour letters:")
    for i in range(0, 16, 4):
        print(" ".join(letter_pool[i:i + 4]))

def display_combat_header(character, enemy, round_counter):
    print("-" * 40)
    print(f"Round {round_counter}/20")
    print(f"{character.name}'s Health: {health_bar(character.health, character.max_health)}")
    print(f"{enemy.name} the {enemy.race}'s Health: {health_bar(enemy.health, enemy.max_health)}")
    print("-" * 40)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class CombatManager:
    def __init__(self, character):
        self.character = character

    def _player_turn(self, enemy, letter_pool):
        while True:
            try:
                print("\nForm a word to attack! (Type 'pass' to skip):")
                player_word = input("> ").strip().lower()
                print(" ")
                if player_word == "pass":
                    print("You skipped your turn!")
                    return True
                elif all(player_word.count(char) <= letter_pool.count(char) for char in
                         player_word) and player_word in VALID_WORDS:
                    damage, critical_hit = calculate_damage(player_word, self.character, enemy)
                    damage_color = RED if critical_hit else YELLOW
                    print(f"You attack with '{player_word}' for {damage_color}{damage}{RESET} damage!")
                    enemy.take_damage(damage)
                    return True
                else:
                    print("Invalid word! Please try again.")
            except EOFError:
                print("\nCombat ended due to input interruption.")
                return False
            except Exception as e:
                print(f"An error occurred: {e}")
                return False

    def _enemy_turn(self, enemy):
        if enemy.health > 0:
            enemy_damage = enemy.attack_target(self.character)
            if enemy_damage > 0:
                print(f"{enemy.name} attacks for {RED}{enemy_damage}{RESET} damage!")
            else:
                print(f"{enemy.name} attacks but does no damage!")

    def _check_combat_end(self, enemy, round_counter):
        if self.character.health <= 0:
            print(f"\n{self.character.name} was defeated... The {enemy.name} the {enemy.race} stands victorious!")
            return "player_lose"
        elif enemy.health <= 0:
            print(f"\n{self.character.name} defeated the {enemy.name} the {enemy.race}! Victory!")
            return "player_win"
        elif round_counter > 20:
            print("\nThe battle has ended in a draw due to time limits!")
            return "draw"
        return None

    def combat_system(self, enemy):
        """Combat system where player forms words to attack."""
        print(f"A wild {enemy.race} named {enemy.name} appears!")
        print(f"{enemy.name}'s Stats: {enemy}")
        round_counter = 1

        while self.character.health > 0 and enemy.health > 0:
            display_combat_header(self.character, enemy, round_counter)
            # Generate random letters for the player
            letter_pool = [random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(16)]
            display_letter_pool(letter_pool)

            if not self._player_turn(enemy, letter_pool):
                break

            if enemy.health > 0:
                self._enemy_turn(enemy)

            time.sleep(3)
            clear_screen()

            round_counter += 1
            result = self._check_combat_end(enemy, round_counter)
            if result:
                break
        return result