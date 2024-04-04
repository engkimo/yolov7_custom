import json
import os
from pathlib import Path
import sys
import glob
import cv2
import numpy as np
from PIL import Image

def draw_boxes(image, boxes):
    for box in zip(boxes):
        print(box)
        label, x, y, w, h = box[0]
        cv2.rectangle(image, (x, y), (x+w, y+h), (), 2)
        # red
        cv2.putText(image, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2)
        
def change(dataset_path):
    save_dir = 'box'
    for json_path in (dataset_path / 'data').glob("*.json"):
        buff = []
        bbs = []
        ids = os.path.splitext(os.path.basename(json_path))[0]
        jdata = json.load(json_path.open())
        image_path = os.path.join(os.path.dirname(json_path), str(ids)+'.jpg')
        #print(image_path)
        image = np.asarray(Image.open(image_path))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # W, H = item['width'], item['height']
        for item in jdata:
            x, y, w, h = item['bbox'][0], item['bbox'][1], item['bbox'][2], item['bbox'][3]
            label = item['label']
            buff.append("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(label, x, y, w, h))
            bbs.append([label, x, y, w, h])
        draw_boxes(image, bbs)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        cv2.imwrite(os.path.join(save_dir, f'{ids}.jpg'), image)
        print("\n".join(buff), file=open(os.path.join(save_dir, f'{ids}.txt'), "w"))
        
        
name = 'folder_name'
dataset_path = Path(name)
change(dataset_path)

