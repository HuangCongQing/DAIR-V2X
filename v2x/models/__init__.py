'''
Description: late_fusion 测试
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-12-10 16:52:26
LastEditTime: 2022-12-11 17:08:33
FilePath: \DAIR-V2X\v2x\models\__init__.py
'''
import sys
import os
import os.path as osp

sys.path.append("..")
sys.path.extend([os.path.join(root, name) for root, dirs, _ in os.walk("../") for name in dirs])

from detection_models import *

# 5中支持模型方式
SUPPROTED_MODELS = {
    "single_side": SingleSide,
    "late_fusion": LateFusion, # main v2x\models\detection_models\mmdet3d_anymodel_anymodality_late.py
    "early_fusion": EarlyFusion,
    "veh_only": VehOnly,
    "inf_only": InfOnly,
}
