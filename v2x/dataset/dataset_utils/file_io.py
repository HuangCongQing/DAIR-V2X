'''
Description: 文件加载和保存
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-12-10 16:52:26
LastEditTime: 2022-12-11 17:34:28
FilePath: \DAIR-V2X\v2x\dataset\dataset_utils\file_io.py
'''
import json
import yaml
import pickle
import numpy as np
from pypcd import pypcd
import mmcv


def load_json(path):
    with open(path, mode="r") as f:
        data = json.load(f)
    return data


def load_yaml(path):
    with open(path, "r") as f:
        data = yaml.load(f)
    return data


def load_pkl(path):
    with open(path, "rb") as f:
        return pickle.load(f)

# 保存pkl
def save_pkl(item, path):
    with open(path, "wb") as f:
        pickle.dump(item, f)
# 保存json
def save_json(item, path):
    with open(path, "w") as f:
        json.dump(item, f)



def read_pcd(pcd_path):
    pcd = pypcd.PointCloud.from_path(pcd_path)
    time = None
    pcd_np_points = np.zeros((pcd.points, 4), dtype=np.float32)
    pcd_np_points[:, 0] = np.transpose(pcd.pc_data["x"])
    pcd_np_points[:, 1] = np.transpose(pcd.pc_data["y"])
    pcd_np_points[:, 2] = np.transpose(pcd.pc_data["z"])
    pcd_np_points[:, 3] = np.transpose(pcd.pc_data["intensity"]) / 256.0
    del_index = np.where(np.isnan(pcd_np_points))[0]
    pcd_np_points = np.delete(pcd_np_points, del_index, axis=0)
    return pcd_np_points, time


def read_jpg(jpg_path):
    image = mmcv.imread(jpg_path)
    return image
