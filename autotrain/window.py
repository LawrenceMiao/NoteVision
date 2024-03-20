import tkinter as tk


class RectangleDrawer:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.rect_start = None
        self.rect_end = None
        self.canvas.bind("<ButtonPress-1>", self.start_rect)
        self.canvas.bind("<B1-Motion>", self.draw_rect)
        self.canvas.bind("<ButtonRelease-1>", self.end_rect)

    def start_rect(self, event):
        self.rect_start = (event.x, event.y)

    def draw_rect(self, event):
        if self.rect_end:
            self.canvas.delete("temp_rect")
        self.rect_end = (event.x, event.y)
        self.canvas.create_rectangle(
            self.rect_start[0],
            self.rect_start[1],
            self.rect_end[0],
            self.rect_end[1],
            outline="black",
            tags="temp_rect",
        )

    def end_rect(self, event):
        if self.rect_end:
            self.canvas.delete("temp_rect")
            self.canvas.create_rectangle(
                self.rect_start[0],
                self.rect_start[1],
                self.rect_end[0],
                self.rect_end[1],
                outline="black",
            )
            self.rect_start = None
            self.rect_end = None


root = tk.Tk()
app = RectangleDrawer(root)
root.mainloop()
