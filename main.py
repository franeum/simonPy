#!/usr/bin/env python3

import os
import sys
import time
import random
import simon_midi as smidi

CHOICES = random.choices([0, 1, 2, 3], k=10)
WRONG = 'OH NOOOOOOOOOO'
NOTE_DURATION = 0.5


def play_seq(n, lst, interval):
    for item in lst[:n]:
        os.system('clear')
        print(item)
        smidi.play_note(smidi.NOTES[item], NOTE_DURATION)


def convert(s):
    return [int(x) for x in s if x.isdigit()]


def check_seq(n_items):
    n = 0
    while n < n_items:
        note = smidi.listen_note()

        print(note)
        if CHOICES[n] == note:
            n += 1
        else:
            print(WRONG)
            sys.exit(1)

    time.sleep(1)


if __name__ == '__main__':
    smidi.spegni()

    for num in range(1, 11):
        play_seq(num, CHOICES, 1)
        check_seq(num)
