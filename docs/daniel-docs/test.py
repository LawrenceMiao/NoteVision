import mido
from PIL import Image, ImageDraw

midi_file_path = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/rach.mid"
midi_file = mido.MidiFile(midi_file_path)

# Iterate through the MIDI file and print out the messages
for msg in midi_file:
    print(msg)

pic_width = 800
pic_height = 600
bg_color = (255, 255, 255)
note_color = (0, 0, 0)

image = Image.new("RGB", (pic_width, pic_height), bg_color)
draw = ImageDraw.Draw(image)

for i in midi_file:
    if i.type == "note_on":
        x = i.time * 10
        y = i.note * 2
        width = 10
        height = 10
        draw.rectangle([x, y, x + width, y + height], fill = note_color)

image.show()