# 计算长方形的面积
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# rectangle = Rectangle(5, 10)
# print(f"长方形的面积是：{rectangle.area()}")


# 输出学生的名字和学校的名字
# class Student:
#     school_name = "某某一中"
#
#     def __init__(self, name):
#         self.name = name
#
#     # def __init__(self):
#     #     self.age = 18
#
#     def print_name(self):
#         print(f"学校名字是：{Student.school_name}, 学生的名字是：{self.name}")
#
#     # def print_age(self):
#     #     print(f"学校名字是：{Student.school_name}, 学生的年龄是：{self.age}")
#
#
# stu = Student("张三")
# stu.print_name()

# 继承
class Animal:

    def speak(self):
        print("动物叫")


# class Dog(Animal):
#     def speak(self):
#         print("汪汪汪")
#
#
# dog = Dog()
# dog.speak()
