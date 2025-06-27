import os


def clear_large_txt_files(directory):
    """
    清空目录中所有大于1GB的.txt文件内容
    :param directory: 要扫描的目录路径
    """
    # 定义1GB的字节大小
    ONE_GB = 1024 * 1024 * 1024

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # 确保是文件且后缀为.txt
        if os.path.isfile(filepath) and filename.lower().endswith('.txt'):
            # 检查文件大小
            file_size = os.path.getsize(filepath)
            if file_size > ONE_GB:
                try:
                    # 清空文件内容
                    with open(filepath, 'w') as file:
                        file.truncate(0)
                    print(f"已清空: {filename} (大小: {file_size / ONE_GB:.2f}GB)")
                except Exception as e:
                    print(f"处理 {filename} 时出错: {str(e)}")


if __name__ == "__main__":
    target_dir = input("请输入要扫描的目录路径: ").strip()

    # 验证目录是否存在
    if not os.path.isdir(target_dir):
        print(f"错误: 目录 '{target_dir}' 不存在")
    else:
        print(f"开始扫描目录: {target_dir}")
        clear_large_txt_files(target_dir)
        print("操作完成")