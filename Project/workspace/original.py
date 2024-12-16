# # Goals
# # First Ending to Epilogue function
# # Stories?
# # Endings at Epilogue
# # Sana matapos yung circuits ko
#
# import pyfiglet, time, os, sys
#
# # name = str()
# # isHuman = bool()
# # isDemon = bool()
#
# def typingPrint(text):
#     if callable(text):
#         text = text()
#
#     for character in text:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.05)
#
# def typingInput(text):
#     for character in text:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.05)
#     value = input()
#     return value
#
# def LongPause(delay=1.5):
#     time.sleep(delay)
#     print("\nPress any key to continue")
#     input()
#     os.system("cls")
#
# def Pause(delay=1.5):
#     time.sleep(delay)
#
# def Clear():
#     os.system("cls")
#
# def title():
#     ascii_banner = pyfiglet.figlet_format("TALES OF RUNETERRA")
#     print(ascii_banner)
#
# def title_screen():
#     is_looping = True
#     while is_looping:
#         Clear()
#         title()
#         typingPrint("This is the runeterra, the world of the mighty warriors")
#         choice = input("\nType 'start' to embark new adventures\nType 'exit' to leave the game\n\nYour choice: ")
#         if choice == "start":
#             is_looping = False
#             prelude()
#         elif choice == "exit":
#             is_looping = False
#             game_exit()
#         else:
#             pass
#
# def launch():
#     title_screen()
#     prelude()
#
# def prelude():
#     chapter = "PRELUDE: STRING OF FATE"
#
#     messages = [
#         "The bell rings, it's a sign that classes ends in the afternoon.",
#         "You are such a lonely person that no one even befriends with you.",
#         "You were walking in road from your school, when suddenly, a truck accidentally hits you.",
#     ]
#
#     for i, message in enumerate(messages):
#         LongPause()
#         Clear()
#         print(chapter)
#         print(" ")
#         typingPrint(message)
#         print(" ")
#
#         if message == "You were walking in road from your school, when suddenly, a truck accidentally hits you.":
#             print(" ")
#             while True:
#                 user_input = typingInput("You sustained fatal damage, do you want to (a) surrender or (b) survive? ").lower()
#                 if user_input == "a":
#                     print(" ")
#                     typingPrint("You are so hopeless. Maybe if there's a second chance, maybe you will live a much happy life.")
#                     print("")
#                     reincarnation_procedure()
#                     break
#
#                 elif user_input == "b":
#                     dialogues = [
#                         "You have the determination to survive. Don't lose hope yet, everything will be fine.",
#                         "You have survived from the accident",
#                         "You graduated from College and pursued your passion as an Computer Engineer. You have been hired by multiple international companies, This accident will remain as a tale to be passed to the future generations of your family.",
#                         "THE END"  # Happy Ending
#                     ]
#
#                     for j, dialogue in enumerate(dialogues):
#                         LongPause()
#                         Clear()
#                         print(chapter)
#                         print(" ")
#                         typingPrint(dialogue)
#                         print(" ")
#                     break
#
#                 else:
#                     LongPause()
#                     Clear()
#                     print(chapter)
#                     print(" ")
#                     typingPrint("You must select a choice. Please retry...")
#                     LongPause()
#                     Clear()
#                     print(chapter)
#                     print(" ")
#
# def reincarnation_procedure():
#     chapter = "Story: DECISION"
#
#     messages = [
#         "A mysterious voice wakes you up...",
#         "???: You will be the one to control your fate.",
#         "???: To be the saviour of this world or to be it's worst calamity? Decide your fate!",
#         lambda: f"???: {name}, you will carry a heavy burden.",
#         "???: Now, you must decide your fate!",
#     ]
#
#     for i, message in enumerate(messages):
#         LongPause()
#         Clear()
#         print(chapter)
#         print(" ")
#         typingPrint(message)
#         print(" ")
#
#         if message == "???: To be the saviour of this world or to be it's worst calamity? Decide your fate!":
#             print(" ")
#             name = typingInput("???: What is your name? ").title()
#
#         if message == "???: Now, you must decide your fate!":
#             print(" ")
#             choice = typingInput("???: Your goal in this world is: (a) To protect this world or (b) To destroy it. Your goal is? ").lower()
#
#             if choice == "a":
#                 dialogues = [
#                     lambda: f"???: {name}, so you wanted to protect this world? How kind of you. ",
#                     "???: Please receive this blessing...",
#                     "System: You have received DIVINE BLESSING and BLESSING OF THE GOD OF LIGHT, because you chose to protect this world.",
#                     # There should be a power up popup here, to be added later.
#                     "???: Carry on and fulfill your mission."
#                 ]
#
#                 for j, dialogue in enumerate(dialogues):
#                     LongPause()
#                     Clear()
#                     print(chapter)
#                     print(" ")
#                     typingPrint(dialogue)
#                     print(" ")
#
#                 Hero_Journey()
#             else:
#                 dialogues = [
#                     lambda: f"???: {name}, so you wanted to destroy this world? How cruel of you! ",
#                     "???: You shall receive this curse...",
#                     "System: You have received DEMONIC CURSE and CURSE OF THE GOD OF DARKNESS, because you chose to destroy this world.",
#                     # There should be a power up popup here, to be added later.
#                     "???: Carry on and fulfill your ambition."
#                 ]
#
#                 for j, dialogue in enumerate(dialogues):
#                     LongPause()
#                     Clear()
#                     print(chapter)
#                     print(" ")
#                     typingPrint(dialogue)
#                     print(" ")
#
#                 Demon_Journey()
#
# def Hero_Journey():
#     # Battle System
#     Hero_Epilogue()
#
# def Demon_Journey():
#     # Battle System
#     Demon_Epilogue()
#
# def Hero_Epilogue(delay=1.5):
#     chapter = "Ending"
#
#     dialogues = [
#         #   lambda: f"???: {name}, thank you for saving the entire world from the apocalypse caused by the Prince of Demons, Lucifer.",
#         "Priest Patrick: Thank you for saving the entire world from the apocalypse caused by the Prince of Demons, Lucifer.",
#         "???: Maybe this is not the last time, we will meet, right?",
#         "System: You saved the world from the apocalypse. Behold, the Hero of the World.",
#         "System: The End"
#     ]
#
#     for j, dialogue in enumerate(dialogues):
#         LongPause()
#         Clear()
#         print(chapter)
#         print(" ")
#         typingPrint(dialogue)
#         print(" ")
#
#     time.sleep(delay)
#     title_screen()
#
# def Demon_Epilogue(delay=1.5):
#     chapter = "Ending"
#
#     dialogues = [
#         "General Diablo: Curse you for destroying the entire world and killing the Hero, Austley.",
#         "General Diablo: We won, our race are the only one standing!",
#         "System: You destroyed the world. Behold, the King of the World",
#         "System: The End"
#     ]
#
#     for j, dialogue in enumerate(dialogues):
#         LongPause()
#         Clear()
#         print(chapter)
#         print(" ")
#         typingPrint(dialogue)
#         print(" ")
#
#     time.sleep(delay)
#     title_screen()
#
# def game_exit(delay=1.5):
#     time.sleep(delay)
#     os.system("cls")
#     title()
#     typingPrint("Looks like you are leaving the land of runeterra, hoping to see you again.")
#     exit()
#
# # title_screen()
# # prelude()
# # reincarnation_procedure()
# # epilogue()
# launch()