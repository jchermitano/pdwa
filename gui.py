# Python 3.x
import tkinter as tk
from PIL import Image, ImageTk
import os

# Create the main window
root = tk.Tk()
root.title("Welcome to Our App")
root.attributes("-fullscreen", True)  # Set full screen
root.geometry("1920x1080")  # Set custom dimensions

# Set the background color to gray
root.configure(bg="#D6D6D6")  # Set the background color to gray
 # Set the window size to full screen

# Load the logo image
logo_image = Image.open("F.png")  # Replace with your logo image file

# Resize the logo image to a larger size (e.g., 200x200 pixels)
logo_image = logo_image.resize((400, 350))

logo_image = ImageTk.PhotoImage(logo_image)

# Create a label to display the logo image with a gray background
logo_label = tk.Label(root, image=logo_image, bg="#D6D6D6")  # Set the background color of the label to gray
logo_label.image = logo_image  # Keep a reference to the image
logo_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)  # Center the logo vertically and horizontally

# Create a button to get started
def open_page():
    root.destroy()  # Close the current window
    os.system("python page.py")  # Open page.py in a new window

get_started_button = tk.Button(root, text="Get Started", font=("Helvetica", 22), command=open_page, bg="black", fg="white")  # Set the background color of the button to gray and text color to white
get_started_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  # Center the button vertically and horizontally

# Run the application
root.mainloop()