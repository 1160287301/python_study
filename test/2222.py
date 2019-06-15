# -*- coding:utf-8 -*-
# 1. 种种迹象表明 当你输入一个订单号 你应该取出该订单所对应人的所有信息
# 比如输入订单编号1   输出小红所有的信息  (我这里已经根据create_date正序排列)
'''
[   # 订单号 身份证 create_data finish_date
    [1, '小红', 20190101, ''],
    [2, '小红', 20190103, 20190104],
    [3, '小红', 20190105, 20190108],
    [4, '小红', 20190107, 20190108],
]
'''
xiao_hong = [
    [1, '小红', 20190101, ''],
    [2, '小红', 20190103, 20190104],
    [3, '小红', 20190105, 20190108],
    [4, '小红', 20190107, 20190108],
]
data_ = dict()
for i in range(len(xiao_hong)):  # 循环出小红所有的信息
    current_ = i  # 当前的数据
    last_ = current_ - 1  # 上一条数据
    current_create_time = xiao_hong[current_][2]  # 当前数据的 create_date
    current_finish_date = xiao_hong[current_][3]  # 当前数据的 finish_date
    current_order_id = int(xiao_hong[current_][0])  # 当前数据的 订单号
    last_finish_date = xiao_hong[last_][3] or 0  # 上一条数据的 finish_date
    if last_ == -1:  # 如果现在循环的是第一条数据
        if not current_finish_date: # 没有finish_date的话
            data_[current_order_id] = 0
        else:
            pass  # 不排除会出现这种情况, 但你没说, 先暂时当没看见
    else:  # 如果现在循环的不是第一条数据
        if last_finish_date == 0: # 上一条数据的 finish_date不存在
            data_[current_order_id] = 1
        else:
            if last_finish_date > current_create_time:  # 上一条数据的 finish_date 大于 当前数据的 create_date
                data_[current_order_id] = 1
            else:
                data_[current_order_id] = 0

print(data_)
# data_结果
'''
{
    1 : 0,
    2 : 1,
    3 : 0,
    4 : 1
}
'''
# 如果要把所有订单分数相加
point = 0
for order_id, order_point in data_.items():
    point += order_point

print(point)  # 总分2分

a = '值'
a = 1 if a is not None else a