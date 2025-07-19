# This is a wrapper script. Assumes yolov5 repo is installed and in PYTHONPATH.
import os

def train_yolo():
    os.system("python yolov5/train.py --img 640 --batch 16 --epochs 100 --data training/custom.yaml --weights yolov5s.pt")

if __name__ == "__main__":
    train_yolo()