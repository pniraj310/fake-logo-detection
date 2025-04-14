import os
import random
import shutil

def move_images(source_folder, destination_folder, percentage=20):
    # List all images in the source folder
    images = os.listdir(source_folder)

    # Calculate the number of images to move
    num_images_to_move = int(len(images) * (percentage / 100))

    # Randomly select images to move
    images_to_move = random.sample(images, num_images_to_move)

    # Create destination folder if not exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Move selected images
    for img in images_to_move:
        src_path = os.path.join(source_folder, img)
        dst_path = os.path.join(destination_folder, img)
        shutil.move(src_path, dst_path)

    print(f"Moved {num_images_to_move} images from {source_folder} to {destination_folder}")

# Move 20% of images from train to validation
move_images("dataset/train/real", "dataset/validation/real", 20)
move_images("dataset/train/fake", "dataset/validation/fake", 20)

print("Dataset split completed!")
