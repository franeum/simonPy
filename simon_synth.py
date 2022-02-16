#!/usr/bin/env python3

from play_sounds import play_file

# play_file(DEFAULT_SONG)  # blocks by default

# play without blocking
play_file('./test2.wav', block=False)
