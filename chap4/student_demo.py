#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/9 10:35
# @Author  : oubin
# @File    : student_demo.py
# @Software: PyCharm
class Student:
    native_value1 = "1"
    native_value2 = "2"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def instanceMethod(self):
        print("这是一个实例方法")

    @classmethod
    def classMethod(cls):
        print("这是一个类方法")

    @staticmethod
    def staticMethod():
        print("这是一个静态方法")


print(id(Student))
print(Student.native_value2)

stu = Student("name", "age")
stu.name = "new name"
stu.first = "first"
print(stu.first)


def show():
    print("动态绑定方法")


stu.show = show();
print(stu.show)

print(Student.classMethod())
print(Student.staticMethod())
print(Student.instanceMethod(stu))


class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self, name):
        self.name = name

c = C("name")
print(dict(c.__dict__))
print(dict(A.__dict__))