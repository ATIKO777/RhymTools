from utils.helper import get_tonal_plan, shift, sort_notes
from utils.scales import chromatic, lydian


class Melodizer:
    def __init__(self):
        self.notes = []

    def melodize(self, chord, position='s'):  # Позиционирование как субдоминанты вернёт самый устойчивый (лидийский) звукоряд
        self.notes = []
        tonal_plan_t = []
        tonal_plan_s = []
        tonal_plan_d = []

        chord_base_s = shift(chord.base, -5)
        chord_base_d = shift(chord.base, -7)

        if 't' in position:
            tonal_plan_t = get_tonal_plan(chord.base, chord.quality)  # Позиционирование как тоники
        if 's' in position:
            tonal_plan_s = get_tonal_plan(chord_base_s, chord.quality)  # Позиционирование как субдоминанты
        if 'd' in position:
            tonal_plan_d = get_tonal_plan(chord_base_d, chord.quality)  # Позиционирование как доминанты

        self.notes = sort_notes(list(set(tonal_plan_t + tonal_plan_s + tonal_plan_d)))
