from __future__ import absolute_import, division, print_function

import os

import argparse
import numpy as np
import PIL.Image as pil
import cv2

from utils.utils import readlines
# from kitti_utils import generate_depth_map


def export_gt_depths_kitti():

    parser = argparse.ArgumentParser(description='export_gt_depth')

    parser.add_argument('--data_path',
                        type=str,
                        help='path to the root of the KITTI data',
                        required=True)
    parser.add_argument('--split',
                        type=str,
                        help='which split to export gt from',
                        required=False,
                        default='endovis',
                        choices=["eigen", "eigen_benchmark", "endovis", "simcol", "endoslam",
                                 "endoslam/Colon", "endoslam/Small_Intestine", "endoslam/Stomach"])
    parser.add_argument('--useage',
                        type=str,
                        help='gt depth use for evaluation or 3d reconstruction',
                        required=False,
                        choices=["eval"])
    opt = parser.parse_args()

    split_folder = os.path.join(os.path.dirname(__file__), "splits", opt.split)
    lines = readlines(os.path.join(split_folder, "test_files.txt"))
    output_path = os.path.join(split_folder, "gt_depths.npz")
        
    print("Exporting ground truth depths for {}".format(opt.split))
    i=0
    gt_depths = []
    min_depth = 10000
    max_depth = 0
    for line in lines:
        i = i+1

        if opt.split == "endovis":
            folder, frame_id, _ = line.split()
            frame_id = int(frame_id)
            print(i)
            print(folder)
            f_str = "scene_points{:06d}.tiff".format(frame_id-1)
            sequence = folder[7]
            data_splt = "train" if int(sequence) < 8 else "test"
            
            gt_depth_path = os.path.join(
            opt.data_path, data_splt, folder, "data", "scene_points",
            f_str)

            gt_depth = cv2.imread(gt_depth_path, 3)
            gt_depth = gt_depth[:, :, 0]
            gt_depth = gt_depth[0:1024, :]

        else:
            raise NotImplementedError

        gt_depths.append(gt_depth.astype(np.float32))

    print(min_depth, max_depth)
    print("Saving to {}".format(opt.split))

    np.savez_compressed(output_path, data=np.array(gt_depths))


if __name__ == "__main__":
    export_gt_depths_kitti()
