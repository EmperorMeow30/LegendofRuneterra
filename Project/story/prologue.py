# Module/Imports/Libraries
from Project.util.character import display_character_status
from Project.story import journey
from Project.util import utilities
from Project.util.progress_system import Progress
from Project.util.variable_handler import person

# Calls the prelude function to show the start of the prologue story
def prelude():
    chapter = "PRELUDE: STRING OF FATE"
    utilities.LongPause()
    utilities.Clear()
    print(chapter)
    print(" ")
    utilities.typingPrint("Do you want for the story to be skipped?\n\n(a) Yes\n(b) No")
    print(" ")
    skip = utilities.typingInput("\n> ").lower()

    # Option A: Skips the prelude of the story
    if skip == "a":
        utilities.LongPause()
        utilities.Clear()
        print(chapter)
        print(" ")
        Progress.is_prelude_completed = True
        Progress.save_progress()
        utilities.typingPrint("You skipped the prelude story, which is a heavy story based part of this game. You will redirected to the next chapter of prologue shortly.")
        print(" ")
        print(" ")
        reincarnation_procedure()
    # Option B: Plays the prelude of the story
    elif skip == "b":
        messages = [
            "You are such a lonely person, your life is a warfare itself.",
            "Your life is a misery, everyone bullies you, even your own parents does.",
            "It haunts you even in your dream, everything you could ask for is a happy life, but fate is too cruel for you.",
            "Alarm: ding-ding-ding",
            "The bell rings, it's a sign that classes ends in the afternoon. You ought to find a food in the nearby restaurant, maybe you need some fresh air to distract you from your problems.",
            "You are crossing the road from your school, when suddenly, a speeding truck hits you.",
        ]

        # This is a function that will iterate each message in the messages list
        for i, message in enumerate(messages):
            utilities.LongPause()
            utilities.Clear()
            print(chapter)
            print(" ")
            utilities.typingPrint(message)
            print(" ")

            # If the message is present in the first message list, execute another list in the form of dialogues
            # This has the same logic as the messages list above
            if message == "You are crossing the road from your school, when suddenly, a speeding truck hits you.":
                while True:
                    dialogues = [
                        "Your classmates and the witnesses were horrified on what they have saw. Even though you are slightly unconscious, you can still hear them pitying you.",
                        "You even heard Joan, one of your classmates, crying. She is one of the people that you regarded as friend, she is the only person in your class who talks with you and even hangs out with you.",
                        "You: Fate is really cruel. I always wanted to confess to Joan, she is my only friend. Yet, my life is about to end here. If only I can live for another time.",
                        "System: The Gods of the Realm are asking you, do you want to live another life or do you want to survive and continue this life?",
                        "You: Wha-what? The Gods of the Realm? Am I really going to die here?",
                        "System: Once again, the Gods of the Realm are waiting for your response.",
                        "System: Do you want to:\n(a) live another life\n(b) continue your living your current life",
                    ]

                    for j, dialogue in enumerate(dialogues):
                        utilities.LongPause()
                        utilities.Clear()
                        print(chapter)
                        print(" ")
                        utilities.typingPrint(dialogue)
                        print(" ")

                    print(" ")
                    user_input = utilities.typingInput("> ").lower()

                    # Option A: Will proceed tp the reincarnation procedure (part 2 of the prelude)
                    if user_input == "a":
                        dialogues = [
                            "System: Are you sure that you want to live another life?",
                            "You: My current life i-is dreadful, everyone doesn't even treat me like a person except the only person that I longed for.",
                            "You: This is the only chance, and I should seize this moment. I want to be happy for once, maybe in my next life, I would be happy.",
                            "???: Very well, this is the response that I am waiting for you, my child."
                        ]

                        for j, dialogue in enumerate(dialogues):
                            utilities.LongPause()
                            utilities.Clear()
                            print(chapter)
                            print(" ")
                            utilities.typingPrint(dialogue)
                            print(" ")
                        Progress.is_prelude_completed = True
                        Progress.save_progress()
                        utilities.Pause(3)
                        reincarnation_procedure()
                        break

                    # Option B: Alternative Ending for the story
                    elif user_input == "b":
                        dialogues = [
                            "System: Are you sure that you want to live your current life?",
                            "You: Even though, I was being hated by everyone. There are some peoples who truly loved me in their own way, my grandparents, some of my classmates and even my friends. I will not leave them, instead, I would like to make my current life happier. I am hoping that everyone will recognize me in the future!",
                            "???: Very well, I should grant you the opportunity that you asked for. Live your life to the fullest, my child.",
                            "Many years later...",
                            "System: And this is how the future unfolds. You managed to graduate from your Computer Engineering course, you were offered different job positions across the world. You married Joan, your college sweetheart. And everyone acknowledged your contribution on the field of Engineering.",
                            "System: Alternative Ending: String of Fate (Time-skip): The story ends after the player wishes to continue their current life.",
                            "System: End of the Story, you are going to be redirected to the menu screen shortly."
                        ]

                        for j, dialogue in enumerate(dialogues):
                            utilities.LongPause()
                            utilities.Clear()
                            print(chapter)
                            print(" ")
                            utilities.typingPrint(dialogue)
                            print(" ")
                        # Will save the progress of the story and will return the user to the title screen
                        Progress.is_prelude_completed = True
                        Progress.save_progress()
                        utilities.Pause(3)
                        utilities.title_screen()
                        break
                    # Error Handling (will catch if the user doesn't type either "a" or "b"
                    else:
                        utilities.LongPause()
                        utilities.Clear()
                        print(chapter)
                        print(" ")
                        utilities.typingPrint("You must select a choice. Please retry...")
                        utilities.LongPause()
                        utilities.Clear()
                        print(chapter)
                        print(" ")
    # Error Handling (will catch if the user doesn't type either "a" or "b"
    else:
        utilities.LongPause()
        utilities.Clear()
        print(chapter)
        print(" ")
        utilities.typingPrint("You must select a choice. Please retry...")
        utilities.LongPause()
        utilities.Clear()
        print(chapter)
        print(" ")

