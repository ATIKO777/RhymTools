from utils.scales import chromatic, lydian
from utils.helper import check_in_lad, shift_scale
from utils.chord import Chord


class Harmonizer:
    def __init__(self):
        self.chords = []

    def harmonize(self, motif):
        self.chords = []

        # Перебор мажоров
        current_lad = []
        current_lad.extend(lydian)
        current_chromatic = []
        current_chromatic.extend(chromatic)
        for base in current_chromatic:
            if check_in_lad(motif, current_lad):
                self.chords.append(Chord(base, 'major'))
            current_lad = shift_scale(current_lad, 1)

        # Перебор миноров
        current_lad = []
        current_lad.extend(lydian)
        current_chromatic = []
        current_chromatic.extend(chromatic)
        current_chromatic = shift_scale(current_chromatic, -3)
        for base in current_chromatic:
            if check_in_lad(motif, current_lad):
                self.chords.append(Chord(base, 'minor'))
            current_lad = shift_scale(current_lad, 1)
