import os

def delete_empty_files(labels_dir, images_dir):
    # Iterate over files in labels directory
    for label_file in os.listdir(labels_dir):
        label_path = os.path.join(labels_dir, label_file)
        # Check if the file is empty
        if os.path.getsize(label_path) == 0:
            # Delete the empty text file
            os.remove(label_path)
            # Delete corresponding image file if exists
            image_path = os.path.join(images_dir, os.path.splitext(label_file)[0] + ".jpg")
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Deleted {label_file} and its corresponding image.")

def main():
    labels_dir = "../RDD2022_Japan/Japan/train/labels"
    images_dir = "../RDD2022_Japan/Japan/train/images"
    delete_empty_files(labels_dir, images_dir)

if __name__ == "__main__":
    main()
