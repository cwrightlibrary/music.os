import tkinter as tk
from PIL import Image, ImageDraw, ImageFilter, ImageTk

class MovableRectangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movable Rectangle")
        
        # Create a canvas widget
        self.canvas = tk.Canvas(root, width=600, height=450, bg='#9EC4E9')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Draw a rectangle on the canvas 235x190
        self.rect = self.canvas.create_rectangle(50, 50, 285, 240, outline="", fill='#EEEEEE')
        self.rect_2 = self.canvas.create_rectangle(50, 50, 285, 90, outline="", fill="#9EADBD")
        
        # Bind mouse events to the canvas
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        
        # Initialize the rectangle position
        self.start_x = 0
        self.start_y = 0

    def on_click(self, event):
        # Check if the click is inside the rectangle
        if self.canvas.find_closest(event.x, event.y)[0] == self.rect_2:
            self.start_x = event.x
            self.start_y = event.y
        else:
            self.start_x = self.start_y = None

    def on_drag(self, event):
        if self.start_x is not None and self.start_y is not None:
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            
            # Move the rectangle by changing its coordinates
            self.canvas.move(self.rect_2, dx, dy)
            self.canvas.move(self.rect, dx, dy)
            
            # Update the start position for the next move
            self.start_x = event.x
            self.start_y = event.y

if __name__ == "__main__":
    root = tk.Tk()
    app = MovableRectangleApp(root)
    root.mainloop()
