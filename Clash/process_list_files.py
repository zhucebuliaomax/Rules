import os
import re

def process_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 进行替换
    # 删除 "DOMAIN,"
    content = content.replace('DOMAIN,', '')
    # 将 "DOMAIN-SUFFIX," 替换为 "."
    content = content.replace('DOMAIN-SUFFIX,', '.')
    
    # 创建新的.txt文件路径
    txt_path = os.path.splitext(file_path)[0] + '.txt'
    
    # 写入新文件
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 遍历当前目录下的所有.list文件
    for filename in os.listdir(current_dir):
        if filename.endswith('.list'):
            file_path = os.path.join(current_dir, filename)
            print(f'处理文件: {filename}')
            process_file(file_path)
            new_filename = os.path.splitext(filename)[0] + '.txt'
            print(f'已生成新文件: {new_filename}')

if __name__ == '__main__':
    main() 