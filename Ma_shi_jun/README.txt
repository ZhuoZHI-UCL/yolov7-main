#任务是对整个北京市的地图进行检测找到所有的垃圾填埋场然后再用点源数据进行对比
#确定最终的垃圾填埋场

步骤：
1.在Split_BJ_citymap.py中我们把整个北京的地图分割成了640*640的小图
2.对每个小图进行目标检测并把检测出来的坐标还原到大图中去，详情见detect.py中使用两条长
#号括起来的部分
3.所有的填埋场在大图中的坐标都被存在 /scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/All_cor.txt
4.去掉该文件中置信度小于0.65的行，用的是screening_point_BJ
5.把置信度大于0.65的检测框给还原到大图里面，见Box_in_bigmap.py