
# OpenOCR Finetune on IIIT5K

## 1. Data Preparation
Unzip IIIT5K, then convert to txt :

```bash
python tools/prepare_iiit5k.py \
  --mat_path data/IIIT5K/traindata.mat \
  --img_dir data/IIIT5K/train \
  --out_path data/IIIT5K/train.txt

python tools/prepare_iiit5k.py \
  --mat_path data/IIIT5K/testdata.mat \
  --img_dir data/IIIT5K/test \
  --out_path data/IIIT5K/val.txt
```

## 2. Create LMDB (optional)
```bash
python tools/create_lmdb_dataset.py \
  --input_txt data/IIIT5K/train.txt \
  --output_path data/IIIT5K/train_lmdb

python tools/create_lmdb_dataset.py \
  --input_txt data/IIIT5K/val.txt \
  --output_path data/IIIT5K/val_lmdb
```

## 3. Train
```bash
bash scripts/train.sh
```
