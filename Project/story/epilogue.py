import time
from Project.util import utilities
from Project.util.variable_handler import person

def Hero_Epilogue(delay=3):
    chapter = "Ending"

    dialogues = [
        lambda: f"Archangel Pleiades: {person.get_name()}, thank you for saving the entire world from the apocalypse caused by the Prince of Demons, Lucifer.",
        "Archangel Pleiades: Thank you for saving the entire world from the apocalypse caused by the Prince of Demons, Lucifer.",
        "Archangel Pleiades: Maybe this is not the last time, we will meet, right?",
        "System: You saved the world from the apocalypse. Behold, the Hero of the World.",
        "System: The End"
    ]

    for j, dialogue in enumerate(dialogues):
        utilities.LongPause()
        utilities.Clear()
        print(chapter)
        print(" ")
        utilities.typingPrint(dialogue)
        print(" ")

    time.sleep(delay)
    time.sleep(delay)
    utilities.title_screen()

def Evil_Epilogue(delay=3):
    chapter = "Ending"

    dialogues = [
        "General Diablo: Curse you for destroying the entire world and killing the Hero, Austley.",
        "General Diablo: We won, our race are the only one standing!",
        "System: You destroyed the world. Behold, the King of the World",
        "System: The End"
    ]

    for j, dialogue in enumerate(dialogues):
        utilities.LongPause()
        utilities.Clear()
        print(chapter)
        print(" ")
        utilities.typingPrint(dialogue)
        print(" ")

    time.sleep(delay)
    time.sleep(delay)
    utilities.title_screen()