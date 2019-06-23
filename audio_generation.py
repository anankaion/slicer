from pydub import AudioSegment
from pydub.generators import Sine
from pydub.generators import Sawtooth
from pydub.playback import play

import random

VOLUME = -20

NOTES = {
    "C1": 523.25,
    "D": 587.33,
    "E": 659.25,
    "F": 698.46,
    "G": 783.99,
    "A": 880.00,
    "B": 987.77,
    "C2": 1046.50
}

NAMES = {
    1: "C1",
    2: "D",
    3: "E",
    4: "F",
    5: "G",
    6: "A",
    7: "B",
    8: "C2"
}


# produce a wave at an exact frequency
def makenoise():
    print("Welcome to the generator. What would you like to generate?")
    command = input()

    if command == "sine":
        print("Which frequency?")
        frequency = input()

        sine = Sine(float(frequency))
        out = sine.to_audio_segment(100)
        play(out)


# perform a frequency sweep
def frequency_sweep():
    sweep = AudioSegment.empty()

    for i in range(0, 10000, 50):
        sine = Sine(float(i))
        sweep += sine.to_audio_segment(10, VOLUME)

    play(sweep)


def generate_notes():
    track = AudioSegment.empty()

    print("Please enter notes you want to play, separated by a space.")
    print("Available notes: ")
    print(NOTES.keys())
    notes = input().split(" ")

    for note in notes:
        saw = Sawtooth(NOTES.get(note))
        track += saw.to_audio_segment(500, VOLUME)

    return track


def generate_notes_r():
    track = AudioSegment.empty()

    for i in range(16):
        saw = Sawtooth(NOTES.get(NAMES.get(random.randint(1, 8))))
        track += saw.to_audio_segment(500, VOLUME)

    return track


def makemusic(tracks, r):
    piece = AudioSegment.empty()

    print("Welcome to your virtual piano.")

    if r != "y":
        piece = generate_notes()
        for i in range(tracks - 1):
            piece = piece.overlay(generate_notes())

    else:
        piece = generate_notes_r()
        for i in range(tracks - 1):
            piece = piece.overlay(generate_notes_r())

    play(piece)
