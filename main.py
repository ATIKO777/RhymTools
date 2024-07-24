'''
    Добавить генерацию midi
    Добавить мелодизацию по лидийскому/дорийскому ладу
    Добавить возможность получать в мелодизации не лад, а интервалы, или короткие диапазоны
'''

# from generator import ChordsGen

# generator = ChordsGen('B', 'minor')
# generator.generate(4)
#
# for chord in generator.chords:
#     print(chord.name)

from utils.helper import get_tonal_plan, shift
from utils.chord import Chord
from utils.melodizer import Melodizer

melodizer = Melodizer()

melodizer.melodize(Chord('C', 'major'), 'func')

print(melodizer.notes)



