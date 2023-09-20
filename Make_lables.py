#由于我们的label现在是乱的，要从所有的里面选出image中test，train,val对应的label放进各自的文件夹
#我们已经使用了XML_TXT文件来制作txt的标注，接下来挑选一样的放进各自的文件夹
import os
import shutil
print('All started')

#分别找到test,train,val文件夹中的名字
def place_label_2_threefolder(path):
    # image_val_path=os.path.join(dir_father,'images/val/')
    image_test_path=os.path.join(dir_father,'images/test/')
    image_train_path=os.path.join(dir_father,'images/train/')
    all_annotation_path=os.path.join(dir_father,'Annotation/')
    #遍历各自文件夹下面的文件名存为列表并去掉文件类型名称
    filename_list_image_val=[]
    filename_list_image_test=[]
    filename_list_image_train=[]
    filename_list_annotation=[]
    # for file in os.listdir(image_val_path):
    #     filename_list_image_val.append(file.split('.')[0])  # 文件名放入列表内
    for file in os.listdir(image_test_path):
        filename_list_image_test.append(file.split('.')[0])  # 文件名放入列表内
    for file in os.listdir(image_train_path):
        filename_list_image_train.append(file.split('.')[0])  # 文件名放入列表内
    for file in os.listdir(all_annotation_path):
        filename_list_annotation.append(file.split('.')[0])  # 文件名放入列表内

    #便利Annotation文件夹，然后把val,test,train三个文件夹中有的注释给移过去，如果没有的话打印出文件名：
    #首先是清空下面的所有文件
    # shutil.rmtree(dir_father+'labels/val')
    # os.mkdir(dir_father+'labels/val')
    shutil.rmtree(dir_father+'labels/test')
    os.mkdir(dir_father+'labels/test')
    shutil.rmtree(dir_father+'labels/train')
    os.mkdir(dir_father+'labels/train')

    # for file_name in filename_list_image_val:
    #     if file_name in filename_list_annotation:
    #         file_anna_path=os.path.join(all_annotation_path,file_name+'.txt')
    #         shutil.copyfile(file_anna_path,os.path.join(dir_father+'labels/val/',file_name+'.txt'))
    #     else:
    #         print(image_val_path)
    #         print(file_name,'not find in annotation')

    for file_name in filename_list_image_test:
        if file_name in filename_list_annotation:
            file_anna_path=os.path.join(all_annotation_path,file_name+'.txt')
            shutil.copyfile(file_anna_path,os.path.join(dir_father+'labels/test/',file_name+'.txt'))
        else:
            print(image_test_path)
            print(file_name,'not find in annotation')

    for file_name in filename_list_image_train:
        if file_name in filename_list_annotation:
            file_anna_path=os.path.join(all_annotation_path,file_name+'.txt')
            shutil.copyfile(file_anna_path,os.path.join(dir_father+'labels/train/',file_name+'.txt'))
        else:
            print(image_train_path)
            print(file_name,'not find in annotation')


dir_father='/scratch/uceezzz/Landfill_dataset/picture18/'
place_label_2_threefolder(dir_father)


print('All finished')