import time
from pygame import midi

NOTES = [1, 4, 7, 10]

midi.init()
m_out = midi.Output(2)
m_input = midi.Input(3, 1)


def spegni():
    for note in NOTES:
        m_out.note_on(note, 0, 0)


def play_note(pitch, dur):
    m_out.note_on(pitch, 127, 0)
    time.sleep(dur * 0.75)
    m_out.note_on(pitch, 0, 0)
    time.sleep(dur * 0.25)


def parse_note(raw):
    note = raw[0][0]
    if note[0] == 144 and note[1] in NOTES:
        return note[1]
    else:
        return -1


def listen_note():
    while True:
        res = m_input.read(1)
        if len(res):
            parsed = parse_note(res)
            if parsed != -1:
                return NOTES.index(parsed)
            else:
                continue
        else:
            continue
