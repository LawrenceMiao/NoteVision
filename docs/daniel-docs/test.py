import mido

# Define the path to your MIDI file
midi_file_path = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/rach.mid"

# Open the MIDI file
midi_file = mido.MidiFile(midi_file_path)

# Iterate through the MIDI file and print out the messages
for msg in midi_file:
    print(msg)