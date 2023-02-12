#!/bin/bash
# 加载模块 
module load anaconda/2022.10
module load cuda/11.6
module load gcc/9.3

# 激活环境
source activate mmsegmentation

# 刷新⽇志缓存
export PYTHONUNBUFFERED=1

# 训练模型
python tools/train.py \
  configs/pspnet50/pspnet_r50_Glomeruli.py \
  --work-dir work/pspnet_r50_Glomeruli