from utils.scales import chromatic, natural_minor, natural_major


def check_in_lad(motif, lad):
    return set(motif).issubset(set(lad))


def shift(note, semitones):
    """
        Сдвинуть ноту на указанное кол-во полутонов
        Parameters
        ----------

        note : str
            Нота
        semitones : int
            Кол-во полутонов

        Returns
        -------
        name : str
            Название аккорда
    """
    return chromatic[(chromatic.index(note) + semitones) % 12]


def shift_scale(scale, semitones):
    for i in range(len(scale)):
        scale[i] = shift(scale[i], semitones)
    return scale


def get_tonal_plan(base, quality):
    tonal_plan = []
    if quality == 'major':
        tonal_plan.extend(natural_major)
    elif quality == 'minor':
        tonal_plan.extend(natural_minor)

    need_shift = chromatic.index(base)
    tonal_plan = shift_scale(tonal_plan, need_shift)
    return tonal_plan

def sort_notes(notes, order='ASC'):
    sorted_notes = []

    if order == 'ASC':
        for note in chromatic:
            if note in notes:
                sorted_notes.append(note)
    if order == 'DESC':
        for note in reversed(chromatic):
            if note in notes:
                sorted_notes.append(note)

    return sorted_notes

def compare_voices(chord_1, chord_2): 
    voices_1 = set(chord_1.voicing)
    voices_2 = set(chord_2.voicing)
    
    common_count = len(voices_1 & voices_2)
    max_count = max(len(voices_1), len(voices_2))

    return f'{common_count}/{max_count}'
