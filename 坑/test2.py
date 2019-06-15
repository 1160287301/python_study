# -*- coding:utf-8 -*-

import operator


#-----------------------------------------------------------------------------------
# print(operator.sub(1, 2))
#-----------------------------------------------------------------------------------
# from collections import  namedtuple
# Employee = namedtuple('Employee', 'name, age, salary')
# rows = [('lily', 20, 2000), ('lucy', 19, 2500)]
# for row in rows:
#     employee = Employee._make(row)
#     print('{}`age is {}, salary is {} '.format(employee.name, employee.age, employee.salary))
#-----------------------------------------------------------------------------------
def get_size(some_object):
    if isinstance(some_object, (list, dict, str, tuple)):
        return len(some_object)
    elif isinstance(some_object, (bool, type(None))):
        return 1
    elif isinstance(some_object, (int, float)):
        return int(some_object)
