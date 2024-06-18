pip install MIDIUtil

from midiutil import MIDIFile
import numpy as np
def get_scale(scale_name):
    scales = {
        "C_major": [60, 62, 64, 65, 67, 69, 71, 72],
        "G_major": [67, 69, 71, 72, 74, 76, 78, 79],
        "D_major": [62, 64, 66, 67, 69, 71, 73, 74],
        "A_minor": [69, 71, 72, 74, 76, 77, 79, 81],
        "E_minor": [64, 66, 67, 69, 71, 72, 74, 76],
        "C_dorian": [60, 62, 63, 65, 67, 69, 70, 72],
        "G_dorian": [67, 69, 70, 72, 74, 76, 77, 79],
        "D_phrygian": [62, 63, 65, 67, 69, 70, 72, 74],
        "A_phrygian": [69, 70, 72, 74, 76, 77, 79, 81],
        "C_lydian": [60, 62, 64, 66, 67, 69, 71, 72],
        "G_lydian": [67, 69, 71, 73, 74, 76, 78, 79],
        "D_mixolydian": [62, 64, 66, 67, 69, 71, 72, 74],
        "A_mixolydian": [69, 71, 73, 74, 76, 77, 79, 81],
        "C_locrian": [60, 61, 63, 65, 67, 68, 70, 72],
        "G_locrian": [67, 68, 70, 72, 74, 75, 77, 79]
    }
    return scales.get(scale_name, scales["C_major"])

def create_variation(scale_name="C_major"):
    scale = get_scale(scale_name)
    
    midi = MIDIFile(1)
    track = 0
    time = 0
    midi.addTrackName(track, time, "Sample Track")
    midi.addTempo(track, time, 120)

    durations = [0.25, 0.5, 1, 2] 
    total_time = 0
    volume = 100 

    while total_time < 16:
        duration = np.random.choice(durations)
        if total_time + duration > 16:  
            duration = 16 - total_time
        pitch = np.random.choice(scale)
        midi.addNote(track, 0, pitch, time, duration, volume)
        time += duration
        total_time += duration

    filename = f"variation_{scale_name}.mid"
    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)
    print(f"MIDI file saved as {filename}")

if __name__ == "__main__":
    available_scales = [
        "C_major", "G_major", "D_major", "A_minor", "E_minor",
        "C_dorian", "G_dorian", "D_phrygian", "A_phrygian",
        "C_lydian", "G_lydian", "D_mixolydian", "A_mixolydian",
        "C_locrian", "G_locrian"
    ]
    
    print("Available scales:", ", ".join(available_scales))
    scale_name = input("Enter the scale name: ")
    create_variation(scale_name)
