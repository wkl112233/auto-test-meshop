import os

"""获取当前文件的上一层目录的绝对路径"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
