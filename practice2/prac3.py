# 列表去重
# def list_remove_elements(lista):
#     lists = []
#     for item in lista:
#         if item not in lists:
#             lists.append(item)
#     return lists
#
#
# print(list_remove_elements([1, 2, 2, 3, 4, 4, 5]))
import random


# 统计文本文件中各单词的出现次数

# def count_words(file_path):
#     word_count = {}
#     with open(file_path, 'r') as file:
#         for line in file:
#             words = line.split(" ")
#             for word in words:
#                 if word not in word_count:
#                     word_count[word] = 0
#                 word_count[word] += 1
#     return word_count
#
#
# print(count_words("/Users/oubin/Downloads/未命名.txt"))


# 前 20项斐波那契数列
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#     print("")
#
# fibonacci(20)


# 字典合并 相同建的值相加
# def merge_dicts(*dict_args):
#     result = dict_args[0].copy()
#     for key, value in dict_args[1].items():
#         result[key] = result.get(key, 0) + value
#         # if key in result:
#         #     result[key] += value
#         # else:
#         #     result[key] = value
#     print(result)
#
#
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4, 'a': 3}
# merge_dicts(dict1, dict2)

# 列表排序
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#     print(lst)
#
#
# bubble_sort([1, 5, 2, 4, 3])

# 猜数游戏

# def guess_number():
#     number = random.randint(1, 100)
#     for i in range(3):
#         guess = int(input(f"正在尝试第{i + 1}次，请输入数字："))
#         if guess == number:
#             return "恭喜你，猜对了"
#         elif guess > number:
#             print("猜的数字太大了")
#         else:
#             print("猜的数字太小了")
#     return f"游戏结束，正确数字是{number}"
#
#
# print(guess_number())
