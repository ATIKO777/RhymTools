from utils.rhyman import RhymanField
import random


class ChordsGen:
    def __init__(self, start_note, start_quality):
        self.current_field = RhymanField(start_note, start_quality)
        self.chords = list()

    @staticmethod
    def get_rand_number(p):
        return random.triangular(0, 100, p)

    def get_group(self, p1, p2, p3, p4):
        groups = list()
        groups.append(self.get_rand_number(p1))
        groups.append(self.get_rand_number(p2))
        groups.append(self.get_rand_number(p3))
        groups.append(self.get_rand_number(p4))
        return groups.index(max(groups)) + 1

    def generate(self, count):
        self.chords = []
        for _ in range(count):
            group = self.get_group(100, 85, 20, 5)
            chord = random.choice(self.current_field.get_chords_by_tie(group))
            self.chords.append(chord)
            if chord.quality != 'dim':
                self.current_field = RhymanField(chord.base, chord.quality)

    def get_current_tonic(self):
        return self.current_field.t
