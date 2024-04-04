train:
	python3 ./train.py --workers 8 --device 0 --batch-size 1 --epochs 300 --data ./original_dataset/mydata.yaml --cfg ./cfg/training/yolov7.yaml --weight ./yolov7.pt --name yolov7 --hyp ./data/hyp.scratch.p5.yaml
test:
	python3 test.py --data ./original_dataset/mydata.yaml --img 640 --batch 1 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/weights/best.pt --name yolov7_640_val
detect:
	python3 detect.py --weights runs/train/yolov7/weights/best.pt --conf 0.25 --img-size 640 --source inference/images/road284.png

onnx:
	python3 export.py --weights runs/train/yolov7/weights/best.pt --grid --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640 --max-wh 640

aug:
	python3 augment_data.py -i original_dataset/train/images -l original_dataset/train/labels -o original_dataset/aug -n 2

train_aux:
	python3 train_aux.py --workers 0 --batch-size 1 --data ./original_dataset/mydata.yaml --img 640 --cfg cfg/training/yolov7-w6.yaml --weights '' --name yolov7-w6 --hyp data/hyp.scratch.p6.yaml
test_aux:
	python3 test.py --data data/origin.yaml --img 640 --batch 4 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/yolov7-w6/weights/best.pt --name yolov7_640_val_aux
detect_aux:
	python3 detect.py --weights runs/train/yolov7-w6/weights/best.pt --conf 0.25 --img-size 640 --source inference/images/road284.png
onnx_aux:
	python3 export.py --weights runs/train/yolov7-w6/weights/best.pt --grid --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640 --max-wh 640
