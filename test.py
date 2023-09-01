import os
import math
# import wandb
import json
import tome
import timm
import torch
import random
import argparse

import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torchvision.datasets as datasets
import torch.distributed as dist

from tqdm import tqdm
from torchvision import transforms

import DiffRate
from pprint import pprint

model_name = "deit_small_patch16_224.fb_in1k"
model = timm.create_model(model_name, pretrained=True)
DiffRate.patch.deit(model, prune_granularity=4, merge_granularity=4)
# model = model.cuda()
print('done')