from mido import MidiFile
from PIL import Image, ImageDraw

file_path = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/rach.mid"
file = MidiFile(file_path)

for line in file:
    print(line)

max_note = 0
max_time = 0
for line in file:
    if line.type == "note_on":
        if line.note > max_note:
            max_note = line.note
        if line.time > max_time:
            max_time = line.time

pic_width = int(max_time * 300) + 500
pic_height = (max_note + 1) * 10 + 250

bg_color = (255, 255, 255)
note_color = (0, 0, 255)
vertical_spacing = 7

image = Image.new("RGB", (pic_width, pic_height), bg_color)
draw = ImageDraw.Draw(image)

note_positions = {}

file = MidiFile(file_path)

for line in file:
    if line.type == "note_on":
        if line.note not in note_positions:
            note_positions[line.note] = 0
        x = line.time * 300
        y = note_positions[line.note]
        width = 10
        height = 10
        draw.rectangle([x, y, x + width, y + height], fill = note_color)
        note_positions[line.note] += vertical_spacing

image.show()