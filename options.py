from __future__ import absolute_import, division, print_function

import os
import argparse

file_dir = os.path.dirname(__file__)  # the directory that options.py resides in

def str2bool(v):
     if isinstance(v, bool):
          return v
     if v.lower() in ('yes', 'true', 't', 'y', '1'):
          return True
     elif v.lower() in ('no', 'false', 'f', 'n', '0'):
          return False
     else:
          raise argparse.ArgumentTypeError('Boolean value expected.')

class MonodepthOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Monodepthv2 options")

        # PATHS
        self.parser.add_argument("--data_path",
                                 type=str,
                                 help="path to the training data",
                                 default=os.path.join(file_dir, "endovis_data"))
        self.parser.add_argument("--log_dir",
                                 type=str,
                                 help="log directory",
                                 default=os.path.join(os.path.expanduser("~"), "tmp"))

        # Model options
        self.parser.add_argument("--pretrained_path",
                                 type=str,
                                 help="pretrained weights path",
                                 default=os.path.join(file_dir, "pretrained_model"))
        self.parser.add_argument("--lora_type",
                                 type=str,
                                 help="which lora type use for the model",
                                 choices=["dvlora", "part-dvlora"],
                                 default="dvlora")
        self.parser.add_argument("--lora_rank",
                                 type=int,
                                 help="the rank of lora",
                                 default=4)
        self.parser.add_argument("--warm_up_step",
                                 type=int,
                                 help="warm up step",
                                 default=20000)
        self.parser.add_argument("--residual_block_indexes",
                                 nargs="*",
                                 type=int,
                                 help="indexes for residual blocks in vitendodepth encoder",
                                 default=[2,5,8,11])
        self.parser.add_argument("--include_cls_token",
                                 type=str2bool,
                                 help="includes the cls token in the transformer blocks",
                                 default=True)
        self.parser.add_argument("--learn_intrinsics",
                                 type=str2bool,
                                 help="learn the camera intrinsics with a seperate decoder",
                                 default=True)

        # SYSTEM options
        self.parser.add_argument("--no_cuda",
                                 help="if set disables CUDA",
                                 action="store_true")
        self.parser.add_argument("--num_workers",
                                 type=int,
                                 help="number of dataloader workers",
                                 default=8)

        # LOADING options
        self.parser.add_argument("--load_weights_folder",
                                 type=str,
                                 help="name of model to load")
        self.parser.add_argument("--models_to_load",
                                 nargs="+",
                                 type=str,
                                 help="models to load",
                                 default=["position_encoder", "position"])

        # EVALUATION options
        self.parser.add_argument("--model_type",
                                 type=str,
                                 help="which training split to use",
                                 choices=["endomust", "afsfm", "depthanything", "pcc"],
                                 default="endomust")
        self.parser.add_argument("--eval_stereo",
                                 help="if set evaluates in stereo mode",
                                 action="store_true")
        self.parser.add_argument("--eval_mono",
                                 help="if set evaluates in mono mode",
                                 action="store_true")
        self.parser.add_argument("--disable_median_scaling",
                                 help="if set disables median scaling in evaluation",
                                 action="store_true")
        self.parser.add_argument("--pred_depth_scale_factor",
                                 help="if set multiplies predictions by this number",
                                 type=float,
                                 default=1)
        self.parser.add_argument("--ext_disp_to_eval",
                                 type=str,
                                 help="optional path to a .npy disparities file to evaluate")
        self.parser.add_argument("--eval_split",
                                 type=str,
                                 default="endovis",
                                 choices=[
                                    "hamlyn", "endovis"],
                                 help="which split to run eval on")
        self.parser.add_argument("--save_pred_disps",
                                 help="if set saves predicted disparities",
                                 action="store_true")
        self.parser.add_argument("--visualize_depth",
                                 help="if set saves visualized depth map",
                                 action="store_true")
        self.parser.add_argument("--no_eval",
                                 help="if set disables evaluation",
                                 action="store_true")
        self.parser.add_argument("--eval_eigen_to_benchmark",
                                 help="if set assume we are loading eigen results from npy but "
                                      "we want to evaluate using the new benchmark.",
                                 action="store_true")
        self.parser.add_argument("--eval_out_dir",
                                 help="if set will output the disparities to this folder",
                                 type=str)
        self.parser.add_argument("--post_process",
                                 help="if set will perform the flipping post processing "
                                      "from the original monodepth paper",
                                 action="store_true")

        # EVALUATION options
        self.parser.add_argument("--save_recon",
                                 help="if set saves reconstruction files",
                                 action="store_true")
    def parse(self):
        self.options = self.parser.parse_args()
        return self.options
