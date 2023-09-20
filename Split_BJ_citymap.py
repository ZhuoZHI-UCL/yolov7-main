#这个文件是把bj那个巨大的tif图给切割成640*640的小图并给每个小图生成对应的一个txt文件，
#该文件中包含了这个小图的起始坐标信息以及该小图的尺寸信息
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

def split_image(image_path, output_folder, tile_size=(640, 640)):
    image = Image.open(image_path)
    img_width, img_height = image.size

    total_tiles_x = (img_width + tile_size[0] - 1) // tile_size[0]
    total_tiles_y = (img_height + tile_size[1] - 1) // tile_size[1]
    total_tiles = total_tiles_x * total_tiles_y

    tile_counter = 0
    for y in range(0, img_height, tile_size[1]):
        for x in range(0, img_width, tile_size[0]):
            tile = image.crop((x, y, x + tile_size[0], y + tile_size[1]))
            tile_name = f"tile_{x}_{y}"
            tile.save(f"{output_folder}/{tile_name}.tif")

            # 保存起始坐标和尺寸信息到txt文件
            with open(f"{output_folder}/{tile_name}.txt", "w") as f:
                f.write(f"start_x: {x}\n")
                f.write(f"start_y: {y}\n")
                f.write(f"width: {tile_size[0]}\n")
                f.write(f"height: {tile_size[1]}\n")
            tile_counter += 1
            print(f"Processing tile {tile_counter} of {total_tiles}")

if __name__ == "__main__":
    input_image_path = "/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/bj.tif"
    output_folder = "/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/splited_image"
    # 创建输出目录，如果不存在
    import os
    import shutil
    if os.path.exists(output_folder):
        #清空文件夹
        for file in os.listdir(output_folder):
            file_path = os.path.join(output_folder, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    split_image(input_image_path, output_folder)