DATA="../data/DAIR-V2X/cooperative-vehicle-infrastructure" # 数据集路径
OUTPUT="../cache/vic-late-lidar" # 输出eval结果
rm -r $OUTPUT
rm -r ../cache
mkdir -p $OUTPUT/result
mkdir -p $OUTPUT/inf/lidar
mkdir -p $OUTPUT/veh/lidar

INFRA_MODEL_PATH="../configs/vic3d/late-fusion-pointcloud/pointpillars"
INFRA_CONFIG_NAME="trainval_config_i.py"
INFRA_MODEL_NAME="vic3d_latefusion_inf_pointpillars_596784ad6127866fcfb286301757c949.pth" # 权重文件

VEHICLE_MODEL_PATH="../configs/vic3d/late-fusion-pointcloud/pointpillars"
VEHICLE_CONFIG_NAME="trainval_config_v.py"
VEHICLE_MODEL_NAME="vic3d_latefusion_veh_pointpillars_a70fa05506bf3075583454f58b28177f.pth"# 权重文件

SPLIT_DATA_PATH="../data/split_datas/cooperative-split-data.json"

# srun --gres=gpu:a100:1 --time=1-0:0:0 --job-name "dair-v2x" \
CUDA_VISIBLE_DEVICES=$1
FUSION_METHOD=$2 # late_fusion (veh_only,inf_only,late_fusion,early_fusion)
DELAY_K=$3 # 2
EXTEND_RANGE_START=$4 # 0m
EXTEND_RANGE_END=$5 # 100m
TIME_COMPENSATION=$6
# 运行eval.py
# bash scripts/eval_lidar_late_fusion_pointpillars.sh 0 late_fusion 2 0 100
python eval.py \
  --input $DATA \
  --output $OUTPUT \
  --model $FUSION_METHOD \ # veh_only,inf_only,late_fusion,early_fusion
  --dataset vic-async \ #  Choices are dair-v2x-v, dair-v2x-i,vic-sync and vic-async.
  --k $DELAY_K \  # 2 the number of previous frames for vic-async dataset. vic-async-0 is equivalent to vic-sync dataset.
  --split val \ # val test_A
  --split-data-path $SPLIT_DATA_PATH \
  --inf-config-path $INFRA_MODEL_PATH/$INFRA_CONFIG_NAME \
  --inf-model-path $INFRA_MODEL_PATH/$INFRA_MODEL_NAME \
  --veh-config-path $VEHICLE_MODEL_PATH/$VEHICLE_CONFIG_NAME \
  --veh-model-path $VEHICLE_MODEL_PATH/${VEHICLE_MODEL_NAME} \
  --device ${CUDA_VISIBLE_DEVICES} \
  --pred-class car \
  --sensortype lidar \
  --extended-range $EXTEND_RANGE_START -39.68 -3 $EXTEND_RANGE_END 39.68 1 \
  --overwrite-cache \
  $TIME_COMPENSATION