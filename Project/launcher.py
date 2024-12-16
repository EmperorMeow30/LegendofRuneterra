# Imports/Modules/Libraries
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from story import prologue
from story.hero_path import hero_story
from util import utilities

# Launches the game
def launch():
    utilities.title_screen()
    prologue.prelude()
    prologue.reincarnation_procedure()
    hero_story.loader()

launch()