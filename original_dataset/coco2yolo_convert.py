import json
from pathlib import Path
import os
import sys
import glob

def coco_to_yolo(item):
    img_w, img_h = item['width'], item['height']
    #1200, 900
    x = item['bbox'][0]
    y = item['bbox'][1]
    w = item['bbox'][2]
    h = item['bbox'][3]
    x_centre = (x + (x+w))/2
    y_centre = (y + (y+h))/2
    x_centre = x_centre / img_w
    y_centre = y_centre / img_h
    w = w / img_w
    h = h / img_h
    return x_centre, y_centre, w, h
    
def yolo_to_coco(b_center_x, b_center_y, w, h):
    image_w, image_h = 1200, 900
    #1200, 900
    x = b_center_x - (w/2)
    y = b_center_y - (h/2)
    
    x *= image_w
    y *= image_h
    w *= image_w
    h *= image_h
    return x, y, w, h
    
NUM_CLS = 5
def change(dataset_path):
    for cls in range(NUM_CLS):
        print(cls)
    #"""
        for json_path in (dataset_path / str(cls)).glob("*.json"):
            print_buffer = []
            j = json.load(json_path.open())
            for item in j:
                class_id = int(cls)
                b_center_x, b_center_y, b_width, b_height = coco_to_yolo(item)
                print_buffer.append("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(class_id, b_center_x, b_center_y, b_width, b_height))
            fname = os.path.basename(json_path).replace("json", "txt")
            save_path = os.path.join(dataset_path, str(cls))
            #print(json_path, print_buffer, os.path.join(save_path, fname))
            print("\n".join(print_buffer), file=open(os.path.join(save_path, fname), "w"))
            os.system("rm {}".format(os.path.join(save_path, os.path.basename(json_path))))
    #"""
name = 'train'
dataset_path = Path(name)
change(dataset_path)

