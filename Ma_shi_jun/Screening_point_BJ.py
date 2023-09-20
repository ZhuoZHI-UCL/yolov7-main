#这个文件是我们去掉 /scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/All_cor.txt
#中置信度小于0.65的行
#筛选过的放在output.txt中

import json
print('All started')
def replace_single_quotes(line):
    return line.replace("'", '"')
# 打开原始文件和输出文件
with open('/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/All_cor.txt', 'r',encoding="utf-8") as f_in, open('/scratch/uceezzz/Dataset/Landfill_dataset/Beijing/bj_city/big/L16/bj_test/output.txt', 'w',encoding="utf-8") as fout:
    # 逐行读取文件内容
    for line in f_in:
        # 替换单引号为双引号
        line = replace_single_quotes(line)
        # 将每一行内容转换为Python字典
        data = json.loads(line.strip())

        # 检查'confidence'键是否小于0.65
        if data["confidence"] >= 0.65:
        # 如果大于等于0.65，则将该行内容写入新的txt文件中
            fout.write(json.dumps(data) + "\n")

print('All finished')