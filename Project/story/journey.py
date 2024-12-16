# Module/Imports/Libraries
# from Project.story import epilogue
from Project.story.hero_path import hero_story
from Project.story.evil_path import villain_story

# Handles the separation of story of each path
def Journey(person):
    if person.isHero:
        hero_story.loader()
        # epilogue.Hero_Epilogue()
    elif person.isEvil:
        villain_story.loader()
        # epilogue.Evil_Epilogue()
    else:
        print("Access Denied, this is a loophole")