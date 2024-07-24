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
