from mido import MidiFile
from PIL import Image, ImageDraw

def parse_mid(mid_path):
    mid = MidiFile(mid_path)
    file = open("for_elise_by_beethoven.txt", "w")

    total_time = 0
    max_note = 0
    for line in mid:
        file.write(str(line) + "\n")
        try:
            total_time += line.time
            if line.note > max_note:
                max_note = line.note
        except:
            pass
    file.close()

    return max_note, total_time

def make_img(mid, max_note, total_time):
    img_color = (255, 255, 255)
    note_color = (0, 0, 255)

    img = Image.new("RGB", (total_time, max_note), img_color)
    draw = ImageDraw.Draw(img)

    note_positions = {}
    note_times = {}

    mid = MidiFile(mid_path)

    for line in mid:
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

    img.show()

if __name__ == '__main__':
    mid_path = 'C:/Users/danie/Documents/courses/S24/rcos/NoteVision/for_elise_by_beethoven.mid'
    max_note, total_time = parse_mid(mid_path)
    # make_img(mid_path, max_note, total_time)