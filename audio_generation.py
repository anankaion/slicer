from pydub.generators import Sine
from pydub.generators import SignalGenerator
from pydub.generators import WhiteNoise
from pydub.playback import play

VOLUME = -20

# produce a wave at an exact frequency
def makemusic():
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
   for i in range(20, 10000, 100):
        sine = Sine(float(i))
        play(sine.to_audio_segment(20, VOLUME))

   white = WhiteNoise()
   play(white.to_audio_segment(20, VOLUME))
