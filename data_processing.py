import os
import hashlib
from PIL import Image

# === CONFIG ===
source_dir = "data/raw_images"  # Folder with raw downloaded images
output_dir = "data/processed_images"  # Where cleaned images will be stored
image_size = (614, 614)  # Resize target (width, height)

# === CREATE OUTPUT FOLDER ===
os.makedirs(output_dir, exist_ok=True)

# === HASH SET TO IDENTIFY DUPLICATES ===
seen_hashes = set()
count = 0

# === PROCESS IMAGES ===
for filename in os.listdir(source_dir):
    filepath = os.path.join(source_dir, filename)

    try:
        # Open and convert image to RGB
        with Image.open(filepath).convert("RGB") as img:
            # Compute hash to detect duplicates
            file_hash = hashlib.md5(img.tobytes()).hexdigest()
            if file_hash in seen_hashes:
                print(f"[DUPLICATE] Skipping: {filename}")
                continue
            seen_hashes.add(file_hash)

            # Resize image
            img = img.resize(image_size, Image.Resampling.LANCZOS)

            # Save with sequential name
            new_filename = f"firearm_{count:04d}.jpg"
            save_path = os.path.join(output_dir, new_filename)
            img.save(save_path)

            print(f"[OK] Saved: {new_filename}")
            count += 1

    except Exception as e:
        print(f"[ERROR] Skipping {filename}: {e}")
