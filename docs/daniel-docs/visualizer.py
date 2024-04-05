from mido import MidiFile
from PIL import Image, ImageDraw

def parse_mid(mid_path):
    mid = MidiFile(mid_path)
    file = open('for_elise_by_beethoven.txt', 'w')

    total_time = 0
    max_note = 0
    for line in mid:
        file.write(str(line) + '\n')
        try:
            total_time += line.time
            if line.note > max_note:
                max_note = line.note
        except:
            pass
    file.close()
    print(total_time)
    print(max_note)

    return total_time, max_note

def make_img(mid_path, total_time, max_note):
    width = 800
    height = 800
    bar_height = 4

    time_scale = width / total_time
    note_scale = height / max_note

    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    mid = MidiFile(mid_path)
    current_time = 0
    for line in mid:
        if line.type == 'note_on':
            # Calculate coordinates for the note
            x1 = int((current_time - line.time) * time_scale)
            x2 = int(current_time * time_scale)
            y1 = height - int(line.note * note_scale)
            y2 = y1 + bar_height

            draw.rectangle([x1, y1, x2, y2], fill = 'blue')

        current_time += line.time

    img.show()

if __name__ == '__main__':
    mid_path = 'C:/Users/danie/Documents/courses/S24/rcos/NoteVision/for_elise_by_beethoven.mid'
    total_time, max_note = parse_mid(mid_path)
    make_img(mid_path, total_time, max_note)