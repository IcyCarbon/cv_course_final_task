import warnings

import torch.cuda

from ultralytics import YOLOv10
warnings.filterwarnings('ignore')
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


if __name__ == '__main__':

    model = YOLOv10(r'.\ultralytics\cfg\models\v10\yolov10n.yaml').load('yolov10n.pt')
    torch.cuda.empty_cache()
    model.train(
                data=r'..\datasets\VOC.yaml',
                cache=True,  # 如果设置为True，在训练前将整个数据集加载到内存中，可以加速训练过程，但需要较多内存
                imgsz=640,  # 训练时输入图像的大小，这里设置为640x640像素。图像尺寸对模型性能和速度有重要影响
                epochs=100,  # 训练的总轮数，这里设置为100轮。一个epoch表示整个数据集被模型看过一次
                single_cls=False,  # 是否是单类别检测,如果设置为True，表示模型仅需要识别一种类别。
                batch=4,  # 批大小，每次迭代训练所用的样本数量。这里设置为1，通常较小的批大小会使训练过程更稳定，但可能会增加训练时间
                # close_mosaic=10,  # 是一个特定于YOLOv8的参数，用于控制何时停止使用mosaic数据增强（一种图像数据增强方法）
                # workers=0,  # 用于加载数据的工作线程数。设置为0表示数据加载将在主线程中进行。
                device='0',  # 指定训练使用的设备，'0'通常表示使用第一个GPU
                # optimizer='SGD',  # using SGD,选择优化器，这里使用SGD（随机梯度下降）
                # amp=False,  # 自动混合精度训练，可以提高训练速度和效率，同时减少内存使用。如果训练中出现损失为NaN，可以关闭此功能
                )