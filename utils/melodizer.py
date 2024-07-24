from utils.helper import get_tonal_plan, shift


class Melodizer:
    def __init__(self):
        self.notes = []

    def melodize(self, chord, mode='full'):
        self.notes = []

        if mode == 'func':
            self.notes = self.func_melodize(chord)
        elif mode == 'lad':
            pass
        elif mode == 'full':
            pass

    @staticmethod
    def func_melodize(chord):
        chord_base_s = shift(chord.base, -5)
        chord_base_d = shift(chord.base, -7)

        tonal_plan_t = get_tonal_plan(chord.base, chord.quality)  # Позиционирование как тоники
        tonal_plan_s = get_tonal_plan(chord_base_s, chord.quality)  # Позиционирование как субдоминанты
        tonal_plan_d = get_tonal_plan(chord_base_d, chord.quality)  # Позиционирование как доминанты

        notes = list(set(tonal_plan_t + tonal_plan_s + tonal_plan_d))
        return notes
