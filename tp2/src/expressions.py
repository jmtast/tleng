class Start(object):
    def __init__(self, tempo, bar, voices):
        self.tempo = tempo
        self.bar = bar
        self.voices = voices

    def name(self):
        return "start"

    def children(self):
        return [self.tempo, self.bar, self.voices]

class TempoDefinition(object):
    def __init__(self, figure, speed):
        self.figure = figure
        self.speed = speed

    def name(self):
        return "#tempo " + self.figure + " " + str(self.speed)

    def children(self):
        return []

class BarDefinition(object):
    def __init__(self, beat, figure):
        self.beat = beat
        self.figure = figure

    def name(self):
        return "#compas " + str(self.beat) + "/" + str(self.figure)

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

class Voice(object):
    def __init__(self, voice_number, bars):
        self.voice_number = voice_number
        self.bars = bars

    def name(self):
        return "voz " + str(self.voice_number)

    def children(self):
        return [self.bars]

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

class Bar(object):
    def __init__(self, notes):
        self.notes = notes

    def name(self):
        return "compas"

    def children(self):
        return [self.notes]

class Repeat(object):
    def __init__(self, times, bars):
        self.times = times
        self.bars = bars

    def name(self):
        return "repetir " + str(self.times)

    def children(self):
        return [self.bars]

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
        if self.dot != None:
            result.append(self.dot)
        if self.other_notes != None:
            result.append(self.other_notes)
        return result

class Note(object):
    def __init__(self, note, note_modifier, octave, figure, dot, other_notes):
        self.note = note
        self.note_modifier = note_modifier
        self.octave = octave
        self.figure = figure
        self.dot = dot
        self.other_notes = other_notes

    def name(self):
        return "nota " + self.note + " octava " + str(self.octave) + self.figure

    def children(self):
        result = []
        if self.note_modifier != None:
            result.append(self.note_modifier)
        if self.dot != None:
            result.append(self.dot)
        if self.other_notes != None:
            result.append(self.other_notes)
        return result
