from utils.scales import chromatic


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
