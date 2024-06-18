pip install MIDIUtil

from midiutil import MIDIFile
import numpy as np
def create_melody():
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "Sample Track")
    midi.addTempo(track, time, 120)

    scale = [60, 62, 64, 65, 67, 69, 71, 72] 
    duration = 1 
    volume = 100 

    for i in range(16):
        pitch = np.random.choice(scale)
        midi.addNote(track, 0, pitch, time, duration, volume)
        time += duration

    with open("melody.mid", "wb") as output_file:
        midi.writeFile(output_file)

if __name__ == "__main__":
    create_melody()
