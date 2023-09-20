  参考视频https://www.bilibili.com/video/BV19B4y1z72V/?spm_id_from=333.788.recommend_more_video.-1&vd_source=08c7a8f788b1356f6c6d705cfc31b898
参考笔记 https://liveuclac-my.sharepoint.com/personal/uceezzz_ucl_ac_uk/_layouts/OneNote.aspx?id=%2Fpersonal%2Fuceezzz_ucl_ac_uk%2FDocuments%2F%E5%85%B6%E4%BB%96%E9%A1%B9%E7%9B%AE&wd=target%28Landfill%20project.one%7C59BE49F3-DBC3-478D-83A9-B73112BA6D21%2F%E4%BD%BF%E7%94%A8yolov7%E8%BF%9B%E8%A1%8C%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%7C4A713FC0-CA8D-402B-BE23-7E75CED906B3%2F%29
onenote:https://liveuclac-my.sharepoint.com/personal/uceezzz_ucl_ac_uk/Documents/其他项目/Landfill%20project.one#使用yolov7进行目标检测&section-id={59BE49F3-DBC3-478D-83A9-B73112BA6D21}&page-id={4A713FC0-CA8D-402B-BE23-7E75CED906B3}&end
几个注意的点：实验结果保存在run里面
运行的话回头看视频

数据集被借走了 在/home/uceezzz/Landfillproject/Swin-Transformer/data/coco里面
数据集给取回后只需要分成images和labels两个文件夹就行 里面分别有三个文件夹 train val test

detect_old是之前给msj进行检测，先把一个大图拆成小图检测再拼接回去

.