# Calls the prelude function to show the second part of the prologue story
def reincarnation_procedure():
    chapter = "STORY: THE JUDGEMENT OF DECISION"

    # This is a function that will iterate each message in the messages list
    messages = [
        "System: Mysterious voices wakes you up. You opened your eyes, and saw two beings, to which you assumed as gods and they sit in their designated thrones.",
        "Archangel Pleiades: Mortal, the Gods of this Realm is calling upon you. You should speak with them immediately.",
        "Moments later...",
        "God of Light: My child, you will be the one to control your fate. You should aspire to be the bringer of peace on this realm.",
        "God of Darkness: Do not feed his minds with those words, Arcanus, that man shall become my successor and should bring destruction to this realm.",
        "Archangel Pleiades: Mortal, state your name.",
        lambda: f"Archangel Pleiades: {person.get_name()}, you will carry a heavy burden. This realm seeks for the guidance of someone like you, as the Gods of this realm are having some chaotic discourse. The future of this realm is in your hands.",
        lambda: f"Archangel Pleiades: {person.get_name()}, you must decide your fate carefully. The future of this realm is in your decision now. Think your decision wisely.",
        "Archangel Pleiades: And the judgement of decision, begins!"
    ]

    # This is a function that will iterate each message in the messages list
    for i, message in enumerate(messages):
        utilities.LongPause()
        utilities.Clear()
        print(chapter)
        print(" ")
        utilities.typingPrint(message)
        print(" ")

        # This will ask the user to input their name
        if message == "Archangel Pleiades: Mortal, state your name.":
            """Prompts the user for their name and ensures a non-empty input."""
            while True:
                print(" ")
                name = utilities.typingInput("System: Your name is ").strip().title()
                if name:
                    person.set_name(name) # set the person's name.
                    break
                else:
                    print("System: Please enter a valid name.")  # Provide user feedback if they did not input any name
        # This will ask the user to choose their goals in the game
        if message == "Archangel Pleiades: And the judgement of decision, begins!":
            while True:
                print("")
                utilities.typingPrint("System: Your goal in this world is:\n\n(a) To protect this world\n(b) To conquer it")
                print(" ")
                choice = input("> ").lower()
                # Option A: They are bound to hero path
                if choice == "a":
                    dialogues = [
                        lambda: f"Archangel Pleiades: {person.get_name()}, as expected to a kind person like you. You aspire to protect this world.",
                        lambda: f"{person.get_name()}: When I first got here, all I want is to be happy in my next life. I think this decision will make me happier. I always wanted to be the beacon of hope for everyone, this is the opportunity for it to happen.",
                        "God of Darkness: How dare you, foolish mortal, you conspired with Arcanus to overthrow the order of this realm? You will pay, my minions shall haunt you forever. YOU WILL PAY!",
                        "Arcanus, God of Light: I am intrigued about your actions, Saturnus. I will make sure to properly guide this child to overcome you and your dominions.",
                        "Moments later in the Sky Realm (Territory of Arcanus)...",
                        "Arcanus, God of Light: As expected for you, my child, you are such a kind soul. You shall receive the sacred blessing and the sacred weapon to prepare yourself against Saturnus and his followers.",
                        "System: You have received [SWORD OF LIGHT] and [BLESSING OF ARCANUS], because of your kind soul that you chose to protect this realm from destruction.",
                        "Arcanus, God of Light: Carry on and fulfill the prophecy!"
                    ]

                    for j, dialogue in enumerate(dialogues):
                        utilities.LongPause()
                        utilities.Clear()
                        print(chapter)
                        print(" ")
                        utilities.typingPrint(dialogue)
                        print(" ")
                    # Flags the user as Hero, saves the progress and gives the user item and skill
                    person.isHero = True
                    utilities.Space()
                    person.inventory.add_item("SWORD OF LIGHT", 1)
                    person.skills.add_skill("BLESSING OF ARCANUS")
                    utilities.Space()
                    display_character_status(person)
                    Progress.save_progress()
                    journey.Journey(person)
                    break
                # Option A: They are bound to evil path
                elif choice == "b":
                    dialogues = [
                        lambda: f"General Diablo: {person.get_name()}, as expected to a person like you. You shall become the successor of the Saturnus, the Great God of Darkness!",
                        lambda: f"{person.get_name()}: I was killed because of reckless people, everyone hated me, even my parents hates me. Everyone shall endure the pain that I experienced. I shall conquer the world!",
                        "God of Light: Do not be astray, my child, do not be deceived by Saturnus.",
                        lambda: f"{person.get_name()}: I was not deceived nor in the wrong path. I will bring catastrophe in this realm.",
                        lambda: f"Arcanus, God of Light: I am intrigued about the path that you've chosen, {person.get_name()}. I will guide the true Hero and they shall bring the true peace in this realm..",
                        "Moments later in the Infernal Realm (Territory of Saturnus)...",
                        lambda: f"Saturnus, God of Darkness: {person.get_name()}, you made the right choice. Arcanus is such an insolent, he even threatened us. That fool, who falsely advertise 'peace', but do not be deceived his reasons are far more sinister than mine. Receive this sacred blessing and this sacred weapon, it shall empower you. Come, and bring glory to the God of Darkness.",
                        "System: You have received [BOW OF CHAOS] and [BLESSING OF SATURNUS], because you made pact with the Devil itself that you chose to conquer this realm and bring destruction to the world.",
                        "Saturnus, God of Darkness: Conquer those lands for my glory!"
                    ]

                    for j, dialogue in enumerate(dialogues):
                        utilities.LongPause()
                        utilities.Clear()
                        print(chapter)
                        print(" ")
                        utilities.typingPrint(dialogue)
                        print(" ")
                    # Flags the user as Evil/Villain, saves the progress and gives the user item and skill
                    person.isEvil = True
                    utilities.Space()
                    person.inventory.add_item("BOW OF CHAOS", 1)
                    person.skills.add_skill("BLESSING OF SATURNUS")
                    print(" ")
                    display_character_status(person)
                    Progress.save_progress()
                    journey.Journey(person)
                    break
                else:
                    utilities.LongPause()
                    utilities.Clear()
                    print(chapter)
                    print(" ")
                    utilities.typingPrint("You must select a choice. Please retry...")
                    utilities.LongPause()
                    utilities.Clear()
                    print(chapter)
                    print(" ")