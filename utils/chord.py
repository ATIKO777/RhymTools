from utils.helper import shift


class Chord:
    def __init__(self, base, quality, shift_on=0):
        """
            Создаёт аккорд
            Parameters
            ----------
            base : str
                Базовая нота
            quality : str
                Наклонение (major/minor)
            shift_on : int
                Кол-во полутонов для сдвига базовой ноты (необязательно)
            Returns
            -------
            Chord : Chord
                Аккорд
        """
        self.quality = quality
        if shift_on:
            self.base = shift(base, shift_on)
        else:
            self.base = base
        self.name = self.set_name()
        self.voicing = self.set_voicing()

    def set_voicing(self):
        """
            Формирование состава аккорда (трезвучия)
            Parameters
            ----------

            Returns
            -------
            voicing : List
                Список нот в составе аккорда
        """
        voicing = []
        if self.quality == 'major':
            voicing.append(self.base)
            voicing.append(shift(self.base, 4))
            voicing.append(shift(self.base, 7))
        elif self.quality == 'minor':
            voicing.append(self.base)
            voicing.append(shift(self.base, 3))
            voicing.append(shift(self.base, 7))
        elif self.quality == 'dim':
            voicing.append(self.base)
            voicing.append(shift(self.base, 3))
            voicing.append(shift(self.base, 6))
        return voicing

    def set_name(self):
        """
            Формирование имени аккорда
            Parameters
            ----------

            Returns
            -------
            name : str
                Название аккорда
        """
        if self.quality == 'major':
            return self.base
        elif self.quality == 'minor':
            return f'{self.base}m'
        elif self.quality == 'dim':
            return f'{self.base}dim'

