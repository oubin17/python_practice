import os
import re


class LogFile:
    def __init__(self, name, size, path):
        self.name = name
        self.size = size
        self.path = path


def clean_large_logs(directories, max_size_gb=1):
    print("开始执行日志清理任务...")
    MAX_SIZE_BYTES = max_size_gb * 1024 ** 3  # 转换为字节

    regex = re.compile(r'.*\d{4}-\d{2}-\d{2}(\.\d{1,2})?\.(log|txt)$', re.IGNORECASE)

    cleaned_files = []
    for directory in directories:
        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                if not (filename.endswith(".log") or filename.endswith(".txt")):
                    continue

                print(f"扫描文件: {filepath}")
                try:
                    filesize = os.path.getsize(filepath)
                    if filesize > MAX_SIZE_BYTES:
                        # 清空大日志文件
                        with open(filepath, 'w') as f:
                            f.truncate()
                        cleaned_files.append(LogFile(filename, filesize, filepath))
                    elif regex.match(filename):
                        # 删除匹配正则表达式的日志文件
                        os.remove(filepath)
                        cleaned_files.append(LogFile(filename, filesize, filepath))
                except Exception as e:
                    print(f"处理 {filename} 出错: {e}")

    # 输出清理结果
    if cleaned_files:
        print("\n已清理的日志文件列表：")
        print("=" * 50)
        for file in cleaned_files:
            size_gb = file.size / MAX_SIZE_BYTES
            print(f"• {file.name} ({size_gb:.2f}GB) @ {file.path}")
        print("=" * 50)
    else:
        print("\n未发现需要清理的大日志文件")

    print("日志清理任务完成")


if __name__ == "__main__":
    TARGET_DIRS = [
        "/home/xyzq/afaadvisor",
        "/home/xyzq/afamarketing",
        "/home/xyzq/afascenetaskflow",
        "/home/xyzq/afacustomer",
        "/home/xyzq/afascene"
    ]
    clean_large_logs(TARGET_DIRS)
