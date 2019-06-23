# -*- coding:utf-8 -*-
import pandas_study


food_info = pandas_study.read_csv('food_info.csv')
# print(type(food_info))
# print(food_info.dtypes)
# print(help(pandas.read_csv))
# print(food_info.head())  # 默认返回前五行数据
# print(food_info.tail())  # 默认返回后五行数据
# print(food_info.shape)
# print(food_info.columns)  # 所有列名

# print(food_info.loc[0])  # 取第一行数据
# print(food_info.loc[3:6])  # 从0开始  3-6行数据
# print(food_info.loc[[2, 5, 10]])  # 3 6 11行数据

# print(food_info['NDB_No'])  # 取ndb_no列数据
# print(food_info[['NDB_No', 'Shrt_Desc']])
# print(food_info.columns.to_list())  # 取列名

# print(food_info['Iron_(mg)'] / 1000)  # 对Iron_(mg)列每个值除以1000

# water_energy = food_info['Water_(g)'] * food_info['Energ_Kcal']
# print(food_info.shape)
# food_info['Iron_(g)'] = food_info['Iron_(mg)'] / 1000  # 添加新值
# print(food_info.shape)

# print(food_info['Water_(g)'].max())  # 最大值
# print(food_info['Water_(g)'].min())  # 最大值

# print(food_info['Sodium_(mg)'][1])
# food_info.sort_values('Sodium_(mg)', inplace=True)  # 默认升序
# food_info.sort_values('Sodium_(mg)', inplace=True, ascending=False)
# print(food_info['Sodium_(mg)'][1])

import pandas_study as pd
import numpy as np
titanic_survival = pd.read_csv('titanic_train.csv')
# print(titanic_survival.head())
age = titanic_survival['Age']
# print(age.loc[0:10])
# print(pd.isnull(age))  # 是否是缺失值
# print(age[pd.isnull(age)])  # 输出缺失值,其他的值将被筛掉
# print(len(age[pd.isnull(age)]))

# mean_age = sum(titanic_survival['Age']) / len(titanic_survival['Age'])
# print(mean_age)  # 因为列中含有缺失值, 所以无法计算 输出nan
# 求均值方法一
# print(titanic_survival['Age'].mean())
# 求均值方法二
# good_ages = titanic_survival['Age'][pd.isnull(titanic_survival['Age'])==False]
# mean_age = sum(good_ages) / len(good_ages)
# print(mean_age)


# 需求:求每个仓位等级(Pclass)的平均价格
# passenger_survival = titanic_survival.pivot_table(index='Pclass', values="Fare", aggfunc=np.mean)
# print(passenger_survival)

# 求每个仓位的平均年龄
# passenger_age = titanic_survival.pivot_table(index='Pclass', values="Age")
# print(passenger_age)

# 求登船地点与船票,获救与否的关系
# port_stats = titanic_survival.pivot_table(index='Embarked', values=['Fare', 'Survived'], aggfunc=np.sum)
# print(port_stats)

# 将年龄中的缺失值丢掉
drop_na_colums = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=['Age', 'Sex'])
