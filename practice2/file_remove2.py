import os
import re


def clean_large_txt_files(directory):
    ONE_GB = 1024 * 100
    regex = re.compile(r'.*\d{4}-\d{2}-\d{2}(\.\d{1,2})?\.(log|txt)$', re.IGNORECASE)

    for fileName in os.listdir(directory):
        filePath = os.path.join(directory, fileName)
        # 确保是文件，并且包含.log关键字
        if os.path.isfile(filePath) and ".log" in fileName:
            fileSize = os.path.getsize(filePath)
            if fileSize > ONE_GB:
                try:
                    with open(filePath, 'w') as file:
                        file.truncate(0)
                        print(filePath, "处理完成")
                except Exception as e:
                    print(f"处理 {fileName} 时出错: {str(e)}")
            elif regex.match(fileName):
                print(f"正则匹配{fileName}")


if __name__ == "__main__":
    directory = "/Users/oubin/Downloads/test"
    clean_large_txt_files(directory)
