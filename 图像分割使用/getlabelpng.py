import os
import shutil

# 指定包含多个子文件夹的目录
parent_dir = 'C:\codes\data_process\json'
# 指定新的存放目录
new_dir = 'C:\codes\data_process\masks'

# 确保新的存放目录存在
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

# 遍历父目录中的所有子文件夹
for subdir, dirs, files in os.walk(parent_dir):
    for file in files:
        if file == 'label.png':
            # 构建原始文件的完整路径
            original_path = os.path.join(subdir, file)
            # 使用子文件夹的名字作为新文件名
            new_filename = os.path.basename(subdir) + '.png'
            # 构建新文件的完整路径
            new_path = os.path.join(new_dir, new_filename)
            # 复制并重命名文件
            shutil.copy2(original_path, new_path)

print("文件提取和重命名完成。")