CUDA_VISIBLE_DEVICES=0 python -m torch.distributed.launch --nproc_per_node=1 \
  tools/train_rec.py \
  --c configs/rec_finetune_iiit5k.yml \
  --o Global.pretrained_model=./openocr_repsvtr_ch.pth