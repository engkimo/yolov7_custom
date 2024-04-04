# yolov7 for customization
To custom, this is base model of yolov7

## yolo annotate format

<img src="https://github.com/madara-tribe/custom-yolov7/assets/48679574/0a797a2a-8f71-4cdc-bbd7-b0800b3dd464" width="500px">

```python
# coco to yolo format
def coco_to_yolo(item):
    img_w, img_h = item['width'], item['height']
    x, y = item['bbox'][0], item['bbox'][1]
    w, h = item['bbox'][2], item['bbox'][3]
    x_centre = (x + (x+w))/2
    y_centre = (y + (y+h))/2
    x_centre = x_centre / img_w
    y_centre = y_centre / img_h
    w = w / img_w
    h = h / img_h
    return x_centre, y_centre, w, h
```

# How to use

Refer to <code>Makefile</code>

### train
```bash
# yolov7
python3 train.py --workers 1 --batch-size 4 --data data/origin.yaml --img 640 640 --mtype yolov7 --cfg cfg/training/yolov7.yaml --weights '' --name yolov7 --hyp data/hyp.scratch.p5.yaml
# aux
python3 train_aux.py --workers 0 --batch-size 4 --data data/origin.yaml --img 640 640 --mtype yolov7_aux --cfg cfg/training/yolov7-w6.yaml --weights '' --name yolov7-w6 --hyp data/hyp.scratch.p6.yaml
```

### test
```python
# yolov7
python3 test.py --data data/origin.yaml --img 640 --batch 4 --conf 0.001 --iou 0.65 --device 0 --weights <wight_path> --name yolov7_640_val
```

### detect
```
# yolov7
python3 detect.py --weights <wight_path> --conf 0.25 --img-size 640 --source <image_path>
```
### augument

```
python3 augment_data.py -i <image path> -l <label path> -o <output> -n <number of progress>
```
# ONNX Export

```
python3 export.py --weights <wight_path> --grid --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640 --max-wh 640
```

# plus
### shinkhorn yolov7
```
git clone -b shinkhorn <shinkhorn repogitory_url>
```

### References

- [augumentation](https://github.com/MinoruHenrique/data_augmentation_yolov7/blob/master/utils/dataaugmentation.py)
