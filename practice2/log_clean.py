import os


class FileClean:
    def __init__(self, file_name, file_size, file_path):
        self.fileName = file_name
        self.fileSize = file_size
        self.filePath = file_path


def clean_large_log(directories):
    print("开始执行删除日志脚本...")
    LOG_FILE_SIZE = 1024 * 1024 * 1024

    fileList = []
    for item in directories:
        for root, dirs, files in os.walk(item):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                print(f"正在扫描文件:{file_path}...")
                if file_path.endswith(".log"):
                    file_size = os.path.getsize(file_path)
                    if file_size > LOG_FILE_SIZE:
                        try:
                            # 清空文件内容
                            with open(file_path, 'w') as file:
                                file.truncate(0)
                            fileList.append(FileClean(file_name, file_size, file_path))

                        except Exception as e:
                            print(f"处理 {file_name} 时出错: {str(e)}")
    print("已清空的文件列表：===================================================")
    for item in fileList:
        print(f"已清空: {item.fileName} (大小: {item.fileSize / LOG_FILE_SIZE:.2f}GB), 文件全路径：{item.filePath}")
    print("结束删除日志脚本：===================================================")


if __name__ == "__main__":
    directory = ["/home/xyzq/afaadvisor", "/home/xyzq/afamarketing", "/home/xyzq/afascenetaskflow",
                 "/home/xyzq/afacustomer", "/home/xyzq/afascene"]
    clean_large_log(directory)
