#这个文件用于将XML转成txt供yolov7模型使用的
import glob
import xml.etree.ElementTree as ET
print('All started')

#类名
#选择输入路径
# path = '/scratch/uceezzz/Landfill_dataset/picture18/Annotation/'
path = '/scratch/uceezzz/Landfill_dataset/picture18/Annotation/'
#转换一个xml文件为txt
def single_xml_to_txt(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    #保存txt文件路径
    txt_file = xml_file.split('.')[0] + '.txt'
    with open(txt_file, 'w') as txt_file:
        for member in root.findall('object'):
	        #从xml获取图像的宽和高
            picture_width = int(root.find('size')[0].text)
            picture_height = int(root.find('size')[1].text)
            class_name = member[0].text

            #类名对应的index
            class_num = 0
            box_x_min = int(member[4][0].text)  # 左上角横坐标
            box_y_min = int(member[4][1].text)  # 左上角纵坐标
            box_x_max = int(member[4][2].text)  # 右下角横坐标
            box_y_max = int(member[4][3].text)  # 右下角纵坐标

            # 转成相对位置和宽高（所有值处于0~1之间）
            x_center = (box_x_min + box_x_max) / (2 * picture_width)
            y_center = (box_y_min + box_y_max) / (2 * picture_height)
            width = (box_x_max - box_x_min) / picture_width
            height = (box_y_max - box_y_min) / picture_height
            print(class_num, x_center, y_center, width, height)
            txt_file.write(str(class_num) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(
                height) + '\n')



#  转换文件夹下的所有xml文件为txt
def dir_xml_to_txt(path):
    for xml_file in glob.glob(path + '*.xml'):
        print(xml_file)
        single_xml_to_txt(xml_file)


dir_xml_to_txt(path)
print('All finished')