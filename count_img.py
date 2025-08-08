import os


def count_images(folder):
    count = 0
    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
            count += 1
    print(f"Total images in '{folder}': {count}")


if __name__ == "__main__":
    count_images("data/raw_images")
