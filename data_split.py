import os
import random
import shutil

def split_dataset(images_dir, labels_dir, train_dir, test_dir, valid_dir, train_ratio=0.8, test_ratio=0.1, valid_ratio=0.1):
    # Create train, test, and valid directories if they don't exist
    for directory in [train_dir, test_dir, valid_dir]:
        os.makedirs(os.path.join(directory, "images"), exist_ok=True)
        os.makedirs(os.path.join(directory, "labels"), exist_ok=True)

    # Get list of image files
    image_files = [f for f in os.listdir(images_dir) if f.endswith(".jpg")]

    # Shuffle the list of image files
    random.shuffle(image_files)

    # Calculate number of images for train, test, and valid sets
    num_images = len(image_files)
    num_train = int(num_images * train_ratio)
    num_test = int(num_images * test_ratio)
    num_valid = num_images - num_train - num_test

    # Assign images to train, test, and valid sets
    train_images = image_files[:num_train]
    test_images = image_files[num_train:num_train+num_test]
    valid_images = image_files[num_train+num_test:]

    # Move images and corresponding labels to train directory
    move_files(train_images, images_dir, labels_dir, train_dir)
    # Move images and corresponding labels to test directory
    move_files(test_images, images_dir, labels_dir, test_dir)
    # Move images and corresponding labels to valid directory
    move_files(valid_images, images_dir, labels_dir, valid_dir)

def move_files(image_files, images_dir, labels_dir, output_dir):
    for image_file in image_files:
        image_path = os.path.join(images_dir, image_file)
        label_file = os.path.splitext(image_file)[0] + ".txt"
        label_path = os.path.join(labels_dir, label_file)
        if os.path.exists(label_path):
            shutil.move(image_path, os.path.join(output_dir, "images", image_file))
            shutil.move(label_path, os.path.join(output_dir, "labels", label_file))

def main():
    images_dir = "../RDD2022_Japan/Japan/train/images"
    labels_dir = "../RDD2022_Japan/Japan/train/labels"
    train_dir = "./train"
    test_dir = "./test"
    valid_dir = "./valid"
    split_dataset(images_dir, labels_dir, train_dir, test_dir, valid_dir)

if __name__ == "__main__":
    main()
