# 校验文件类型为图片
from PIL import Image


def is_image(file):
    try:
        Image.open(file)
        return True
    except:
        return False
