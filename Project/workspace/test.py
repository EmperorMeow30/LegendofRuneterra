from Project.util.character import Character

def path_checking():
    person = Character()
    person.isHero = True
    person.isEvil = False
    person.isNeutral = False
    print(f"The character's race is: {person.path()}")

path_checking()