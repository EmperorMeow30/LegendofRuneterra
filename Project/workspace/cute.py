# import sys
# import os
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#
# from Project.story.hero_path import hero_story
# from Project.util.character import Character, display_character_status
# from Project.combat.combat_system import CombatManager
# from Project.combat.hero_path.enemies import Slime, Orc, OrcKing
# from Project.util.progress import Progress
#
# # Create a character instance
# person = Character(name="Austin")
# slime = Slime(name="Guss", level=1)
# orc = Orc(name="Patrick", level=1)
# orc_king = OrcKing(name="Austley", level=1)
# progress = Progress()
#
# combat_manager = CombatManager(person)
#
# person.level = 1
# person.implement_blessing()
# person.skills.add_skill("CRITICAL EYE")
# person.skills.level_up_skill("CRITICAL EYE")
# person.update_character()
# # magical_loading_screen()
# #hero_story.loader()