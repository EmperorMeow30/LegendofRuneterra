from Project.util.character import Character
from Project.combat.hero_path.enemies import Slime, Orc, OrcKing, InfernalGuard, Elise, EliseFinalForm
from Project.combat.evil_path.enemies import Warrior, Giant, GiantKing, AngelicGuard, EliseAngel, EliseSeraphim

# Person
person = Character()

# Enemies (Hero Path)
slime = Slime(level=1)
orc = Orc(level=1)
orc_king = OrcKing(level=3)
infernal_guard = InfernalGuard(level=3)
elise = Elise(level=1)
elise_final = EliseFinalForm(level=1)

# Enemies (Evil Path)
warrior = Warrior(level=1)
giant = Giant(level=1)
giant_king = GiantKing(level=3)
angelic_guard = AngelicGuard(level=3)
elise_angel = EliseAngel(level=1)
elise_seraphim = EliseSeraphim(level=1)