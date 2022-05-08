#!/usr/bin/env Python
# -*- coding: utf-8 -*-
"""
@author: 陈 子坤 (GitHub@sandyzikun)
@title: Instance 04-4 tqdm
@time: 2022-03-29 16:14:39
"""
import time, tqdm
if __name__ == "__main__":
    for k in tqdm.trange(1, 100):
        time.sleep(0.01)