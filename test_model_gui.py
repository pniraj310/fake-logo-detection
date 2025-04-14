import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Load the trained model
model = tf.keras.models.load_model("model/fake_logo_detector.h5")

# Function to predict image class
def predict_image(img_path):
    if not os.path.exists(img_path):
        messagebox.showerror("Error", f"File not found:\n{img_path}")
        return

    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    confidence = prediction[0][0]
    
    if confidence > 0.5:
        result = f"Prediction: FAKE LOGO\nConfidence: {confidence * 100:.2f}%"
    else:
        result = f"Prediction: REAL LOGO\nConfidence: {(1 - confidence) * 100:.2f}%"
    
    messagebox.showinfo("Prediction Result", result)

# File picker logic
def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if file_path:
        predict_image(file_path)

# Simple GUI
root = tk.Tk()
root.title("Fake Logo Detector")
root.geometry("300x150")

label = tk.Label(root, text="Click the button below to choose an image.")
label.pack(pady=20)

button = tk.Button(root, text="Select Image", command=open_file_dialog)
button.pack(pady=10)

root.mainloop()
