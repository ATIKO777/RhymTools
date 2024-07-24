from utils.chord import Chord


class RhymanField:
    def __init__(self, tonic_note, tonic_quality):
        """
            Создает Римановское пространство трезвучий
            Parameters
            ----------

            tonic_note : str
                Тонический звук
            tonic_quality : str
                Наклонение тонического трезвучия

            Returns
            -------
            RhymanField : RhymanField
                Римановское пространство трезвучий
        """
        self.tonic_note = tonic_note
        self.tonic_quality = tonic_quality

        self.t = None
        self.s = None
        self.d = None
        self.s_m = None
        self.d_m = None
        self.e2 = None
        self.e7 = None

        self.t_low = None
        self.s_low = None
        self.d_low = None
        self.s_m_low = None
        self.d_m_low = None

        self.t_high = None
        self.s_m_high = None
        self.d_m_high = None

        self.set_field()

    def get_chords(self, filter='all'):
        """
            Получить аккорды по "параллелям"
            Parameters
            ----------

            filter : str
                Фильтр на параллели (tonality/high/low/all)

            Returns
            -------
            chords : List
                Список аккордов
        """
        chords = []
        if filter in ['tonality', 'all']:
            chords.extend([self.t, self.s, self.d, self.s_m, self.d_m, self.e2, self.e7])
        if filter in ['low', 'all']:
            chords.extend([self.t_low, self.s_low, self.d_low, self.s_m_low, self.d_m_low])
        if filter in ['high', 'all']:
            chords.extend([self.t_high, self.s_m_high, self.d_m_high])
        return chords

    def get_chords_by_tie(self, tie_level=1):
        """
            Получить аккорды по степеням родства
            Parameters
            ----------

            tie_level : int
                Степень родства (1-4)

            Returns
            -------
            chords : List
                Список аккордов
        """
        chords = []
        if tie_level == 1:
            chords.extend([self.t, self.s, self.d, self.s_m, self.d_m, self.e2, self.e7])
        elif tie_level == 2:
            chords.extend([self.t_low, self.s_low, self.d_low])
        elif tie_level == 3:
            chords.extend([self.s_m_high, self.d_m_high])
        elif tie_level == 4:
            chords.extend([self.t_high, self.s_m_low, self.d_m_low])
        return chords

    def set_field(self):
        """
            Заполняет пространство аккордами
        """
        if self.tonic_quality == 'major':
            self.t = Chord(self.tonic_note, 'major')
            self.s = Chord(self.tonic_note, 'major', 5)
            self.d = Chord(self.tonic_note, 'major', 7)
            self.s_m = Chord(self.tonic_note, 'minor', -3)
            self.d_m = Chord(self.tonic_note, 'minor', 4)
            self.e2 = Chord(self.tonic_note, 'minor', 2)
            self.e7 = Chord(self.tonic_note, 'dim', -1)

            self.t_low = Chord(self.tonic_note, 'minor')
            self.s_low = Chord(self.tonic_note, 'minor', 5)
            self.d_low = Chord(self.tonic_note, 'minor', 7)
            self.s_m_low = Chord(self.tonic_note, 'major', -4)
            self.d_m_low = Chord(self.tonic_note, 'major', 3)

            self.t_high = Chord(self.tonic_note, 'minor', 1)
            self.s_m_high = Chord(self.tonic_note, 'major', -3)
            self.d_m_high = Chord(self.tonic_note, 'major', 4)

        elif self.tonic_quality == 'minor':
            self.t = Chord(self.tonic_note, 'minor')
            self.s = Chord(self.tonic_note, 'minor', 5)
            self.d = Chord(self.tonic_note, 'minor', 7)
            self.s_m = Chord(self.tonic_note, 'major', -4)
            self.d_m = Chord(self.tonic_note, 'major', 3)
            self.e2 = Chord(self.tonic_note, 'dim', 2)
            self.e7 = Chord(self.tonic_note, 'major', -2)

            self.t_low = Chord(self.tonic_note, 'major')
            self.s_low = Chord(self.tonic_note, 'major', 5)
            self.d_low = Chord(self.tonic_note, 'major', 7)
            self.s_m_low = Chord(self.tonic_note, 'minor', -3)
            self.d_m_low = Chord(self.tonic_note, 'minor', 4)

            self.t_high = Chord(self.tonic_note, 'major', -1)
            self.s_m_high = Chord(self.tonic_note, 'minor', -4)
            self.d_m_high = Chord(self.tonic_note, 'minor', 3)
