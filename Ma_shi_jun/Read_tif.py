#读取一个tif图像并输出它的尺寸
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
def get_tiff_dimensions(file_path):
    with Image.open(file_path) as img:
        width, height = img.size
    return width, height

tif_path = "/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/bj.tif"
width, height = get_tiff_dimensions(tif_path)
print(f"Image dimensions: Width = {width}, Height = {height}")