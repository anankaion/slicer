from pydub import AudioSegment
from pydub.playback import play

from sys import argv

from audio_generation import makenoise
from audio_generation import makemusic
from audio_generation import frequency_sweep

is_export = False  # flag if export is necessary
export = AudioSegment.empty()  # export audiofile dummy

# more than two arguments have to be given
if len(argv) > 3:

    # soundfiles necessary
    soundfile = AudioSegment.from_file(argv[1], format=argv[1].split(".")[1])  # Input soundfile

    # increase volume
    if argv[2] == "louder":
        print("Audio made louder by " + argv[3] + "dB")
        export = soundfile + int(argv[3])
        is_export = True

    # decrease volume
    elif argv[2] == "quieter":
        print("Audio made quieter by " + argv[3] + "dB")
        export = soundfile - int(argv[3])
        is_export = True

    # combine two audio files
    elif argv[2] == "combine":
        print("Audio files combined.")
        appendix = AudioSegment.from_file(argv[3], format=argv[3].split(".")[1])
        export = soundfile + appendix
        is_export = True

    # reverse audio file
    elif argv[2] == "reverse":
        print("Audio reversed.")
        export = soundfile.reverse()
        is_export = True

    # play the current audiofile
    elif argv[2] == "play":
        play(soundfile)

    # get info about audiofile
    elif argv[2] == "info":
        print("Audio Info:")
        print("dBFS:\t" + str(soundfile.dBFS))
        print("Channels:\t" + str(soundfile.channels))
        print("Sample Width:\t" + str(soundfile.sample_width))
        print("Frame Rate:\t" + str(soundfile.frame_rate))
        print("RMS:\t" + str(soundfile.rms))
        print("Max:\t" + str(soundfile.max))
        print("Length:\t" + str(soundfile.duration_seconds) + " seconds")

# single argument options
elif len(argv) > 1:
    if argv[1] == "makenoise":
        makenoise()

    elif argv[1] == "sweep":
        frequency_sweep()

    elif argv[1] == "makemusic":
        makemusic()

# if no operation is given
else:
    print("Specify operation.")

# if you know audiofile is available, export
if is_export:
    export.export("export", format=argv[1].split(".")[1])
