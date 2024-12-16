# Module/Imports/Libraries
from Project.combat.combat_system import CombatManager
from Project.util import utilities
from Project.util.character import display_character_status
from Project.util.progress_system import Progress
from Project.util.variable_handler import person, warrior, giant, giant_king, angelic_guard, elise_angel, elise_seraphim
from Project.util.background_music import play_music_in_background

# Initialization of combat system and music path
combat_manager = CombatManager(person)
music_path = "C:\\Users\\Ralph\\PycharmProjects\\Studies\\Project\\util\\sound_effects\\villain_background.mp3"

# Function to keep player accessing chapters if they haven't finished the previous chapter
def loader():
    # Also plays music in the background for immersion
    utilities.Clear()
    print("Loading Game...")
    play_music_in_background(music_path)
    utilities.Pause(2)

    chapter_functions = {
        1: chapter_one,
        2: chapter_two,
        3: chapter_three,
        4: chapter_four,
        5: chapter_five,
        6: chapter_six,
        6.5: chapter_six_point_five,
        7: chapter_seven
    }

    progress_flags = {
        1: Progress.is_chapter_one_completed,
        2: Progress.is_chapter_two_completed,
        3: Progress.is_chapter_three_completed,
        4: Progress.is_chapter_four_completed,
        5: Progress.is_chapter_five_completed,
        6: Progress.is_chapter_six_completed,
        6.5: Progress.is_chapter_six_half_completed,
        7: Progress.is_chapter_seven_completed
    }

    if all(flag is False for flag in progress_flags.values()):
        chapter_functions[1]()  # Start with chapter one if no progress
        return

    while True:
        utilities.Clear()
        print("Select the Chapter you wish to play:")
        for chapter_num in range(1, 8):
            if chapter_num in chapter_functions:
                chapter_name = chapter_functions[chapter_num].__name__.replace("_", " ").title()
                completion_status = "Complete" if progress_flags.get(chapter_num, False) else "Locked"
                print(f"({chapter_num}) {chapter_name} - {completion_status}")
        print("\n(0) Back to Title Screen")

        choice = utilities.typingInput("> ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                utilities.title_screen()
                return
            elif choice in chapter_functions:
                if choice == 1 or progress_flags.get(choice - 1,False) or choice == 6.5 or choice == 7:  # Allow chapter 1 always or if previous is complete
                    utilities.Clear()
                    if not progress_flags.get(choice, False):
                        print(f"Starting {chapter_functions[choice].__name__.replace('_', ' ').title()}...")
                    else:
                        print(f"Reliving {chapter_functions[choice].__name__.replace('_', ' ').title()}...")
                    utilities.Pause(3)
                    chapter_functions[choice]()
                    return  # Only start a new chapter, and return after that
                else:
                    utilities.typingPrint("You must complete the previous chapter to access this one")
                    utilities.Pause(3)
            else:
                utilities.typingPrint("Invalid choice. Please try again.")
                utilities.Pause(3)
        else:
            utilities.typingPrint("Invalid input. Please enter a number.")
            utilities.Pause(3)

# Chapter one of the story
def chapter_one():
    chapter = "EMBRACING THE SHADOWS"

    # Message list
    messages = [
        "**Narrator:** Runeterra, a world of magic and conflict, where the balance of light and darkness is constantly challenged.",
        "**Narrator:** The Faction of Light, led by the benevolent Lord Arcanus, strives for harmony, while the Faction of Darkness, under the command of the enigmatic Lord Saturnus, seeks to reshape reality itself.",
        "**Narrator:** You, a soul with untapped potential, are about to embark on a path that will change the fate of the realms.",
        lambda: f"**{person.get_name()}:** (You reflect on the chaos that plagues this world) The light offers only stagnation, their 'peace' is a cage. Saturnus's vision...it speaks to the ambition within me.",
        "**Narrator:** A figure shrouded in dark robes appears before you. It is Malachi, a devoted servant of Lord Saturnus.",
        lambda: f"**Malachi:** {person.get_name()}, Lord Saturnus has taken notice of your unique power, your potential to reshape this world. He invites you to join us in the Infernal Realm.",
        lambda: f"**{person.get_name()}:** Saturnus's invitation... I've been waiting for this. To embrace the darkness, to challenge the status quo... it is my purpose.",
        lambda: f"**Malachi:** Your strength is not a curse, but a gift. You can use that power to shape the world as you desire.",
        lambda: f"**{person.get_name()}:** Tell me, Malachi... What do I need to do?",
    ]

    # This is a function that will iterate each message in the messages list
    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")
        # If the message is present in the first message list, execute another list in the form of dialogues
        if message == f"**{person.get_name()}:** Tell me, Malachi... What do I need to do?":
            dialogues = [
                lambda: f"**Narrator:** Malachi smiles, his eyes gleaming with a dark delight.",
                "**Narrator:** Malachi leads you to the depths of the forest.",
                "**Narrator:** Suddenly, a brave warrior appears!",
                "**Brave Warrior:** You! You are joining the darkness, aren't you? You will not get away with this!",
                lambda: f"**{person.get_name()} (inner monologue):** Such righteous foolishness. You will get what you deserve.",
            ]

            # This is a function that will iterate each dialogue in the dialogues list
            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                # If the message is present in the second message list, execute choices
                if dialogue == f"**{person.get_name()} (inner monologue):** Such righteous foolishness. You will get what you deserve.":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to reason with the warrior\n(b) Draw your weapon and fight!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        # Option A: Will converse with the enemy
                        if choice == "a":
                            conversations = [
                                "**Narrator:** You attempt to explain your reasons to the warrior.",
                                lambda: f"**{person.get_name()}:** I choose the path of power. Lord Saturnus has given me the potential to change this stagnant world.",
                                "**Malachi:** You can't reason with these righteous fools. They believe their 'light' is the only way, even if it leads to stagnation.",
                                "**Brave Warrior:** Your vision is tainted by darkness! You are succumbing to evil!",
                                lambda: f"**{person.get_name()}:** The 'light' you so zealously follow is a mere shackle! I will forge my own path!",
                                "**Narrator:** The warrior attacks you because you would not listen.",
                                lambda: f"**Malachi:** (Sighs) Seems like you have to teach him a lesson.",
                            ]

                            for k, conversation in enumerate(conversations):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(conversation)
                                print(" ")

                            # Adds items and level up skills
                            print(" ")
                            combat_manager.combat_system(warrior)
                            person.inventory.add_item("IRON GAUNTLETS", 1)
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.implement_curse()
                            person.update_character()

                            while True:
                                # Asks the user if they still wanted to continue adventure
                                utilities.Space()
                                Progress.is_chapter_one_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    utilities.LongPause()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_two()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    # Error Handling
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                            break
                        # Option B: Will fight with the enemy
                        elif choice == "b":
                            panels = [
                                "**Narrator:** You draw your weapon, assuming a battle stance against the warrior.",
                                "**Narrator:** This is your first taste of combat in this adventure.",
                                "**Narrator:** Combat is turn-based. You and your foes take turns attacking.",
                                "**Narrator:** Spell words correctly to unleash your attacks."
                            ]

                            for l, panel in enumerate(panels):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(panel)
                                print(" ")

                            # Combat System
                            utilities.Space()
                            utilities.magical_loading_screen()
                            utilities.LongPause()
                            person.update_character()
                            combat_manager.combat_system(warrior)
                            utilities.typingPrint(f"**Narrator:** You find a Iron Gauntlets on the fallen warrior and pick it up.")
                            person.gain_experience(100)
                            print(" ")
                            # Add an item and level up the skill
                            person.inventory.add_item("IRON GAUNTLETS", 1)
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.implement_curse()

                            while True:
                                # Asks the user if they still wanted to continue adventure
                                utilities.Space()
                                Progress.is_chapter_one_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_two()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                            break
                        else:
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")
                            utilities.typingPrint("You must make a choice. Please try again...")
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")

# Chapter two of the story
def chapter_two():
    chapter = "THE DARK PROPHECY"

    messages = [
        lambda: f"**Narrator:** You and Malachi reach the Infernal Realm shortly...",
        "**Narrator:** You are greeted by none other than Lord Saturnus, himself.",
        lambda: f"**Lord Saturnus:** Welcome, {person.get_name()}. I have eagerly awaited your arrival.",
        lambda: f"**Lord Saturnus:** I have seen your potential, the hunger for power, and the potential to break the chains of this world.",
        lambda: f"**Lord Saturnus:** There is a prophecy about you, Dark One. And it is the reason why you are here...",
        lambda: f"**Saturnus's Voice:** A shadow will rise, challenging the order of the light. The embodiment of chaos shall commit an act of rebellion, proving that free will is superior to the light's stagnancy. He will have to chose between his true destiny and his fear of the unknown.",
        "**Narrator:** The prophecy is filled with promise, and ambition. You feel a surge of power rushing through your veins...",
        lambda: f"**Malachi:** My Lord, has the Infernal Guild devised any interpretations for this new, ominous prophecy?",
        lambda: f"**Lord Saturnus:** Not yet, but I trust {person.get_name()} will fulfill this prophecy. For now, I offer you my blessings.",
        lambda: f"**{person.get_name()}:** Thank you, Lord Saturnus. I will not disappoint you!",
    ]

    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")

        if message == f"**{person.get_name()}:** Thank you, Lord Saturnus. I will not disappoint you!":
            dialogues = [
                lambda: f"**Narrator:** You and Malachi explore the Infernal Realm a bit.",
                lambda: f"**Narrator:** Suddenly, you hear a report of a disturbance.",
                "**Infernal Citizen:** The supply team is being attacked! I beg of you, my lord, please help!",
                "**Malachi:** My Lord, calm yourself and explain the situation clearly...",
                "**Infernal Citizen:** We were ambushed by a group of Giants while transporting food. I barely escaped! The other members are still there!",
                lambda: f"**Lord Saturnus:** {person.get_name()} and Malachi, this is the perfect opportunity to test the limits of your powers.",
                lambda: f"**Lord Saturnus:** I will cast a powerful spell, teleporting you both to the supply team.",
                lambda: f"**Lord Saturnus:** And take these blessings, {person.get_name()}. You will need them.",
            ]

            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                if dialogue == f"**Lord Saturnus:** And take these blessings, {person.get_name()}. You will need them.":
                    person.gain_experience(200)
                    person.skills.level_up_skill("BLESSING OF SATURNUS")

                while True:
                    utilities.Space()
                    Progress.is_chapter_two_completed = True
                    utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                    utilities.typingPrint("\n(a) Yes\n(b) No")
                    utilities.Space()
                    choice = input("\n> ").lower()
                    if choice == "a":
                        # Mark Chapter Two as complete
                        utilities.Clear()
                        print(f"**{chapter}**")
                        Progress.save_progress()
                        utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                        utilities.Pause(3)
                        utilities.Clear()
                        print(f"**{chapter}**")
                        utilities.magical_loading_screen()
                        display_character_status(person)
                        utilities.Pause(3)
                        chapter_three()
                        break
                    elif choice == "b":
                        # Mark Chapter as complete
                        utilities.Clear()
                        print(f"**{chapter}**")
                        Progress.save_progress()
                        utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                        utilities.Space()
                        utilities.typingPrint("You will be returned to the title screen shortly...")
                        utilities.Pause(3)
                        utilities.title_screen()
                        break
                    else:
                        utilities.LongPause()
                        utilities.Clear()
                        print(f"**{chapter}**")
                        print(" ")
                        utilities.typingPrint("You must make a choice. Please try again...")
                        utilities.LongPause()
                        utilities.Clear()
                        print(f"**{chapter}**")
                        print(" ")

# Chapter three of the story
def chapter_three():
    chapter = "A CLASH OF GIANTS"

    messages = [
        lambda: f"**Narrator:** You and Malachi are instantly teleported to the chaotic scene.",
        "**Giant King:** What sorcery is this?! How did you arrive here so suddenly?",
        "**Giant King:** Enough talk! I shall crush you! Attack them!",
        lambda: f"**{person.get_name()}:** Malachi, step aside! I shall deal with these giants.",
    ]

    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")

        if message == f"**{person.get_name()}:** Malachi, step aside! I shall deal with these giants.":
            dialogues = [
                lambda: f"**Narrator:** {person.get_name()}, this is another form of battle you will have to experience. In this game, you are bound to be victorious, right?",
                "**Narrator:** Not anymore. This will be challenging. Good luck dealing with a multitude of enemies.",
                "**Narrator:** A ferocious group of giants, led by their King, emerge to confront you!",
                "**Giant King:** You puny humans will be our dinner today!",
            ]

            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                if dialogue == "**Giant King:** You puny humans will be our dinner today!":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to reason with the Giant King\n(b) Engage the Giants in battle!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        if choice == "a":
                            conversations = [
                                lambda: f"**{person.get_name()}:** I do not want any bloodshed. Stand down, and I'll spare your lives.",
                                "**Giant King:** You think you are strong enough to dictate what we should do, human?! You are merely a grain of sand against us!",
                                "**Giant King (to his minions):** Grab the dark mage! Use him as a bait to taunt the kid!",
                                "**Narrator:** The Giants seize Malachi, injuring him in the process!",
                                lambda: f"**{person.get_name()}:** You will regret this! I swear on my name!",
                            ]

                            for k, conversation in enumerate(conversations):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(conversation)
                                print(" ")

                            utilities.Space()
                            utilities.magical_loading_screen()
                            utilities.LongPause()
                            person.update_character()
                            combat_manager.combat_system(giant)
                            combat_manager.combat_system(giant_king)
                            person.gain_experience(600)
                            print(" ")
                            person.skills.add_skill("DARK VISION")
                            person.skills.level_up_skill("BLESSING OF SATURNUS")

                            while True:
                                utilities.Space()
                                Progress.is_chapter_three_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    utilities.LongPause()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_four()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                            break
                        elif choice == "b":
                            panels = [
                                lambda: f"**Narrator:** You wield your weapon, ready to face the giants in battle.",
                                "**Narrator:** The Giant King, in a desperate act, throws a strange blast of energy at Malachi, knocking him down.",
                                lambda: f"**{person.get_name()}:** This ends now! I will make you pay!"
                            ]

                            for l, panel in enumerate(panels):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(panel)
                                print(" ")

                            # Combat System
                            utilities.Space()
                            utilities.magical_loading_screen()
                            utilities.LongPause()
                            person.update_character()
                            combat_manager.combat_system(giant)
                            combat_manager.combat_system(giant_king)
                            person.gain_experience(600)
                            print(" ")
                            person.skills.add_skill("DARK VISION")
                            person.skills.level_up_skill("BLESSING OF SATURNUS")

                            while True:
                                utilities.Space()
                                Progress.is_chapter_three_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_four()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                            break
                        else:
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")
                            utilities.typingPrint("You must make a choice. Please try again...")
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")

# Chapter four of the story
def chapter_four():
    chapter = "A BETRAYAL OF FAITH"

    messages = [
        "**Narrator:** The battle concludes, the Giants are defeated. Malachi is severely injured.",
        "**Narrator:** A week has passed...",
        lambda: f"**Narrator:** {person.get_name()} reports back to Lord Saturnus.",
        lambda: f"**Lord Saturnus:** Greetings {person.get_name()}. Malachi seems to be recovering, but the council has discovered some concerning leads regarding Lord Arcanus and his plans.",
        lambda: f"**{person.get_name()}:** Lord Arcanus? Was he behind the ambush?",
        "**Lord Saturnus:** Not directly, but there are suspicious connections between him and those giants.",
        "**Lord Saturnus:** The weapons they wield are not from our realm. They are of divine origin.",
        lambda: f"**{person.get_name()}:** Divine origin? This is getting more complicated.",
        "**Lord Saturnus:** Indeed, and for that, I ask you to infiltrate the Light Realm. We must discover the full extent of their treacherous plans.",
        lambda: f"**{person.get_name()}:** How am I to enter the Light Realm if I am affiliated with the Faction of Darkness?",
        "**Lord Saturnus:** Through teleportation, as before. This time you will need this amulet.",
        lambda: f"**Narrator:** You receive the [AMULET OF SHROUD] from Lord Saturnus.",
        "**Lord Saturnus:** It will aid in masking your true identity within the Light Realm. However, you must avoid direct contact with Lord Arcanus or his followers lest they uncover your true nature.",
        lambda: f"**{person.get_name()}:** Understood, My Lord. I shall be vigilant.",
    ]

    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")

        if message == f"**{person.get_name()}:** Understood, My Lord. I shall be vigilant.":
            dialogues = [
                lambda: f"**Narrator:** Once again, Lord Saturnus's power transports {person.get_name()} to the outskirts of the Light Realm.",
                f"**Narrator:** A few details about the realm of light...",
                f"**Narrator:** Ruled by Lord Arcanus, the God of Light and twin brother of Saturnus. It is a realm where those who seek peace and order reside.",
                f"**Narrator:** It also houses the 'Celestial Order', a group known for its zealous devotion to the light and their rigid enforcement of its laws.",
                lambda: f"**{person.get_name()}:** Such a pristine place. Those who lived here must be so naive.",
                "**Narrator:** Before you stands the main gate of the Light Realm. Guards are checking each visitor's identification.",
                "**Narrator:** The line is long, so you have to wait. You decided to keep silent as they chattered...",
                "**Guard 1:** Have you heard about what happened to Raphael recently?",
                "**Guard 2:** Yes, it seems that he was reprimanded by His Majesty. It seems that he was too careless in torturing the prisoner.",
                "**Guard 3:** I heard that Raphael was the one who controlled the Giant King to intercept the supply mission of the Infernal Guild.",
                "**Guard 2:** Well, nothing to expect. That kid destroyed the Infernal Realm completely. He seems to be poised to become His Majesty's successor.",
                "**Guard 1:** Probably after he eliminates the so-called 'Dark One' of the Faction of Darkness.",
                "**Guard 3:** Right, that 'Dark One' will never win against Raphael in his entire lifetime.",
                lambda: f"**{person.get_name()}:** 'Raphael'... Who is that person they speak of?",
            ]

            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                if dialogue == f"**{person.get_name()}:** 'Raphael'... Who is that person they speak of?":
                    person.gain_experience(1000)
                    print(" ")
                    person.skills.add_skill("DARK VISION")
                    person.skills.level_up_skill("BLESSING OF SATURNUS")

                while True:
                    utilities.Space()
                    Progress.is_chapter_four_completed = True
                    utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                    utilities.typingPrint("\n(a) Yes\n(b) No")
                    utilities.Space()
                    choice = input("\n> ").lower()
                    if choice == "a":
                        # Mark Chapter Two as complete
                        utilities.Clear()
                        print(f"**{chapter}**")
                        Progress.save_progress()
                        utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                        utilities.Pause(3)
                        utilities.Clear()
                        print(f"**{chapter}**")
                        utilities.magical_loading_screen()
                        display_character_status(person)
                        utilities.Pause(3)
                        chapter_five()
                        break
                    elif choice == "b":
                        # Mark Chapter as complete
                        utilities.Clear()
                        print(f"**{chapter}**")
                        Progress.save_progress()
                        utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                        utilities.Space()
                        utilities.typingPrint("You will be returned to the title screen shortly...")
                        utilities.Pause(3)
                        utilities.title_screen()
                        break
                    else:
                        utilities.LongPause()
                        utilities.Clear()
                        print(f"**{chapter}**")
                        print(" ")
                        utilities.typingPrint("You must make a choice. Please try again...")
                        utilities.LongPause()
                        utilities.Clear()
                        print(f"**{chapter}**")

                        print(" ")

# Chapter five of the story
def chapter_five():
    chapter = "A DIVINE INTERCEPTION"

    messages = [
        "**Narrator:** As you proceed further into the Light Realm, the serene atmosphere is broken by a sudden shout.",
        "**Angelic Guard:** Intruder! Halt!",
        "**Angelic Guard:** You don't belong here. Prepare to be punished!",
        lambda: f"**{person.get_name()}:** Damn, I was too careless...",
    ]

    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")

        if message == f"**{person.get_name()}:** Damn, I was too careless...":
            dialogues = [
                "**Narrator:** The Angelic Guards, clad in bright armor, converge on your location.",
                "**Narrator:** Their eyes glow with righteous fury.",
                "**Narrator:** It is time for another battle. These guys are stronger than your average giants.",
            ]

            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                if dialogue == "**Narrator:** It is time for another battle. These guys are stronger than your average giants.":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to flee\n(b) Stand your ground and fight!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        if choice == "a":
                            conversations = [
                                "**Narrator:** You attempt to evade the guards, but they are too quick, and they managed to grab you.",
                                "**Angelic Guard:** You can't run from the justice of the Light Realm!",
                                lambda: f"**{person.get_name()}:** I guess, I have no choice but to fight.",
                            ]

                            for k, conversation in enumerate(conversations):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(conversation)
                                print(" ")

                            utilities.Space()
                            utilities.magical_loading_screen()
                            utilities.LongPause()
                            person.update_character()
                            combat_manager.combat_system(angelic_guard)
                            combat_manager.combat_system(angelic_guard)
                            person.gain_experience(1200)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.skills.level_up_skill("DARK VISION")
                            if "SHADOW BLADE" not in person.inventory.items:
                                person.inventory.add_item("SHADOW BLADE", 1)
                            person.update_character()

                            while True:
                                utilities.Space()
                                Progress.is_chapter_five_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    utilities.LongPause()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_six()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                            break
                        elif choice == "b":
                            panels = [
                                "**Narrator:** You unsheathe your weapon, ready to face the Angelic Guards.",
                                "**Narrator:** These guards are more dangerous than any foes you've faced so far.",
                                "**Narrator:** Be careful, and good luck!",
                            ]

                            for l, panel in enumerate(panels):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(panel)
                                print(" ")

                            # Combat System
                            utilities.Space()
                            utilities.magical_loading_screen()
                            utilities.LongPause()
                            person.update_character()
                            combat_manager.combat_system(angelic_guard)
                            combat_manager.combat_system(angelic_guard)
                            person.gain_experience(1200)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.skills.level_up_skill("DARK VISION")
                            if "SHADOW BLADE" not in person.inventory.items:
                                person.inventory.add_item("SHADOW BLADE", 1)
                            person.update_character()

                            while True:
                                utilities.Space()
                                Progress.is_chapter_five_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    utilities.LongPause()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_six()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                            break
                        else:
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")
                            utilities.typingPrint("You must make a choice. Please try again...")
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")

# Chapter six of the story
def chapter_six():
    chapter = "HOLY CONFINEMENT"

    messages = [
        "**Narrator:** The Angelic Guards lie defeated, but before you can fully assess your surroundings, a divine energy envelops you.",
        "**Narrator:** You collapse to the ground, your vision fading into blackness.",
        "**Narrator:** You awaken in a bright, sterile cell. The smell of incense fills your nostrils. You are in the 'Temple of Light'.",
        lambda: f"**{person.get_name()}:** What happened...how did they capture me?",
        lambda: f"**{person.get_name()}:** Wait... I have the Amulet of Shroud, right? How could they have identified me?",
    ]

    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")

        if message == f"**{person.get_name()}:** Wait... I have the Amulet of Shroud, right? How could they have identified me?":
            dialogues = [
                "**Narrator:** You examine your cell. It's spacious, made of smooth white stone. No windows, just a heavy, ornate door.",
                lambda: f"**{person.get_name()}:** This is bad, very bad. I have to find a way to escape this prison.",
                "**Narrator:** You decide to survey the area a bit. You find a loose tile.",
                lambda: f"**{person.get_name()}:** Finally, a chance to escape!",
            ]

            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                if dialogue == f"**{person.get_name()}:** Finally, a chance to escape!":
                    while True:
                        utilities.Space()
                        Progress.is_chapter_six_completed = True
                        utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                        utilities.typingPrint("\n(a) Yes\n(b) No")
                        utilities.Space()
                        choice = input("\n> ").lower()
                        if choice == "a":
                            # Mark Chapter as complete
                            utilities.Clear()
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.skills.level_up_skill("DARK VISION")
                            print(f"**{chapter}**")
                            Progress.save_progress()
                            utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                            utilities.Pause(3)
                            utilities.Clear()
                            print(f"**{chapter}**")
                            utilities.magical_loading_screen()
                            display_character_status(person)
                            utilities.Pause(3)
                            chapter_six_point_five()
                            break
                        elif choice == "b":
                            # Mark Chapter as complete
                            utilities.Clear()
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.skills.level_up_skill("DARK VISION")
                            print(f"**{chapter}**")
                            Progress.save_progress()
                            utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                            utilities.Space()
                            utilities.typingPrint("You will be returned to the title screen shortly...")
                            utilities.Pause(3)
                            utilities.title_screen()
                            break
                        else:
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")
                            utilities.typingPrint("You must make a choice. Please try again...")
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")

# Chapter six (part 2) of the story
def chapter_six_point_five():
    chapter = "AN UNEXPECTED ENCOUNTER"

    messages = [
        "**Narrator:** You manage to pry the tile loose and discover a hidden passage.",
        "**Narrator:** After a series of twists and turns, you emerge outside the prison.",
        "**Narrator:** You are once again met with the pure, yet stifling atmosphere of the Light Realm.",
        lambda: f"**Narrator:** But someone is standing in front of you, it is a familiar face... the hooded figure mentioned in Chapter 4.",
        lambda: f"**Elise:** Well, well... if it isn't the 'Dark One' who loves to disrupt our peace.",
    ]

    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")

        if message == f"**Elise:** Well, well... if it isn't the 'Dark One' who loves to disrupt our peace.":
            dialogues = [
                "**Narrator:** The person before you removes their hood, revealing a bright, serene face.",
                "**Narrator:** It is Elise, the Light Realm's rising star, and the orchestrator of all your troubles.",
                lambda: f"**{person.get_name()}:** So, you are the one behind the ambush and everything else... How did you see through my disguise?",
                "**Elise:** That amulet...it's just a child's trinket! I can see through your disguise like it's an open book.",
                "**Elise:** Enough chit-chat! You will repent before me.",
            ]

            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                if dialogue == "**Elise:** Enough chit-chat! You will repent before me.":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to reason with Elise\n(b) Prepare for battle against Elise!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        if choice == "a":
                            conversations = [
                                lambda: f"**{person.get_name()}:** Why are you doing this, Elise? We are not enemies by default.",
                                "**Elise:** Fool! I strive for peace and order, and you, with the Faction of Darkness, are against my very existence!",
                                "**Elise:** Now, let's end this meaningless conversation... Fight me if you dare, or kneel before the Light!",
                            ]

                            for k, conversation in enumerate(conversations):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(conversation)
                                print(" ")

                            utilities.Space()
                            utilities.magical_loading_screen()
                            utilities.LongPause()
                            person.update_character()
                            combat_manager.combat_system(elise_angel)
                            person.gain_experience(1500)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.skills.level_up_skill("DARK VISION")

                            while True:
                                utilities.Space()
                                Progress.is_chapter_six_half_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    utilities.LongPause()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_seven()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                            break
                        elif choice == "b":
                            panels = [
                                "**Narrator:** You prepare your weapon, ready to confront Elise.",
                                "**Narrator:** Her divine aura intensifies, it's time for another test of your skills.",
                                "**Narrator:** Fight, Dark One! Fight!",
                            ]

                            for l, panel in enumerate(panels):
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint(panel)
                                print(" ")

                            # Combat System
                            utilities.Space()
                            utilities.magical_loading_screen()
                            utilities.LongPause()
                            person.update_character()
                            combat_manager.combat_system(elise_angel)
                            person.gain_experience(1500)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF SATURNUS")
                            person.skills.level_up_skill("DARK VISION")
                            person.update_character()

                            while True:
                                utilities.Space()
                                Progress.is_chapter_six_half_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Dark One?")
                                utilities.typingPrint("\n(a) Yes\n(b) No")
                                utilities.Space()
                                choice = input("\n> ").lower()
                                if choice == "a":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Pause(3)
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    utilities.magical_loading_screen()
                                    display_character_status(person)
                                    utilities.Pause(3)
                                    chapter_seven()
                                    break
                                elif choice == "b":
                                    # Mark Chapter as complete
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    Progress.save_progress()
                                    utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                    utilities.Space()
                                    utilities.typingPrint("You will be returned to the title screen shortly...")
                                    utilities.Pause(3)
                                    utilities.title_screen()
                                    break
                                else:
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                                    print(" ")
                                    utilities.typingPrint("You must make a choice. Please try again...")
                                    utilities.LongPause()
                                    utilities.Clear()
                                    print(f"**{chapter}**")
                        print(" ")

# Chapter seven of the story
def chapter_seven():
    chapter = "THE ASCENSION OF DARKNESS"

    messages = [
        "**Narrator:** You have managed to defeat Elise, but something is happening to her. The divine energy around her twists and intensifies.",
        "**Narrator:** She rises once again, not the Elise you fought moments ago, but something...more powerful.",
        "**Narrator:** The change is dramatic, it reminds you of someone, but you cannot remember who.",
        lambda: f"**Elise (Final Form):** You may have defeated my previous form, Dark One, but now, I shall unleash my true power.",
    ]

    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(f"**{chapter}**")
        print(" ")

        if callable(message):
            message = message()

        utilities.typingPrint(message)
        print(" ")

        if message == f"**Elise (Final Form):** You may have defeated my previous form, Dark One, but now, I shall unleash my true power.":
            dialogues = [
                "**Narrator:** Elise's final form has manifested, it's time for your final battle.",
                "**Narrator:** You have come so far... will you succeed here, or will everything fall apart?",
                "**Narrator:** Fight, Dark One! Fight with everything you have!",
            ]

            for j, dialogue in enumerate(dialogues):
                utilities.LongPause()
                utilities.Clear()
                print(f"**{chapter}**")
                print(" ")

                if callable(dialogue):
                    dialogue = dialogue()

                utilities.typingPrint(dialogue)
                print(" ")

                if dialogue == "**Narrator:** Fight, Dark One! Fight with everything you have!":
                    utilities.Space()
                    utilities.magical_loading_screen()
                    utilities.LongPause()
                    person.update_character()
                    result = combat_manager.combat_system(elise_seraphim)
                    person.gain_experience(3000)
                    print(" ")
                    person.skills.level_up_skill("BLESSING OF SATURNUS")
                    person.skills.level_up_skill("DARK VISION")
                    person.update_character()

                    if result == "victory":
                        conversations = [
                            "**Narrator:** Elise's final form collapses, the divine energy dissipating into the air.",
                            "**Elise:** I... what have I done? I...I remember now...",
                            lambda: f"**{person.get_name()}:** It's over now, Elise.",
                            "**Narrator:** Elise is defeated, and the Light Realm seems to be growing dim and silent.",
                            lambda: f"**Narrator:** However, this is not the end of the story. The chaos and darkness you have unleashed is merely the beginning of this saga.",
                        ]

                        for k, conversation in enumerate(conversations):
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")
                            utilities.typingPrint(conversation)
                            print(" ")

                        while True:
                            utilities.Space()
                            Progress.is_chapter_seven_completed = True
                            utilities.typingPrint(f"**Narrator:** To be continued in Part 2 of the story...")
                            utilities.typingPrint("\n(a) Yes\n(b) No")
                            utilities.Space()
                            choice = input("\n> ").lower()
                            if choice == "a":
                                # Mark Chapter as complete
                                utilities.Clear()
                                print(f"**{chapter}**")
                                Progress.save_progress()
                                utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                utilities.Pause(3)
                                utilities.Clear()
                                print(f"**{chapter}**")
                                utilities.magical_loading_screen()
                                utilities.LongPause()
                                display_character_status(person)
                                utilities.Pause(3)
                                utilities.title_screen()
                                break
                            elif choice == "b":
                                # Mark Chapter as complete
                                utilities.Clear()
                                print(f"**{chapter}**")
                                Progress.save_progress()
                                utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                utilities.Space()
                                utilities.typingPrint("You will be returned to the title screen shortly...")
                                utilities.Pause(3)
                                utilities.title_screen()
                                break
                            else:
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint("You must make a choice. Please try again...")
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                        break
                    elif result == "defeat":
                        conversations = [
                            "**Narrator:** You fall to your knees, exhausted, Elise's final form towering over you.",
                            "**Elise (Final Form):** You have fought bravely, but you were never a match for me, fool!",
                             "**Narrator:** The Light Realm crumbles, as a bright, blinding energy consumes the very essence of the universe.",
                             "**Narrator:** You wake up at the Infernal Realm, Lord Saturnus is there, waiting for you.",
                            lambda: f"**Lord Saturnus:** {person.get_name()}, I saw everything! The realms...are about to collapse! This is not the end...",
                            lambda: f"**Lord Saturnus:** But...you must be stronger, for the coming trials are far worse than you have experienced so far!",
                            lambda: f"**Narrator:** However, this is not the end of the story. The chaos and darkness you have unleashed is merely the beginning of this saga.",
                        ]

                        for k, conversation in enumerate(conversations):
                            utilities.LongPause()
                            utilities.Clear()
                            print(f"**{chapter}**")
                            print(" ")
                            utilities.typingPrint(conversation)
                            print(" ")

                        while True:
                            utilities.Space()
                            Progress.is_chapter_seven_completed = True
                            utilities.typingPrint(f"**Narrator:** To be continued in Part 2 of the story...")
                            utilities.typingPrint("\n(a) Yes\n(b) No")
                            utilities.Space()
                            choice = input("\n> ").lower()
                            if choice == "a":
                                # Mark Chapter as complete
                                utilities.Clear()
                                print(f"**{chapter}**")
                                Progress.save_progress()
                                utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                utilities.Pause(3)
                                utilities.Clear()
                                print(f"**{chapter}**")
                                utilities.magical_loading_screen()
                                utilities.LongPause()
                                display_character_status(person)
                                utilities.Pause(3)
                                utilities.title_screen()
                                break
                            elif choice == "b":
                                # Mark Chapter as complete
                                utilities.Clear()
                                print(f"**{chapter}**")
                                Progress.save_progress()
                                utilities.typingPrint(f"**Narrator:** {utilities.current_chapter()} completed. Progress saved!")
                                utilities.Space()
                                utilities.typingPrint("You will be returned to the title screen shortly...")
                                utilities.Pause(3)
                                utilities.title_screen()
                                break
                            else:
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                                utilities.typingPrint("You must make a choice. Please try again...")
                                utilities.LongPause()
                                utilities.Clear()
                                print(f"**{chapter}**")
                                print(" ")
                        break