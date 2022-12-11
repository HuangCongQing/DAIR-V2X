from dair_v2x_for_detection import *
from dataset_utils import *

# 四种数据类型
SUPPROTED_DATASETS = {
    "dair-v2x-v": DAIRV2XV,
    "dair-v2x-i": DAIRV2XI,
    "vic-sync": VICSyncDataset, # 同步融合
    "vic-async": VICAsyncDataset, # 当前main异步  vic-async
}
