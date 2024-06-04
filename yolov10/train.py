import warnings

import torch.cuda

from ultralytics import YOLOv10
warnings.filterwarnings('ignore')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


if __name__ == '__main__':

    model = YOLOv10(r'./ultralytics/cfg/models/v10/yolov10s.yaml').load('yolov10s.pt')
    torch.cuda.empty_cache()
    model.train(
                data=r'../datasets/VOC.yaml',
                cache=True,  # 如果设置为True，在训练前将整个数据集加载到内存中，可以加速训练过程，但需要较多内存
                imgsz=640,  # 训练时输入图像的大小，这里设置为640x640像素。图像尺寸对模型性能和速度有重要影响
                epochs=200,  # 训练的总轮数，这里设置为100轮。一个epoch表示整个数据集被模型看过一次
                single_cls=False,  # 是否是单类别检测,如果设置为True，表示模型仅需要识别一种类别。
                # iou=0.6,
                lr0=0.001,
                batch=-1,
                #shear=0.2,
                #mixup=0.2,
                # close_mosaic=10,  # 是一个特定于YOLOv8的参数，用于控制何时停止使用mosaic数据增强（一种图像数据增强方法）
                # workers=0,  # 用于加载数据的工作线程数。设置为0表示数据加载将在主线程中进行。
                device='0',  # 指定训练使用的设备，'0'通常表示使用第一个GPU
                optimizer='Adam',
                )