# -*- coding:utf-8 -*-

dict1 = {
    'key1': {'1': 1},
    'key2': {'2': 2},
}


# clear
# print(dict1.clear())

# copy 浅拷贝  嵌套的数据不会拷贝
#
# dict2 = dict1.copy()
# dict2['key1']['1'] = 11
# print(dict1)

# 深拷贝
import copy
dict3 = copy.deepcopy(dict1)
dict3['key1']['1'] = 11
print(dict1)

# formkeys
new_dict = dict.fromkeys(['key3', 'key4'], {"company": 'company11111'})
print(new_dict)
print('-'*50)
# setdefault
print(new_dict.setdefault('key4', 'setdefault'))
print(new_dict)
print(new_dict.setdefault('key5', 'setdefault'))
print(new_dict)