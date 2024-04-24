from mido import MidiFile
from PIL import Image, ImageDraw

# Function to parse the MIDI file and extract necessary information
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

# Function to generate an image representing the MIDI data
def make_img(midPath, totalTime, maxNote):
    # Define image dimensions and parameters
    width = 800
    height = 800
    barHeight = 4

    # Calculate scaling factors based on MIDI data and image dimensions
    timeScale = width / totalTime
    noteScale = height / maxNote

    # Create a new blank image
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)

    # Open MIDI file again to process note data
    mid = MidiFile(midPath)
    currTime = 0
    for line in mid:
        if line.type == 'note_on':
            # Calculate coordinates for drawing the note bar
            x1 = int((currTime - line.time) * timeScale)
            x2 = int(currTime * timeScale)
            y1 = height - int(line.note * noteScale)
            y2 = y1 + barHeight

            # Draw a rectangle representing the note on the correct spot in the image
            draw.rectangle([x1, y1, x2, y2], fill = 'blue')

        currTime += line.time

    # Show the image
    img.show()

if __name__ == '__main__':
    midPath = 'C:/Users/danie/Documents/courses/S24/rcos/NoteVision/for_elise_by_beethoven.mid'
    totalTime, maxNote = parse_mid(midPath)
    make_img(midPath, totalTime, maxNote)