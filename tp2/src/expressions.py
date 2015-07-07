# -*- coding: utf-8 -*-
figure_values = {
    "redonda": 1,
    "blanca": 2,
    "negra": 4,
    "corchea": 8,
    "semicorchea": 16,
    "fusa": 32,
    "semifusa": 64
}

class Start(object):
    def __init__(self, tempo, bar, voices):
        self.tempo = tempo
        self.bar = bar
        self.voices = voices

    def name(self):
        return "start"

    def children(self):
        return [self.tempo, self.bar, self.voices]

    def get_voices(self):
        return self.voices.get_arr_voices();

class TempoDefinition(object):
    def __init__(self, figure, speed):
        self.figure = figure
        self.speed = speed

    def name(self):
        return "#tempo " + self.figure + " " + str(self.speed)

    def milliseconds(self):
        return int(1000000 * 60 * figure_values[self.figure] / (4 * float(self.speed)))

    def children(self):
        return []

class BarDefinition(object):
    def __init__(self, beat, figure):
        self.beat = beat
        self.figure = figure

    def name(self):
        return "#compas " + self.fraction()

    def fraction(self):
        return str(self.beat) + "/" + str(self.figure)

    def children(self):
        return []

class Voices(object):
    def __init__(self, voice, other_voices):
        self.voice = voice
        self.other_voices = other_voices

    def name(self):
        return "voces"

    def children(self):
        if self.other_voices == None:
            return [self.voice]
        else:
            return [self.voice, self.other_voices]

    def get_arr_voices(self):
        voices = [self.voice]
        if self.other_voices is not None:
            voices += self.other_voices.get_arr_voices()

        return voices

class Voice(object):
    def __init__(self, voice_number, bars):
        self.voice_number = voice_number
        self.bars = bars

    def name(self):
        return "voz " + str(self.voice_number)

    def children(self):
        return [self.bars]

    def get_bars(self):
        return self.bars.get_arr_bars()

class Bars(object):
    def __init__(self, bar, other_bars):
        self.bar = bar
        self.other_bars = other_bars

    def name(self):
        return "compases"

    def children(self):
        if self.other_bars == None:
            return [self.bar]
        else:
            return [self.bar, self.other_bars]

        return voices

    def get_arr_bars(self):
        bars = self.bar.get_arr_bars()
        if self.other_bars is not None:
            bars += self.other_bars.get_arr_bars()

        return bars

class Bar(object):
    def __init__(self, notes):
        self.notes = notes

    def name(self):
        return "compas"

    def children(self):
        return [self.notes]

    def get_arr_bars(self):
        return [self]

    def get_notes(self):
        return self.notes.get_arr_notes()

# Un repetir puede ir en lugar de un compás, por lo tanto también implementa
# get_arr_bars()

class Repeat(object):
    def __init__(self, times, bars):
        self.times = times
        self.bars = bars

    def name(self):
        return "repetir " + str(self.times)

    def children(self):
        return [self.bars]

    def get_arr_bars(self):
        return self.bars.get_arr_bars() * self.times

class Dot(object):
    def __init__(self, dot):
        self.dot = dot

    def name(self):
        return str(self.dot)

    def children(self):
        return []

class NoteModifier(object):
    def __init__(self, note_modifier):
        self.note_modifier = note_modifier

    def name(self):
        return str(self.note_modifier)

    def children(self):
        return []

class Silence(object):
    def __init__(self, figure, dot, other_notes):
        self.figure = figure
        self.dot = dot
        self.other_notes = other_notes

    def name(self):
        return "silencio " + self.figure

    def children(self):
        result = []
        if self.dot is not None:
            result.append(self.dot)
        if self.other_notes is not None:
            result.append(self.other_notes)
        return result

    def get_arr_notes(self):
        notes = [self]
        if self.other_notes is not None:
            notes += self.other_notes.get_arr_notes()

        return notes

    def get_value(self):
        return figure_values[self.figure]

class Note(object):
    def __init__(self, note, note_modifier, octave, figure, dot, other_notes):
        self.note = note
        self.note_modifier = note_modifier
        self.octave = octave
        self.figure = figure
        self.dot = dot
        self.other_notes = other_notes

    def name(self):
        return "nota " + self.note + self.note_modifier_name() + " octava " + str(self.octave) + self.figure

    def children(self):
        result = []
        if self.note_modifier is not None:
            result.append(self.note_modifier)
        if self.dot is not None:
            result.append(self.dot)
        if self.other_notes is not None:
            result.append(self.other_notes)
        return result

    def get_arr_notes(self):
        notes = [self]
        if self.other_notes is not None:
            notes += self.other_notes.get_arr_notes()

        return notes

    def note_modifier_name(self):
        note_modifier = ""
        if self.note_modifier is not None:
            note_modifier = self.note_modifier.name()

        return note_modifier

    def __str__(self):
        translation_notes = {
            "do": "c",
            "re": "d",
            "mi": "e",
            "fa": "f",
            "sol": "g",
            "la": "a",
            "si": "b"
        }

        return translation_notes[self.note] + self.note_modifier_name() + str(self.octave)

    def get_value(self):
        return figure_values[self.figure]
