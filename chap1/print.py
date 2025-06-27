# a+ 文件不存在，则创建，存在，则追加
fp=open('/Users/oubin/Downloads/未命名.txt', "a+")
print("hello world", file=fp)
fp.close()

print("hello\nworld")
print("hello\tworld")
print("hellooo\tworld")
print("hello\rworld")#覆盖
print("hello\bworld")#退格

print(r"hellooo\tworld")#转义字符不起作用，在字符串前加r或R