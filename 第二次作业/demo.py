from mmdet.apis import init_detector, inference_detector
import mmcv

# 下载的配置文件放在 `/HOME/scz0bet/run/mmdetection` 文件下
config_file = 'mask_rcnn_r50_fpn_2x_coco.py'
# 参数文件 同级目录写上文件名即可
checkpoint_file = 'mask_rcnn_r50_fpn_2x_coco_bbox_mAP-0.392__segm_mAP-0.354_20200505_003907-3e542a40.pth'
device = 'cpu'
# 初始化检测器
model = init_detector(config_file, checkpoint_file, device=device)

# 推理演示图像
result = inference_detector(model, 'demo/demo.jpg')

model.show_result('demo/demo.jpg', result, out_file='result.jpg')
