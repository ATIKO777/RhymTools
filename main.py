'''
    Добавить генерацию midi
    Добавить мелодизацию по позиционированию аккорда T/S/D
    Добавить мелодизацию по лидийскому/дорийскому ладу
    Добавить возможность получать в мелодизации не лад, а интервалы, или короткие диапазоны
'''

# from generator import ChordsGen

# generator = ChordsGen('B', 'minor')
# generator.generate(4)
#
# for chord in generator.chords:
#     print(chord.name)

from utils.harmonizer import Harmonizer

harmonizer = Harmonizer()
harmonizer.harmonize(['C', 'D'])

for chord in harmonizer.chords:
    print(chord.name)


