# -*- coding:utf-8 -*-
# 类也是对象 type是创建类的类
# 什么事元类 元类是创建类的类 type->class->对象

def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    if name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


def say(self):
    return self.name


class BaseClass:
    def a(self):
        return "in baseclass"


if __name__ == '__main__':
    # myclass = create_class('user')
    # u = myclass()
    # print(u)

    # 使用type动态创建类
    # User = type("User", (BaseClass,), {'name': 'user', 'say': say})
    # u = User()
    # print(u.name)
    # print(u.say())
    # print(u.a())

    # class MetaClass(type):
    #     def __new__(cls, *args, **kwargs):
    #         print("in metaclass new")
    #         return super().__new__(cls, *args, **kwargs)

    # python中实例化过程,寻找metaclass->寻找父类的metaclass->当前模块(文件)寻找父类的metaclass->type
    # class newclass(metaclass=MetaClass):
    #     def __init__(self, name):
    #         self.name = name
    #
    #     def __str__(self):
    #         return "user"
    #
    #
    # n = newclass(name="name")
    # print(n)
    pass

