from pydub import AudioSegment

from pydub.generators import Sine
from pydub.generators import Sawtooth
from pydub.playback import play

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


def makemusic():
    piece = AudioSegment.empty()

    print("Welcome to your virtual piano.")
    print("Please enter notes you want to play, separated by a space.")
    print("(Example: A,B,D,C,D)")
    notes = input().split(" ")

    for note in notes:
        saw = Sawtooth(NOTES.get(note))
        piece += saw.to_audio_segment(500, VOLUME)

    play(piece)
