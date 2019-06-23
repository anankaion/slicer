from pydub import AudioSegment
from pydub.playback import play

from sys import argv

from audio_generation import makenoise
from audio_generation import makemusic
from audio_generation import frequency_sweep

is_export = False  # flag if export is necessary
export = AudioSegment.empty()  # export audiofile dummy

if argv[1] == "music":
    if argv[2] == "makenoise":
        makenoise()

    elif argv[2] == "sweep":
        frequency_sweep()

    elif argv[2] == "makemusic":
        if len(argv) > 4:
            makemusic(int(argv[3]), argv[4])

elif argv[1] == "file":
    # soundfiles necessary
    soundfile = AudioSegment.from_file(argv[2], format=argv[2].split(".")[2])  # Input soundfile

    # increase volume
    if argv[3] == "louder":
        print("Audio made louder by " + argv[4] + "dB")
        export = soundfile + int(argv[4])
        is_export = True

    # decrease volume
    elif argv[3] == "quieter":
        print("Audio made quieter by " + argv[4] + "dB")
        export = soundfile - int(argv[4])
        is_export = True

    # combine two audio files
    elif argv[3] == "combine":
        print("Audio files combined.")
        appendix = AudioSegment.from_file(argv[4], format=argv[4].split(".")[1])
        export = soundfile + appendix
        is_export = True

    # reverse audio file
    elif argv[3] == "reverse":
        print("Audio reversed.")
        export = soundfile.reverse()
        is_export = True

    # play the current audiofile
    elif argv[3] == "play":
        play(soundfile)

    # get info about audiofile
    elif argv[3] == "info":
        print("Audio Info:")
        print("dBFS:\t" + str(soundfile.dBFS))
        print("Channels:\t" + str(soundfile.channels))
        print("Sample Width:\t" + str(soundfile.sample_width))
        print("Frame Rate:\t" + str(soundfile.frame_rate))
        print("RMS:\t" + str(soundfile.rms))
        print("Max:\t" + str(soundfile.max))
        print("Length:\t" + str(soundfile.duration_seconds) + " seconds")

    # if you know audiofile is available, export
    if is_export:
        export.export("export", format=argv[2].split(".")[2])
