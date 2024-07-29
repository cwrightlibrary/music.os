import tkinter as tk
from PIL import Image, ImageDraw, ImageFilter, ImageTk

class BlurryRectangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blurry Rectangle")
        
        # Create a canvas widget
        self.canvas = tk.Canvas(root, width=500, height=500, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create a blurred rectangle and display it
        self.create_blurry_rectangle()

    def create_blurry_rectangle(self):
        # Create an image with PIL
        image = Image.new('RGBA', (500, 500), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        
        # Draw a black rectangle
        draw.rectangle([100, 100, 400, 400], fill='black')

        # Apply a blur filter
        blurred_image = image.filter(ImageFilter.GaussianBlur(10))
        
        # Convert PIL image to Tkinter image
        tk_image = ImageTk.PhotoImage(blurred_image)
        
        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        
        # Keep a reference to avoid garbage collection
        self.canvas.image = tk_image

if __name__ == "__main__":
    root = tk.Tk()
    app = BlurryRectangleApp(root)
    root.mainloop()
