import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
import numpy as np
from PIL import Image, ImageTk
import wavio

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")
root.attributes("-fullscreen", True)  # Set full screen
root.geometry("1920x1080")  # Set custom dimensions

# Create a frame for the logo with a white background
logo_frame = tk.Frame(root, bg="white", height=150)
logo_frame.pack(fill="x")

# Load the logo image
logo_image = Image.open("fault-finder.png")  # Replace with your logo image file

# Resize the logo image to a larger size (e.g., 200x200 pixels)
logo_image = logo_image.resize((450, 150))

logo_image = ImageTk.PhotoImage(logo_image)

# Create a label to display the logo image
logo_label = tk.Label(logo_frame, image=logo_image, bg="white")  # Set the background color of the label to white
logo_label.image = logo_image  # Keep a reference to the image
logo_label.pack(anchor="nw", pady=10)  # Place the logo at the top left corner

# Create a frame for the rest of the widgets with a gray background
main_frame = tk.Frame(root, bg="#eeeeee")
main_frame.pack(fill="both", expand=True)

is_recording = False
recording_data = []

# Function to start recording
def start_recording():
    global is_recording, recording_data
    if not is_recording:
        is_recording = True
        recording_data = []
        sd.default.samplerate = 44100
        sd.default.channels = 1
        messagebox.showinfo("Information", "Recording started!")
        stream = sd.InputStream(callback=callback)
        stream.start()
        root.after(100, update_stream, stream)

# Function to stop recording
def stop_recording():
    global is_recording
    if is_recording:
        is_recording = False
        messagebox.showinfo("Information", "Recording stopped!")
        save_recording()

# Callback function to collect audio data
def callback(indata, frames, time, status):
    if is_recording:
        recording_data.append(indata.copy())

# Function to update stream
def update_stream(stream):
    if is_recording:
        root.after(100, update_stream, stream)
    else:
        stream.stop()

# Function to save recording to a WAV file
def save_recording():
    recording_array = np.concatenate(recording_data, axis=0)
    wavio.write("recording.wav", recording_array, 44100, sampwidth=2)
    messagebox.showinfo("Information", "Recording saved as recording.wav")

# Function to predict audio type (non-functional)
def predict_audio_type():
    messagebox.showinfo("Prediction", "Prediction not implemented yet!")

# Create a label
label = tk.Label(main_frame, text="Hello, Tkinter!", font=("Helvetica", 24))
label.pack(pady=50)

# Create a frame for the recommendation
recommendation_frame = tk.Frame(main_frame, bg="#eeeeee")
recommendation_frame.pack(fill="x", pady=20)

# Create a label for the recommendation
recommendation_label = tk.Label(recommendation_frame, text="Recommendation:", font=("Helvetica", 18))
recommendation_label.pack(fill="x", padx=10)

# Create a listbox for the recommendation
recommendation_listbox = tk.Listbox(recommendation_frame, width=40, height=3)
recommendation_listbox.pack(side=tk.LEFT, padx=10)

# Add items to the listbox
recommendation_listbox.insert(tk.END, "Check the Alternator")
recommendation_listbox.insert(tk.END, "Check the Water Pump")
recommendation_listbox.insert(tk.END, "Check the Bearing Alternator Front")

# Create a frame to hold the buttons
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=50)

# Create Button 1 (Start) with color
button1 = tk.Button(button_frame, text="Start", command=start_recording, bg="green", fg="white", font=("Helvetica", 18))
button1.pack(side=tk.LEFT, padx=20)

# Create Button 2 (Stop) with color
button2 = tk.Button(button_frame, text="Stop", command=stop_recording, bg="red", fg="white", font=("Helvetica", 18))
button2.pack(side=tk.LEFT, padx=20)

# Create Button 3 (Predict) with color
button3 = tk.Button(button_frame, text="Done", command=predict_audio_type, bg="blue", fg="white", font=("Helvetica", 18))
button3.pack(side=tk.LEFT, padx=20)

root.mainloop()