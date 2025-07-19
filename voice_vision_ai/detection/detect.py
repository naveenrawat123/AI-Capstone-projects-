import torch
from pathlib import Path
import yaml

def run_yolo(image_path, target_object):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='detection/model/yolov5s.pt')
    results = model(image_path)
    labels = results.names
    preds = results.pred[0]
    for *box, conf, cls in preds:
        label = labels[int(cls)]
        if target_object.lower() in label.lower():
            return True, box
    return False, None