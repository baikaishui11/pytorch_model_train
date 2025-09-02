import torch

# Load a YOLOv5 model (options: yolov5n, yolov5s, yolov5m, yolov5l, yolov5x)
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

# Define the input image source (URL, local file, PIL image, OpenCV frame, numpy array, or list)
img = "https://ultralytics.com/images/zidane.jpg"  # Example image

# Perform inference (handles batching, resizing, normalization automatically)
results = model(img)

# Process the results (options: .print(), .show(), .save(), .crop(), .pandas())
results.print()  # Print results to console
results.show()  # Display results in a window
results.save()  # Save results to runs/detect/exp

# python detect.py --weights runs/train/exp8/weights/best.pt --source 0
# python train.py --data mask.yaml --cfg yolov5s.yaml --weights yolov5s.pt --epoch 50 --batch-size 4
