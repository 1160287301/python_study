# -*- coding:utf-8 -*-


class Company:
    def __init__(self, e_list):
        self.employee = e_list

    def __str__(self):
        return ','.join(self.employee)

    def __repr__(self):
        return ','.join(self.employee)



company = Company(['1', '2', '3'])
print(company)  # 没有str函数 <__main__.Company object at 0x0000029B595829E8>
print(company)  # 有str函数 1,2,3
company  # 调用__repr__   pycharm不输出

