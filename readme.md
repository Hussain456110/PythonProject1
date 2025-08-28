🛡️ Thermal Pistol Detection using YOLOv11
This project focuses on detecting thermal pistols in images using a fine-tuned YOLOv11n model. The model is trained on a custom thermal image dataset of pistols, split into training, validation, and test sets. The repository includes code for training, evaluation, and inference, along with visualizations of model performance.

📑 Table of Contents
Overview

Dataset

Model

Setup

Training

Evaluation

Inference

Results

License

📌 Overview
The goal of this project is to detect thermal pistols in images using the YOLOv11n model. The model is fine-tuned on a custom dataset and evaluated for accuracy, precision, recall, and F1 score. The repository includes scripts for training, validation, and inference, as well as visualizations of dataset and model performance.

🗂️ Dataset
The dataset consists of thermal images of pistols, split into three subsets:

Train: 80% of the data

Validation: 10% of the data

Test: 10% of the data

Each image is accompanied by a corresponding YOLO-format label file containing bounding box annotations.

🧠 Model
The model used is YOLOv11n, a lightweight version of YOLOv11 architecture. The model is fine-tuned on the thermal pistol dataset.

🔍 Key Metrics
mAP50-95: 0.7281

Precision: 1.0000

Recall: 0.9964

F1 Score: 0.9982

⚙️ Setup
Clone the repository and install dependencies:

bash
Copy
Edit
git clone https://github.com/Alishan45/thermal-pistol-detection.git
cd thermal-pistol-detection
pip install -r requirements.txt
🏋️‍♂️ Training
bash
Copy
Edit
python train.py --data /path/to/dataset.yaml --epochs 100 --imgsz 640
📈 Evaluation
bash
Copy
Edit
python val.py --data /path/to/dataset.yaml --weights /path/to/best.pt
🔍 Inference
bash
Copy
Edit
python detect.py --weights /path/to/best.pt --source /path/to/image.jpg
📊 Results
Training metrics

Confusion Matrix

PR Curve

Sample Predictions

Ensure images like results.png, confusion_matrix.png are generated and saved in the correct directory.

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

📝 Additional Notes
Replace /path/to/ placeholders with actual file paths.

Update the GitHub repository URL with your real GitHub link:
https://github.com/Alishan45/thermal-pistol-detection.git

