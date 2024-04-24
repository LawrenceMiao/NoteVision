from mido import MidiFile
from PIL import Image, ImageDraw

def parse_mid(midPath):
    mid = MidiFile(midPath)
    file = open('for_elise_by_beethoven.txt', 'w')

    totalTime = 0
    maxNote = 0
    for line in mid:
        file.write(str(line) + '\n')
        try:
            totalTime += line.time
            if line.note > maxNote:
                maxNote = line.note
        except:
            pass
    file.close()
    print(totalTime)
    print(maxNote)

    return totalTime, maxNote

def make_img(midPath, totalTime, maxNote):
    width = 800
    height = 800
    barHeight = 4

    timeScale = width / totalTime
    noteScale = height / maxNote

    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    mid = MidiFile(midPath)
    currTime = 0
    for line in mid:
        if line.type == 'note_on':
            # Calculate coordinates for the note
            x1 = int((currTime - line.time) * timeScale)
            x2 = int(currTime * timeScale)
            y1 = height - int(line.note * noteScale)
            y2 = y1 + barHeight

            draw.rectangle([x1, y1, x2, y2], fill = 'blue')

        currTime += line.time

    img.show()

if __name__ == '__main__':
    midPath = 'C:/Users/danie/Documents/courses/S24/rcos/NoteVision/for_elise_by_beethoven.mid'
    totalTime, maxNote = parse_mid(midPath)
    make_img(midPath, totalTime, maxNote)