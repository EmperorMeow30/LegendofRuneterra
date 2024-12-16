# Module/Imports/Libraries
import json
from Project.util.variable_handler import person

# Progress class
class Progress:
    # Sets the booleans to False as a default
    is_prelude_completed = False
    is_chapter_one_completed = False
    is_chapter_two_completed = False
    is_chapter_three_completed = False
    is_chapter_four_completed = False
    is_chapter_five_completed = False
    is_chapter_six_completed = False
    is_chapter_six_half_completed = False
    is_chapter_seven_completed = False

    # A function to save the progress of the game, as well as the character data
    @classmethod
    def save_progress(cls):
        with open("C:\\Users\\Ralph\\PycharmProjects\\Studies\\Project\\database\\progress.json", "w",encoding="utf-8") as f:
            data = {
                "is_prelude_completed": cls.is_prelude_completed,
                "is_chapter_one_completed": cls.is_chapter_one_completed,
                "is_chapter_two_completed": cls.is_chapter_two_completed,
                "is_chapter_three_completed": cls.is_chapter_three_completed,
                "is_chapter_four_completed": cls.is_chapter_four_completed,
                "is_chapter_five_completed": cls.is_chapter_five_completed,
                "is_chapter_six_completed": cls.is_chapter_six_completed,
                "is_chapter_six_half_completed": cls.is_chapter_six_half_completed,
                "is_chapter_seven_completed": cls.is_chapter_seven_completed,
                "character_data": cls.serialize_character(person) if person else None,  # Use the imported 'person'
            }
            json.dump(data, f, ensure_ascii=False, indent=4)

    # A function to load the progress of the game, as well as the character data
    @classmethod
    def load_progress(cls):
        try:
            with open("C:\\Users\\Ralph\\PycharmProjects\\Studies\\Project\\database\\progress.json", "r",encoding="utf-8") as f:
                data = json.load(f)
                cls.is_prelude_completed = data.get("is_prelude_completed", False)
                cls.is_chapter_one_completed = data.get("is_chapter_one_completed", False)
                cls.is_chapter_two_completed = data.get("is_chapter_two_completed", False)
                cls.is_chapter_three_completed = data.get("is_chapter_three_completed", False)
                cls.is_chapter_four_completed = data.get("is_chapter_four_completed", False)
                cls.is_chapter_five_completed = data.get("is_chapter_five_completed", False)
                cls.is_chapter_six_completed = data.get("is_chapter_six_completed", False)
                cls.is_chapter_six_half_completed = data.get("is_chapter_six_half_completed", False)
                cls.is_chapter_seven_completed = data.get("is_chapter_seven_completed", False)
                character_data = data.get("character_data")  # Load character data
                if character_data:
                   cls.deserialize_character(character_data, person)

        # Error handling if there is no progress.json file, it will set everything to False (default)
        except FileNotFoundError:
            cls.is_prelude_completed = False
            cls.is_chapter_one_completed = False
            cls.is_chapter_two_completed = False
            cls.is_chapter_three_completed = False
            cls.is_chapter_four_completed = False
            cls.is_chapter_five_completed = False
            cls.is_chapter_six_completed = False
            cls.is_chapter_six_half_completed = False
            cls.is_chapter_seven_completed = False

    # Converts character data object into a dictionary
    @classmethod
    def serialize_character(cls, character):
        if not character:
            return None

        return {
            "name": character.get_name(),
            "isHero": character.isHero,
            "isEvil": character.isEvil,
            "isNeutral": character.isNeutral,
            "level": character.level,
            "experience": character.experience,
            "health": character.health,
            "max_health": character.max_health,
            "attack": character.attack,
            "defense": character.defense,
            "inventory": character.inventory.items,
            "skills": {name: skill.__dict__ for name, skill in character.skills.skills.items()}
        }

    # Gets the data of Character from a dictionary.
    @classmethod
    def deserialize_character(cls, data, character):
        if not data:
            return None

        person.name = data.get("name", "")
        character.isHero = data.get("isHero", False)
        character.isEvil = data.get("isEvil", False)
        character.isNeutral = data.get("isNeutral", False)
        character.level = data.get("level", 1)
        character.experience = data.get("experience", 0)
        character.health = data.get("health", 100)
        character.max_health = data.get("max_health", 100)
        character.attack = data.get("attack", 10)
        character.defense = data.get("defense", 3)
        character.inventory.items = data.get("inventory", {})

        skills_data = data.get("skills", {})
        for name, skill_data in skills_data.items():
            skill = character.skills.add_skill(name)
            if skill:
                skill.level = skill_data.get('level', 1)
        return character