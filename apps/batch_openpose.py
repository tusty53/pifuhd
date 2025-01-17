# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

import numpy as np

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--openpose_dir', type=str, required=True)
parser.add_argument('-i', '--input_root', type=str, required=True)
parser.add_argument('-o_j', '--out_path_json', type=str, required=True)
parser.add_argument('-o_i', '--out_path_image', type=str, required=True)
args = parser.parse_args()

op_dir = args.openpose_dir
input_path = args.input_root
out_path_json = args.out_path_json
out_path_image = args.out_path_image

os.makedirs(out_path_json, exist_ok=True)
os.makedirs(out_path_image, exist_ok=True)

cmd = "cd {0}; ./build/examples/openpose/openpose.bin --image_dir {1} --write_json {2} --render_pose 2 --face --face_render 2 --hand --hand_render 2  --display 0 --write_images {3}".format(op_dir, input_path, out_path_json, out_path_image)
print(cmd)
os.system(cmd)
