#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:xvhuangjian   time:2022/9/6
import os
prompts = "Icebear of we bare bears holds a sign saying ’my fault‘"

# for i in prompts:
for i in range(100):
    os.system("python txt2img.py --prompt 'Icebear of We Bare Bears holds a sign, it says:'wtf'' --n_samples 6 --plms --outdir ../Workspace --ddim_steps 100 --ckpt ../models/ldm/stable-diffusion-v1/sd-v1-4-full-ema.ckpt --seed {}".format(i))

