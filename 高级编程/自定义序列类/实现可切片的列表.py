# -*- coding:utf-8 -*-

# 模式[start:end:step]
import numbers
class Group:
    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        pass

    def __getitem__(self, item):
        cls = type(self)  # 不要写成Group 避免硬编码
        if isinstance(item, slice):
            return cls(self.group_name, self.company_name, self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(self.group_name, self.company_name, [self.staffs[item]])

    def __len__(self):
        pass

    def __iter__(self):
        pass

    def __contains__(self, item):
        print("contains:",end='1')
        return item in self.staffs


group = Group("imooc", "user", ["bobby1", "bobby2", "bobby3"])
print(group[:2].staffs)
print("bobby1" in group)