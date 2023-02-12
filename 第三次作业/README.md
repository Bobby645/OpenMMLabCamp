# 小鼠肾小球切片语义分割

## 训练模型的配置文件
pspnet_r50_Glomeruli.py

## 模型日志文件
20230211_235645.log

## 模型性能

   |   Class    |  IoU  |  Acc  |
   | :--------: | :---: | :---: |
   | background | 99.36 | 99.85 |
   | glomeruili | 69.45 | 74.95 |

aAcc: 99.3700  mIoU: 84.4100  mAcc: 87.4000

## 模型测试：
原图：

<img src = "https://user-images.githubusercontent.com/84892024/218291727-0e233eda-2e99-4391-9a1d-26954e55cdab.png" width=50%>

mask:

<img src = "https://user-images.githubusercontent.com/84892024/218291744-fe17dea9-0767-4e7b-869e-c52b9108118d.png" width=50%>

预测图：

<img src = "https://user-images.githubusercontent.com/84892024/218291730-86836791-1579-4e71-ad17-6ed832fb3a0c.jpg" width=50%>

## 模型文件
谷歌云盘：https://drive.google.com/file/d/1448lY76oQFFZ44AsKN0-VBA82rT5XnXI/view?usp=share_link

代码测试[云GPU环境，北京超算]：sys.platform: linux
GPU RTX 3090、CUDA v11.6 、GCC:9.3.0

PyTorch: 1.13.1

MMEngine: 0.5.0

mmcv：2.0.0rc4

mmdet ：3.0.0rc5

mmsegmentation：1.0.0rc5

## 知乎笔记链接
https://zhuanlan.zhihu.com/p/605279581

