# Modules/Imports/Libraries
import pyfiglet
import time
import os
import sys
import random

from Project.util.progress_system import Progress
from Project.story import prologue
from Project.story.hero_path import hero_story
from Project.story.evil_path import villain_story
from Project.util.variable_handler import person
from Project.util.character import Character

# Allows the program to print text with a typing effect
def typingPrint(text, speed=0.1):
    if callable(text):
        text = text()

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)

# Allows the program to execute input with a typing effect as well
def typingInput(text, speed=0.05):
    typingPrint(text, speed)
    return input()

# Prints a specified number of blank lines.
def Space(count=1):
    print("\n" * count, end="")

# Pauses and waits for user input.
def LongPause(delay=1.5):
    time.sleep(delay)
    typingPrint("\nPress enter to continue")
    input()
    Clear()

# Pauses time for a while.
def Pause(delay=1.5):
    time.sleep(delay)

# Clears the terminal screen
def Clear():
    os.system("cls" if os.name == "nt" else "clear")

# Prints the title of the story in an ASCII manner
def title():
    """Displays the game title."""
    ascii_banner = pyfiglet.figlet_format("TALES OF RUNETERRA")
    print(ascii_banner)

# Manages the game's title screen and main menu.
def title_screen():
    while True:
        Progress.load_progress()
        Clear()
        title()
        typingPrint("This is Runeterra, the world of mighty warriors.\n")

        if Progress.is_prelude_completed:
            choice = typingInput("\nType 'start' for new adventures, 'load' to continue, or 'exit' to leave:\n> ").lower()
        else:
            choice = typingInput("\nType 'start' to embark on new adventures or 'exit' to leave:\n\n> ").lower()

        if choice == "start":
            if not Progress.is_prelude_completed:
                 prologue.prelude()
            else:
                prologue.prelude()
            break
        elif choice == "load" and Progress.is_prelude_completed:
            load_game()
            break
        elif choice == "exit":
            game_exit()
            break
        else:
           typingPrint("\nInvalid option. Please try again.\n")
           Pause(2)

def load_game():
    # Allows the player to load a specific chapter.
    Clear()
    title()
    print(f"Name: {Character.get_name(person)}")
    Progress.save_progress()
    typingPrint("Select the chapter you want to load:\n")
    chapters = []
    chapter_mapping = {}

    # Determine character path and story module
    Progress.load_progress() # Load the progress first
    story_module = None
    if person.isHero:
        story_module = hero_story
    elif person.isEvil:
        story_module = villain_story
    else:
        typingPrint("Loophole")

    # Chapter list and mapping
    # Prelude - Always available to start the game
    chapters.append("0. Prelude (Replay)" if Progress.is_prelude_completed else "0. Prelude")
    chapter_mapping["0"] = prologue.prelude

    # Chapter 1
    if Progress.is_prelude_completed:  # Only show if prelude is completed
        chapters.append("1. Chapter One (Replay)" if Progress.is_chapter_one_completed else "1. Chapter One")
        chapter_mapping["1"] = story_module.chapter_one

    # Chapter 2
    if Progress.is_chapter_one_completed:
        chapters.append("2. Chapter Two (Replay)" if Progress.is_chapter_two_completed else "2. Chapter Two")
        chapter_mapping["2"] = story_module.chapter_two

    # Chapter 3
    if Progress.is_chapter_two_completed:
        chapters.append("3. Chapter Three (Replay)" if Progress.is_chapter_three_completed else "3. Chapter Three")
        chapter_mapping["3"] = story_module.chapter_three

    # Chapter 4
    if Progress.is_chapter_three_completed:
        chapters.append("4. Chapter Four (Replay)" if Progress.is_chapter_four_completed else "4. Chapter Four")
        chapter_mapping["4"] = story_module.chapter_four

    # Chapter 5
    if Progress.is_chapter_four_completed:
        chapters.append("5. Chapter Five (Replay)" if Progress.is_chapter_five_completed else "5. Chapter Five")
        chapter_mapping["5"] = story_module.chapter_five

    # Chapter 6
    if Progress.is_chapter_five_completed:
        chapters.append("6. Chapter Six (Replay)" if Progress.is_chapter_six_completed else "6. Chapter Six")
        chapter_mapping["6"] = story_module.chapter_six

    # Chapter 6.5
    if Progress.is_chapter_six_completed:
        chapters.append("6.5. Chapter Six (Part 2) (Replay)" if Progress.is_chapter_six_half_completed else "6.5. Chapter Six (Part 2)")
        chapter_mapping["6.5"] = story_module.chapter_six_point_five

    # Chapter 7
    if Progress.is_chapter_six_half_completed:
        chapters.append("7. Arc 1 Finale: Chapter Seven (Replay)" if Progress.is_chapter_seven_completed else "7. Arc 1 Finale: Chapter Seven")
        chapter_mapping["7"] = story_module.chapter_seven

    chapters.append("\nArc 2 to be continued...") if Progress.is_chapter_seven_completed else None

    for chapter in chapters:
        print(chapter)

    chapter_choice = typingInput("\nEnter the chapter number to load: ")

    if chapter_choice in chapter_mapping:
        typingPrint(f"\nStarting {chapters[int(chapter_choice) if chapter_choice.replace('.', '', 1).isdigit() else 0].split('(')[0].strip()}...")
        Pause(3)
        chapter_mapping[chapter_choice]()
    else:
        typingPrint("\nInvalid choice or chapter not yet unlocked.")
        Pause(3)

