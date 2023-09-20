#这个文件是我们要在大图里面标注出所有的检测到的lanfill
import json
import rasterio
from rasterio.features import bounds as featureBounds
from rasterio.windows import Window
from shapely.geometry import box as shapely_box
import numpy as np
from PIL import Image, ImageDraw, ImageFont

Image.MAX_IMAGE_PIXELS = None
# 读取tif图像
image = Image.open("/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/bj.tif")
with open("/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/output.txt", "r") as file:
    lines = file.readlines()
draw = ImageDraw.Draw(image)
# 如果需要在图像上显示文字，请提供一个字体文件
font = ImageFont.truetype("arial.ttf", 20)
for line in lines:
    data = json.loads(line)
    coordinates = data["coordinates"]
    confidence = data["confidence"]

    # 画出box
    draw.rectangle(coordinates, outline="red", width=2)

    # 添加confidence
    text = f"{confidence:.2f}"
    draw.text((coordinates[0], coordinates[1] - 20), text, fill="red", font=font)
    print('Fininsed one box')
# 保存结果图像
print('Saving new tif')
# 保存结果图像
image.save("/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/bj_box.jpg",quality=10)


