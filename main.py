from pydub import AudioSegment
from pydub.playback import play
from sys import argv

soundfile = AudioSegment.from_file(argv[1], format=argv[1].split(".")[1])
export = AudioSegment.empty()

if argv[2] == "louder":
    print("Audio made louder by " + argv[3] + "dB")
    export = soundfile + int(argv[3])

elif argv[2] == "quieter":
    print("Audio made quieter by " + argv[3] + "dB")
    export = soundfile - int(argv[3])

elif argv[2] == "combine":
    print("Audio files combined.")
    appendix = AudioSegment.from_file(argv[3], format=argv[3].split(".")[1])
    export = soundfile + appendix

elif argv[2] == "reverse":
    print("Audio reversed.")
    export = soundfile.reverse()

elif argv[2] == "play":
    play(soundfile)

elif argv[2] == "info":
    print("Audio Info:")
    print("dBFS:\t" + str(soundfile.dBFS))
    print("Channels:\t" + str(soundfile.channels))
    print("Sample Width:\t" + str(soundfile.sample_width))
    print("Frame Rate:\t" + str(soundfile.frame_rate))
    print("RMS:\t" + str(soundfile.rms))
    print("Max:\t" + str(soundfile.max))
    print("Length:\t" + str(soundfile.duration_seconds) + " seconds")

export.export("export", format=argv[1].split(".")[1])
