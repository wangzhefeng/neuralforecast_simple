# -*- coding: utf-8 -*-

# ***************************************************
# * File        : tsdataset.py
# * Author      : Zhefeng Wang
# * Email       : wangzhefengr@163.com
# * Date        : 2024-04-12
# * Version     : 1.0.041217
# * Description : description
# * Link        : link
# * Requirement : 相关模块版本需求(例如: numpy >= 2.1.0)
# * TODO        : 1.
# ***************************************************

__all__ = [
    "TimeSeriesLoader",
    "TimeSeriesDataset",
    "TimeSeriesDataMoudle",
]

# python libraries
import os
import sys
ROOT = os.getcwd()
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# global variable
LOGGING_LABEL = __file__.split('/')[-1][:-3]







# 测试代码 main 函数
def main():
   pass

if __name__ == "__main__":
   main()
