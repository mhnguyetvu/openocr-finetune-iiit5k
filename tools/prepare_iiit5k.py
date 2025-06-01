import os
import scipy.io

def convert(mat_path, img_dir, out_txt):
    mat = scipy.io.loadmat(mat_path)
    labels = mat['labels'][0]
    with open(out_txt, 'w', encoding='utf-8') as f:
        for item in labels:
            img_name = item[0][0]
            label = item[1][0]
            f.write(f"{img_dir}/{img_name}\t{label}\n")

if __name__ == '__main__':
    convert('data/IIIT5K/traindata.mat', 'train', 'data/IIIT5K/rec_gt_train.txt')
    convert('data/IIIT5K/testdata.mat', 'test', 'data/IIIT5K/rec_gt_test.txt')
