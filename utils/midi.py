import pretty_midi


class Midi:
    def __init__(self, path):
        self.path = path
        self.last_bar = 0

        self.file = pretty_midi.PrettyMIDI()
        self.instrument = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Acoustic Grand Piano'))
        self.file.instruments.append(self.instrument)

    def add_note(self, note_num, start, end):
        note = pretty_midi.Note(
            velocity=100,  # громкость (от 0 до 127)
            pitch=note_num,  # номер ноты
            start=start,  # время начала в секундах
            end=end  # время окончания в секундах
        )
        self.instrument.notes.append(note)

    def add_chord(self, chord):
        pass

    def save(self):
        self.file.write(self.path)

