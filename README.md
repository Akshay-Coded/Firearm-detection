# Firearm-detection

An end-to-end firearm detection project using YOLO-style object detection.  
This repo contains data-scraping and preprocessing scripts, sample annotated data, a trained YOLOv8 weight (`yolov8s.pt`), and prediction/demo assets (`test.mp4`, `result.mp4`, etc.).

> **Note:** This README assumes use of Ultralytics YOLOv8 (or compatible detection scripts). Adjust commands if you use another framework.

---

## Table of Contents

- [Features](#features)  
- [Repository structure](#repository-structure)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Data preparation](#data-preparation)  
- [Training](#training)  
- [Inference / Prediction](#inference--prediction)  
- [Scripts (what they do)](#scripts-what-they-do)  
- [Results & demos](#results--demos)  
- [Notes & best practices](#notes--best-practices)  
- [License & contact](#license--contact)

---

## Features

- End-to-end flow from scraping firearm images to training and inference.
- Preprocessing utilities to convert / count images and prepare annotation sets.
- Included trained weights: `yolov8s.pt` (example model file present in repo).
- Demo videos (`test.mp4`, `result.mp4`) showing detection output.

---

## Repository structure

```
.
├── data_annotated/         # (annotated dataset - YOLO format expected)
├── data_sample/            # (sample images)
├── predict/                # prediction utilities / demo scripts
├── runs/                   # example runs / results (from detection)
├── count_img.py            # count images in folders
├── data_processing.py      # dataset processing & conversion helpers
├── scrape_firearm_image.py # script to scrape firearm images from web
├── yolov8s.pt              # pretrained / exported weights included (example)
├── test.mp4                # demo input video
├── result.mp4              # demo output video (predictions)
└── README.md               # <-- add this file
```

---

## Requirements

- Python **3.8+**
- Recommended packages (install via pip). If a `requirements.txt` is not present, install the essentials:

```bash
pip install ultralytics opencv-python numpy pandas tqdm matplotlib requests beautifulsoup4
```

- GPU recommended (CUDA) for training. CPU works for inference/testing but will be slower.

---

## Installation

1. Clone the repo (if you haven't already):
```bash
git clone https://github.com/Akshay-Coded/Firearm-detection.git
cd Firearm-detection
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# mac/linux
source venv/bin/activate
# windows (powershell)
.\venv\Scripts\Activate.ps1
```

3. Install requirements:
```bash
pip install -r requirements.txt  # if you add one
# or install the minimal set manually:
pip install ultralytics opencv-python numpy pandas tqdm matplotlib requests beautifulsoup4
```

---

## Data preparation

- `data_annotated/` is expected to contain images and `.txt` label files in YOLO format:
  - Each image `image.jpg` should have a corresponding `image.txt` with lines:
    ```
    <class_id> <x_center> <y_center> <width> <height>
    ```
    (All normalized between 0 and 1.)

- Useful helper scripts:
  - `scrape_firearm_image.py` — scrape firearm images from the web (edit query, pages, output folder).
  - `data_processing.py` — utilities for converting and organizing annotations (open to customization).
  - `count_img.py` — quickly count images/annotations per folder.

**Tip:** Verify annotations visually (few sample images) before training.

---

## Training

This repo ships with `yolov8s.pt` (a trained weight). If you want to retrain or fine-tune:

### Using Ultralytics YOLOv8 CLI
1. Create a `data.yaml` file describing your dataset:
```yaml
train: path/to/train/images
val:   path/to/val/images
nc: 1            # number of classes (e.g. firearms)
names: ['firearm']
```

2. Run training:
```bash
# with ultralytics installed (yolo CLI)
yolo detect train model=yolov8s.pt data=data.yaml epochs=50 imgsz=640 name=firearm-run
```

Or start from a prebuilt YOLOv8 config (e.g., `yolov8s.pt` as base) or from `yolov8n.yaml` if available.

### Or using a `train.py` script
If you prefer a script-based approach, adapt Ultralytics example training code and point it to `data.yaml`.

---

## Inference / Prediction

### Quick CLI (Ultralytics)
```bash
# Predict on an image:
yolo detect predict model=yolov8s.pt source=path/to/image.jpg

# Predict on a video:
yolo detect predict model=yolov8s.pt source=test.mp4 save=True

# Predict on a webcam (replace 0 with your device index):
yolo detect predict model=yolov8s.pt source=0
```

### Using `predict/` scripts
If the repo contains `predict/detect.py` or similar:
```bash
python predict/detect.py --weights yolov8s.pt --source test.mp4 --save
```
(Adjust argument names to the script's interface.)

Output predictions will typically appear in `runs/detect/` with images or a processed video.

---

## Scripts — what they do

- `scrape_firearm_image.py`  
  Simple web-scraper to gather firearm images. Edit keywords, output folder, or scraping limits before running.

- `data_processing.py`  
  Functions to convert, clean, or reorganize dataset folders and annotations into the format required for training.

- `count_img.py`  
  Counts images and (optionally) labels across dataset folders — useful to check dataset balance and presence of missing labels.

- `predict/`  
  Folder containing project-specific inference utilities and demo scripts.

---

## Results & demos

- `test.mp4` — sample input video (demo).
- `result.mp4` — demo output showing firearm detection (committed example).
- `runs/detect/` — example detection run outputs (images/videos with boxes).

---

## Notes & Best Practices

- **Ethics & legal:** Firearm detection models can have safety, privacy, and legal implications. Use only in accordance with applicable laws, institutional policies, and ethical guidelines. Obtain consent when collecting data involving people, and avoid deploying without testing and appropriate safeguards.
- **Data quality:** Model performance depends heavily on the dataset: varied viewpoints, lighting, occlusion, and negative samples are important.
- **Evaluation:** Use held-out validation data and metrics such as mAP@0.5, precision, recall to evaluate model behavior.
- **Edge performance:** For real-time edge or embedded deployment, test smaller models (e.g., `yolov8n`) and perform model pruning/quantization.

---

## License

Add a license file (e.g., `LICENSE` — MIT or other) if you want this repo to be reused. This README does not enforce a license.

---

## Contact

If you want to reach the repository owner:  
**Akshay** — GitHub: https://github.com/Akshay-Coded

(If you'd like an email address added to this README, tell me what to include and I'll update it.)
