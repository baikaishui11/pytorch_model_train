# 用yolov5训练口罩训练集并部署
## 装yolov5所需环境
```python
pip install -r requirements.txt
```
## 测试环境是否正常
```python
python test.py
```
## 下载口罩数据集msak并解压在datasets文件夹中
[链接](https://pan.baidu.com/s/1oh5e8cRAWXXClLB0ZRlmHw?pwd=vzfa)
## 在yolov5_mask里data文件夹中新建mask.yaml文件，并写入以下代码：
```python
train: ../datasets/mask/images # 训练集存放地址
val: ../datasets/mask/images # 数据集存放地址
nc: 2 # 总类别
names: ['face', 'mask'] # 类别名称
```
## 修改models文件夹下的yolov5s.yaml文件将nc改为2
## 运行以下程序，可适当修改epoch和batch-size
```python
python train.py --data mask.yaml --cfg yolov5s.yaml --weights yolov5s.pt --epoch 8 --batch-size 4
```
## 将runs/train/exp/weights文件中训练好的weights部署并用摄像头测试
```python
python detect.py --weights runs/train/exp8/weights/best.pt --source 0
```
