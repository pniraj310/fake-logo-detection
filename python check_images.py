from PIL import Image
import os

def check_images(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                img = Image.open(file_path)  # Try opening the image
                img.verify()  # Check if it's corrupted
            except Exception as e:
                print(f"Corrupt image found and deleted: {file_path}")
                os.remove(file_path)  # Remove the corrupted file

# Change these paths if needed
check_images("dataset/train") 
check_images("dataset/validation")

print("Image check completed!")