# Returns the name of the current chapter based on progress.
def current_chapter():
    if Progress.is_chapter_seven_completed:
         return "Chapter Seven"
    elif Progress.is_chapter_six_half_completed:
         return "Chapter Six (Part 2)"
    elif Progress.is_chapter_six_completed:
         return "Chapter Six"
    elif Progress.is_chapter_five_completed:
        return "Chapter Five"
    elif Progress.is_chapter_four_completed:
        return "Chapter Four"
    elif Progress.is_chapter_three_completed:
        return "Chapter Three"
    elif Progress.is_chapter_two_completed:
        return "Chapter Two"
    elif Progress.is_chapter_one_completed:
        return "Chapter One"
    else:
        return "Chapter Unknown"

# Returns the name of the next chapter based on progress.
def next_chapter():
    if Progress.is_chapter_seven_completed:
        return "To be continued"
    elif Progress.is_chapter_six_half_completed:
         return "Chapter Seven"
    elif Progress.is_chapter_six_completed:
        return "Chapter Six (Part 2)"
    elif Progress.is_chapter_five_completed:
        return "Chapter Six"
    elif Progress.is_chapter_four_completed:
        return "Chapter Five"
    elif Progress.is_chapter_three_completed:
        return "Chapter Four"
    elif Progress.is_chapter_two_completed:
        return "Chapter Three"
    elif Progress.is_chapter_one_completed:
        return "Chapter Two"
    else:
        return "Chapter One"

# Displays a loading screen with animations.
def magical_loading_screen():
    phases = [
        "Drawing the summoning circle...",
        "Gathering ethereal energy...",
        "Summoning the fated one...",
        "Meeting the council of authority...",
        "Deciding the destiny of this realm...",
        "Weaving the threads of fate...",
    ]
    symbols = ["🔮", "✨", "🔥", "🌙", "⚡", "💀"]

    for _ in range(3):
        for symbol in symbols:
            sys.stdout.write(f"\r{symbol} Summoning your destiny {symbol} ")
            sys.stdout.flush()
            time.sleep(0.3)

    for phase in phases:
        sys.stdout.write(f"\r{phase} {' ' * 10}\n")
        sys.stdout.flush()
        time.sleep(random.uniform(1.5, 2.5))

    print(" ")
    sys.stdout.write("\r✨ The portal has opened! Your adventure in the land of Runeterra begins... ✨\n"
    )
    sys.stdout.flush()

# Displays a goodbye message and exits the game.
def game_exit(delay=1.5):
    time.sleep(delay)
    Clear()
    title()
    typingPrint("Looks like you are leaving the land of Runeterra. Hoping to see you again.")
    exit()