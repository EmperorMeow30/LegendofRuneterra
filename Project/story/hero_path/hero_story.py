# Module/Imports/Libraries
import os
from Project.combat.combat_system import CombatManager
from Project.util import utilities
from Project.util.character import display_character_status
from Project.util.progress_system import Progress
from Project.util.variable_handler import person, slime, orc, orc_king, infernal_guard, elise, elise_final
from Project.util.background_music import play_music_in_background

# Initialization of combat system and music path
combat_manager = CombatManager(person)
script_dir = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(script_dir, "sound_effects", "hero_background.mp3")

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
                if choice == 1 or progress_flags.get(choice - 1,
                                                     False) or choice == 6.5 or choice == 7:  # Allow chapter 1 always or if previous is complete
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
    chapter = "A NEW WORLD DAWNS"

    # Message list
    messages = [
        "**Narrator:** The threads of destiny are woven in the vast tapestry of Runeterra...",
        "**Narrator:** Here, where magic echoes through ancient lands, races clash, and mighty beasts roam. Warriors strive for power, rogues seek shadows, and dark forces plot in secret.",
        "**Narrator:** Some embrace the light, bound by justice, while others succumb to the darkness, like the dreaded Demon King, twisted by the influence of Saturnus, the God of Darkness. Now, a new legend is about to be forged.",
        lambda: f"**{person.get_name()}:** (You gaze around, a sense of wonder filling you) This land... it's breathtaking, yet a shadow hangs over it. Can one soul truly make a difference against the likes of Saturnus? I'm grateful for Lord Arcanus's guidance that fateful day, at least.",
        "**Narrator:** A gentle knock echoes at your door. You open it to find Father Austin, a beacon of the Faction of Light.",
        lambda: f"**Father Austin:** Greetings, {person.get_name()}, the prophesied hero. Lord Arcanus has sent urgent tidings. We must hasten to the Church of Light to receive a crucial prophecy.",
        lambda: f"**{person.get_name()}:** A new prophecy? Is it linked to the one I carry, or is it something more...ominous?",
        lambda: f"**Father Austin:** Indeed. Whenever the Lord Arcanus sends forth a new prophecy, a darkness stirs within the Church. Your presence, {person.get_name()}, is our only hope to stand against it.",
        lambda: f"**{person.get_name()}:** Fear not, Father. Lead the way. I shall escort you to the Church.",
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
        if message == f"**{person.get_name()}:** Fear not, Father. Lead the way. I shall escort you to the Church.":
            dialogues = [
                lambda: f"**Narrator:** You and Father Austin leave the tavern, setting out towards the Church of Light.",
                "**Narrator:** Your journey is cut short, however...",
                "**Narrator:** An enraged slime oozes into your path!",
                "**Angry Slime:** You! You're the one who destroyed my village! Prepare to face my wrath!",
                lambda: f"**{person.get_name()} (inner monologue):** Destroyed a village? I've only arrived here yesterday... What nonsense is this slime spouting?",
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
                if dialogue == f"**{person.get_name()} (inner monologue):** Destroyed a village? I've only arrived here yesterday... What nonsense is this slime spouting?":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to reason with the slime\n(b) Draw your weapon and fight!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        # Option A: Will converse with the enemy
                        if choice == "a":
                            conversations = [
                                "**Narrator:** You calmly attempt to explain your situation to the slime.",
                                lambda: f"**{person.get_name()}:** I have no knowledge of any village destruction. I arrived in this land just yesterday, and I'm escorting Father Austin to the Church for the prophecy.",
                                "**Father Austin:** We heard of the tragedy at Agrippa, a city devastated yesterday. Our faction is sending aid for its restoration.",
                                "**Angry Slime:** Wait... then you're not the one?! Our leader was tricked! Some hooded figure told us it was the 'hero' who did this!",
                                lambda: f"**{person.get_name()}:** A hooded figure? 'That person' must be one of Saturnus's lackeys! They're already making their moves!",
                                lambda: f"**Angry Slime:** I am so sorry, {person.get_name()}. Please, accept this small token of my gratitude.",
                                "**Narrator:** You receive a [SLIME HELMET, +50 Health] from the grateful slime.",
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
                            person.inventory.add_item("SLIME HELMET", 1)
                            person.skills.level_up_skill("BLESSING OF ARCANUS")
                            person.implement_blessing()
                            person.update_character()

                            while True:
                                # Asks the user if they still wanted to continue adventure
                                utilities.Space()
                                Progress.is_chapter_one_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
                                    # Error handling
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
                                "**Narrator:** You draw your weapon, assuming a battle stance against the slime.",
                                "**Narrator:** This is your first encounter with an enemy on this adventure.",
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
                            combat_manager.combat_system(slime)
                            utilities.typingPrint(f"**Narrator:** You find a Slime Helmet on the fallen creature and pick it up.")
                            person.gain_experience(100)
                            print(" ")
                            # Add an item and level up the skill
                            person.inventory.add_item("SLIME HELMET", 1)
                            person.skills.level_up_skill("BLESSING OF ARCANUS")
                            person.implement_blessing()

                            while True:
                                # Asks the user if they still wanted to continue adventure
                                utilities.Space()
                                Progress.is_chapter_one_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
    chapter = "THE PROPHECY UNFOLDS"

    messages = [
        lambda: f"**Narrator:** You and Father Austin arrive at the Church shortly...",
        "**Narrator:** Priestess Rafaela, the head of the Church, welcomes you with open arms.",
        lambda: f"**Priestess Rafaela:** Greetings, {person.get_name()} and Father Austin. Your presence here is a blessing.",
        lambda: f"**Priestess Rafaela:** This morning, I have received a continuation of the prophecy foretold about {person.get_name()}, our chosen hero.",
        lambda: f"**Priestess Rafaela:** Hear now the words of the prophecy...",
        lambda: f"**Divine Voice of Arcanus:** When the savior appears, chaos shall rise, threatening to consume this realm. The embodiment of evil shall commit an unpardonable act, forcing the destined hero to choose between their sanity and their duty.",
        "**Narrator:** The prophecy leaves everyone in shocked and bewildered silence...",
        lambda: f"**Father Austin:** Priestess, has the Church devised any interpretations for this new, ominous prophecy?",
        lambda: f"**Priestess Rafaela:** Not yet. It will take weeks for our scholars to formulate an official understanding. For now, enjoy the Church's hospitality. The city of Agrippa has many factions lending a hand, so most of our attendees are busy.",
        lambda: f"**{person.get_name()}:** Thank you, Priestess Rafaela. We will surely enjoy our stay here!",
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

        if message == f"**{person.get_name()}:** Thank you, Priestess Rafaela. We will surely enjoy our stay here!":
            dialogues = [
                lambda: f"**Narrator:** You and Father Austin explore the Church a bit.",
                lambda: f"**Narrator:** Suddenly, a cry of distress pierces the quiet.",
                "**???:** The reinforcement supply team! We're under attack! Please, someone help!",
                "**Priestess Rafaela:** Father Ryan, calm yourself and explain the situation clearly...",
                "**Father Ryan:** Priestess, forgive my outburst! We were ambushed by a group of orcs while transporting food. I barely escaped! The other Fathers are still there!",
                lambda: f"**Priestess Rafaela:** {person.get_name()} and Father Austin, I entrust this matter to you.",
                lambda: f"**Priestess Rafaela:** I will cast a powerful spell, teleporting you both to the supply team.",
                lambda: f"**Priestess Rafaela:** And take these blessings, {person.get_name()}. You will need them.",
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

                if dialogue == f"**Priestess Rafaela:** And take these blessings, {person.get_name()}. You will need them.":
                    person.gain_experience(200)
                    person.skills.level_up_skill("BLESSING OF ARCANUS")

                while True:
                    utilities.Space()
                    Progress.is_chapter_two_completed = True
                    utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
    chapter = "UNFORTUNATE INTERCEPTION"

    messages = [
        lambda: f"**Narrator:** You and Father Austin are instantly teleported to the chaotic scene.",
        "**Orc King:** What sorcery is this?! How did you arrive here all of the sudden?",
        "**Orc King:** Enough talk! I hunger for battle! Attack them!",
        lambda: f"**{person.get_name()}:** Father Austin, stay back! I will deal with these orcs.",
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

        if message == f"**{person.get_name()}:** Father Austin, stay back! I will deal with these orcs.":
            dialogues = [
                lambda: f"**Narrator:** {person.get_name()}, I must introduce to you, another form of battle. In this game, you are bound to be victorious right?",
                "**Narrator:** Not anymore. This will be challenging. Good luck dealing with a multitude of enemies.",
                "**Narrator:** A ferocious group of orcs, led by their King, emerge to confront you!",
                "**Orc King:** You puny humans will be our feast for today!",
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

                if dialogue == "**Orc King:** You puny humans will be our feast for today!":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to reason with the Orc King\n(b) Engage the Orcs in battle!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        if choice == "a":
                            conversations = [
                                lambda: f"**{person.get_name()}:** Please, do not do this. We do not wish to harm you. Retreat now, and no one gets hurt.",
                                "**Orc King:** You dare threaten us, human?! You speak as if you can defeat us!",
                                "**Orc King (to his minions):** Grab the old man! Use him to taunt the kid!",
                                "**Narrator:** The Orcs brutally seize Father Austin, injuring him in the process!",
                                lambda: f"**{person.get_name()}:** You will pay for this! I swear on my name!",
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
                            combat_manager.combat_system(orc)
                            combat_manager.combat_system(orc_king)
                            person.gain_experience(600)
                            print(" ")
                            person.skills.add_skill("CRITICAL EYE")
                            person.skills.level_up_skill("BLESSING OF ARCANUS")

                            while True:
                                utilities.Space()
                                Progress.is_chapter_three_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
                                lambda: f"**Narrator:** You wield your sword, ready to face the orcs in battle.",
                                "**Narrator:** The Orc King, in a desperate act, throws a strange poison at Father Austin causing him to collapse.",
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
                            combat_manager.combat_system(orc)
                            combat_manager.combat_system(orc_king)
                            person.gain_experience(600)
                            print(" ")
                            person.skills.add_skill("CRITICAL EYE")
                            person.skills.level_up_skill("BLESSING OF ARCANUS")

                            while True:
                                utilities.Space()
                                Progress.is_chapter_three_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
    chapter = "FATED ENCOUNTER"

    messages = [
        "**Narrator:** The battle concludes, the Orcs are defeated. But Father Austin is in critical condition.",
        "**Narrator:** A week has passed...",
        lambda: f"**Narrator:** {person.get_name()} seeks counsel with Priestess Rafaela.",
        lambda: f"**Priestess Rafaela:** Greetings {person.get_name()}. Father Austin seems to be recovering well, but the council has discovered some concerning leads regarding Saturnus and his schemes.",
        lambda: f"**{person.get_name()}:** Lord Saturnus? Was he behind the ambush?",
        "**Priestess Rafaela:** Not directly, but there are suspicious connections between him and those orcs.",
        "**Priestess Rafaela:** The poison and weapons they wield are not from this realm, they are native to the Infernal Realm.",
        lambda: f"**{person.get_name()}:** Infernal Realm? This is getting more complicated.",
        "**Priestess Rafaela:** Indeed, and for that, I ask you to infiltrate the Infernal Realm. We must discover the full extent of their plans.",
        lambda: f"**{person.get_name()}:** How am I to enter the Infernal Realm if I am not affiliated with the Faction of Darkness?",
        "**Priestess Rafaela:** Through teleportation, as before. This time you will need this amulet.",
        lambda: f"**Narrator:** You receive the [AMULET OF MANIPULATION] from Priestess Rafaela.",
        "**Priestess Rafaela:** It will aid in disguising your identity within the Infernal Realm. However, you must avoid direct contact with Saturnus or his accomplices lest they uncover your true nature.",
        lambda: f"**{person.get_name()}:** Understood, Priestess. I will be vigilant this time.",
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

        if message == f"**{person.get_name()}:** Understood, Priestess. I will be vigilant this time.":
            dialogues = [
                lambda: f"**Narrator:** Once again, the Priestess's power transports {person.get_name()} to the outskirts of the Infernal Realm.",
                f"**Narrator:** A few details about the realm of darkness...",
                f"**Narrator:** Ruled by Saturnus, the God of Darkness and the twin brother of Arcanus. It is a realm where outcasts, demonic entities, and fugitives reside.",
                f"**Narrator:** It also houses the 'Infernal Guild', infamous for its members' ruthless struggle for power and greed.",
                lambda: f"**{person.get_name()}:** Such a wretched place. The peoples who lived here might as well be called psychopaths.",
                "**Narrator:** Before you stands the main gate of the Infernal Realm. Guards are checking each visitor's identification.",
                "**Narrator:** The line is long, so you have to wait. You decided to keep silent as they chattered...",
                "**Guard 1:** Have you heard about what happened to Elise recently?",
                "**Guard 2:** Yes, it seems that she was scolded by His Majesty. It seems that she went overboard torturing the priest.",
                "**Guard 3:** I heard that Elise was the one who controlled the Orc King to intercept the supply mission of the Church of Light in the City of Agrippa.",
                "**Guard 2:** Well, nothing to expect. That kid destroyed Agrippa completely. She seems to be poised to become His Majesty's successor.",
                "**Guard 1:** Probably after she eliminates the so-called 'Hero' of the Faction of Light.",
                "**Guard 3:** Right, that 'hero' will never win against Elise, in his entire lifetime.",
                lambda: f"**{person.get_name()}:** 'Elise'... Who is that person they speak of?",
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

                if dialogue == f"**{person.get_name()}:** 'Elise'... Who is that person they speak of?":
                    person.gain_experience(1000)
                    print(" ")
                    person.skills.add_skill("CRITICAL EYE")
                    person.skills.level_up_skill("BLESSING OF ARCANUS")

                while True:
                    utilities.Space()
                    Progress.is_chapter_four_completed = True
                    utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
    chapter = "UNMASKING THE ENEMY"

    messages = [
        "**Narrator:** As you proceed further into the Infernal Realm, the eerie silence is broken by a sudden commotion.",
        "**Infernal Guard:** Intruder! Halt!",
        "**Infernal Guard:** You don't belong here. Prepare to be judged!",
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
                "**Narrator:** The Infernal Guards, clad in dark armor, converge on your location.",
                "**Narrator:** Their eyes glow with malevolent intent.",
                "**Narrator:** It is time for another battle. These guys are stronger than your average orcs.",
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

                if dialogue == "**Narrator:** It is time for another battle. These guys are stronger than your average orcs.":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to flee\n(b) Stand your ground and fight!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        if choice == "a":
                            conversations = [
                                "**Narrator:** You attempt to evade the guards, but they are too quick, and they managed to grab you.",
                                "**Infernal Guard:** You can't run from the wrath of the Infernal Realm!",
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
                            combat_manager.combat_system(infernal_guard)
                            combat_manager.combat_system(infernal_guard)
                            person.gain_experience(1200)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF ARCANUS")
                            person.skills.level_up_skill("CRITICAL EYE")
                            if "FLAME SWORD" not in person.inventory.items:
                                person.inventory.add_item("FLAME SWORD", 1)
                            person.update_character()

                            while True:
                                utilities.Space()
                                Progress.is_chapter_five_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
                                "**Narrator:** You unsheathe your weapon, ready to face the Infernal Guards.",
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
                            combat_manager.combat_system(infernal_guard)
                            combat_manager.combat_system(infernal_guard)
                            person.gain_experience(1200)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF ARCANUS")
                            person.skills.level_up_skill("CRITICAL EYE")
                            if "FLAME SWORD" not in person.inventory.items:
                                person.inventory.add_item("FLAME SWORD", 1)
                            person.update_character()

                            while True:
                                utilities.Space()
                                Progress.is_chapter_five_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
    chapter = "IMPRISONED AND BETRAYED"

    messages = [
        "**Narrator:** The Infernal Guards lie defeated, but before you can fully assess your surroundings, a dark magic envelops you.",
        "**Narrator:** You collapse to the ground, your vision fading into blackness.",
        "**Narrator:** You awaken in a cold, damp cell. The stench of despair fills your nostrils. You are in the infamous 'Tower of Babel'.",
        lambda: f"**{person.get_name()}:** What happened...how did they catch me?",
        lambda: f"**{person.get_name()}:** Wait... I have the Amulet of Manipulation, right? How could they have identified me?",
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

        if message == f"**{person.get_name()}:** Wait... I have the Amulet of Manipulation, right? How could they have identified me?":
            dialogues = [
                "**Narrator:** You examine your cell. It's small, made of solid dark stone. No windows, just a heavy iron door.",
                lambda: f"**{person.get_name()}:** This is bad, very bad. I have to find a way to escape this prison.",
                "**Narrator:** You decide to survey the area a bit. You find a loose brick.",
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
                        person.skills.level_up_skill("BLESSING OF ARCANUS")
                        person.skills.level_up_skill("CRITICAL EYE")
                        Progress.is_chapter_six_completed = True
                        utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
                            chapter_six_point_five()
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

# Chapter six (part 2) of the story
def chapter_six_point_five():
    chapter = "A FAMILIAR FACE"

    messages = [
        "**Narrator:** You manage to pry the brick loose and discover a hidden passage.",
        "**Narrator:** After a series of twists and turns, you emerge outside the prison.",
        "**Narrator:** You are once again met with the grim reality of the Infernal Realm.",
        lambda: f"**Narrator:** But someone is standing in front of you, it is a familiar face... the hooded figure mentioned in Chapter 1.",
        lambda: f"**Elise:** Well, well... if it isn't the 'hero' who loves to meddle in our affairs.",
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

        if message == f"**Elise:** Well, well... if it isn't the 'hero' who loves to meddle in our affairs.":
            dialogues = [
                "**Narrator:** The woman before you removes her hood, revealing a dark, beautiful face.",
                "**Narrator:** It is Elise, the Infernal Realm's rising star, and the orchestrator of all your troubles.",
                lambda: f"**{person.get_name()}:** So, you are the one behind the ambush and everything else... How did you know about me despite having the amulet?",
                "**Elise:** That amulet...it's just a child's toy! I can see through your disguise like it's a simple glass.",
                "**Elise:** Enough chit-chat! You will perish before me.",
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

                if dialogue == "**Elise:** Enough chit-chat! You will perish before me.":
                    while True:
                        utilities.typingPrint(f"**Narrator:** What action will you take, {person.get_name()}?\n(a) Attempt to reason with Elise\n(b) Prepare for battle against Elise!")
                        print(" ")
                        choice = utilities.typingInput("\n> ").lower()
                        if choice == "a":
                            conversations = [
                                lambda: f"**{person.get_name()}:** Why are you doing this, Elise? We are not enemies by default.",
                                "**Elise:** Fool! I crave chaos and destruction, and you, with the Faction of Light, are against my very existence!",
                                "**Elise:** Now, let's end this meaningless conversation... Fight me if you dare, or run away like a coward!",
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
                            combat_manager.combat_system(elise)
                            person.gain_experience(1500)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF ARCANUS")
                            person.skills.level_up_skill("CRITICAL EYE")

                            while True:
                                utilities.Space()
                                Progress.is_chapter_six_half_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
                                "**Narrator:** Her dark aura intensifies, it's time for another test of your skills.",
                                "**Narrator:** Fight, Hero! Fight!",
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
                            combat_manager.combat_system(elise)
                            person.gain_experience(1500)
                            print(" ")
                            person.skills.level_up_skill("BLESSING OF ARCANUS")
                            person.skills.level_up_skill("CRITICAL EYE")
                            person.update_character()

                            while True:
                                utilities.Space()
                                Progress.is_chapter_six_half_completed = True
                                utilities.typingPrint(f"Will you continue your adventure to {utilities.next_chapter()}, Hero?")
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
    chapter = "THE FINAL BATTLE"

    messages = [
        "**Narrator:** You have managed to defeat Elise, but something is happening to her. The dark energy around her intensifies.",
        "**Narrator:** She rises once again, not the Elise you fought moments ago, but something...more.",
        "**Narrator:** The change is drastic, it reminds you of someone, but you cannot remember who.",
        lambda: f"**Elise (Final Form):** You may have defeated my previous form, hero, but now, I shall unleash my true power.",
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

        if message == f"**Elise (Final Form):** You may have defeated my previous form, hero, but now, I shall unleash my true power.":
            dialogues = [
                "**Narrator:** Elise's final form has manifested, it's time for your final battle.",
                "**Narrator:** You have come so far... will you succeed here, or will everything come to an end?",
                "**Narrator:** Fight, Hero! Fight with everything you have!",
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

                if dialogue == "**Narrator:** Fight, Hero! Fight with everything you have!":
                    utilities.Space()
                    utilities.magical_loading_screen()
                    utilities.LongPause()
                    person.update_character()
                    result = combat_manager.combat_system(elise_final)
                    person.gain_experience(3000)
                    print(" ")
                    person.skills.level_up_skill("BLESSING OF ARCANUS")
                    person.skills.level_up_skill("CRITICAL EYE")
                    person.update_character()

                    if result == "victory":
                        conversations = [
                            "**Narrator:** Elise's final form collapses, the dark energy dissipating into the air.",
                            "**Elise:** I... what have I done? I...I remember now...",
                            lambda: f"**{person.get_name()}:** It's over now, Elise.",
                            "**Narrator:** Elise is defeated, and the Infernal Realm seems to be calming down as well.",
                            lambda: f"**Narrator:** However, this is not the end of the story. The chaos and darkness you have experienced is merely the beginning of this saga.",
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
                            "**Elise (Final Form):** You have fought well, but you were never a match for me, fool!",
                            "**Narrator:** The Infernal Realm shakes, as a dark, ominous energy engulfs the very essence of the universe.",
                            "**Narrator:** You wake up at the Church of Light, and the Priestess is there, waiting for you.",
                            lambda: f"**Priestess Rafaela:** {person.get_name()}, I saw everything! The realms...are about to be destroyed! This is not the end...",
                            lambda: f"**Priestess Rafaela:** But...you must be stronger, for the coming trials are far worse than you have experienced so far!",
                            lambda: f"**Narrator:** However, this is not the end of the story. The chaos and darkness you have experienced is merely the beginning of this saga.",
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