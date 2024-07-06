import subprocess
import os

# 指定包含 JSON 文件的目录
json_dir = r'C:\codes\data_process\json'
# 指定输出 mask 图像的目录
output_dir = r'C:\codes\data_process\json'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 遍历目录中的所有 JSON 文件
for json_file in os.listdir(json_dir):
    if json_file.endswith('.json'):
        # 构建完整的文件路径
        json_path = os.path.join(json_dir, json_file)
        # 构建输出路径
        output_path = os.path.join(output_dir, json_file.replace('.json', '.png'))
        # 执行 labelme_json_to_dataset 命令
        subprocess.run(['labelme_json_to_dataset', '-o', output_path, json_path])

print("批量转换完成。")