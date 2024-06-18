pip install MIDIUtil

from midiutil import MIDIFile
import numpy as np

def get_scale(scale_name, octave):
    scales = {
        "C_major": [0, 2, 4, 5, 7, 9, 11, 12],
        "G_major": [7, 9, 11, 12, 14, 16, 18, 19],
        "D_major": [2, 4, 6, 7, 9, 11, 13, 14],
        "A_minor": [9, 11, 12, 14, 16, 17, 19, 21],
        "E_minor": [4, 6, 7, 9, 11, 12, 14, 16],
        "C_dorian": [0, 2, 3, 5, 7, 9, 10, 12],
        "G_dorian": [7, 9, 10, 12, 14, 16, 17, 19],
        "D_phrygian": [2, 3, 5, 7, 9, 10, 12, 14],
        "A_phrygian": [9, 10, 12, 14, 16, 17, 19, 21],
        "C_lydian": [0, 2, 4, 6, 7, 9, 11, 12],
        "G_lydian": [7, 9, 11, 13, 14, 16, 18, 19],
        "D_mixolydian": [2, 4, 6, 7, 9, 11, 12, 14],
        "A_mixolydian": [9, 11, 13, 14, 16, 17, 19, 21],
        "C_locrian": [0, 1, 3, 5, 7, 8, 10, 12],
        "G_locrian": [7, 8, 10, 12, 14, 15, 17, 19]
    }
    base_octave = 12 * octave
    return [note + base_octave for note in scales.get(scale_name, scales["C_major"])]

def create_variation(scale_name="C_major", bpm=120, octave=4):
    scale = get_scale(scale_name, octave)
    

    midi = MIDIFile(1)  
    track = 0
    time = 0
    midi.addTrackName(track, time, "Sample Track")
    midi.addTempo(track, time, bpm)

    durations = [0.25, 0.5, 1, 2]  
    total_time = 0
    volume = 100  

    last_note = None  

    while total_time < 16:
        duration = np.random.choice(durations)
        if total_time + duration > 16:  
            duration = 16 - total_time
        
        if last_note is not None:
            while True:
                pitch = np.random.choice(scale)
                if abs(pitch - last_note) <= 7:  
                    break
        else:
            pitch = np.random.choice(scale)

        midi.addNote(track, 0, pitch, time, duration, volume)
        time += duration
        total_time += duration
        last_note = pitch

    filename = f"variation_{scale_name}_{bpm}bpm_octave{octave}.mid"
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
    bpm = int(input("Enter the BPM (e.g., 120): "))
    octave = int(input("Enter the octave (e.g., 4): "))
    create_variation(scale_name, bpm, octave)
