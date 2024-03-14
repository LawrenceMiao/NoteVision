from mido import MidiFile
from PIL import Image, ImageDraw

mid_file_path = "C:/Users/danie/Documents/courses/S24/rcos/NoteVision/rach.mid"
mid_file = MidiFile(mid_file_path)

txt_file = open("rach.txt", "w")
for line in mid_file:
    txt_file.write(str(line) + "\n")
txt_file.close()

mid_file = MidiFile(mid_file_path)

max_note = 0
max_time = 0
for line in mid_file:
    if line.type == "note_on":
        if line.note > max_note:
            max_note = line.note
        if line.time > max_time:
            max_time = line.time

pic_width = int(max_time * 350) + 100
pic_height = (max_note * 15) + 300

bg_color = (255, 255, 255)
note_color = (0, 0, 255)
vertical_spacing = 5

image = Image.new("RGB", (pic_width, pic_height), bg_color)
draw = ImageDraw.Draw(image)

note_positions = {}
note_times = {}

mid_file = MidiFile(mid_file_path)

for line in mid_file:
    if line.type == "note_on":
        if line.note not in note_positions:
            note_positions[line.note] = 0
            note_times[line.note] = line.time
        else:
            note_positions[line.note] = note_times[line.note] * 100
        x = note_positions[line.note]
        y = line.note * 15
        width = 4
        height = 2
        draw.rectangle([x, y, x + width, y + height], fill = note_color)
        note_times[line.note] += line.time

image.show()