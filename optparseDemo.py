# -*- coding:utf-8 -*-
'''
  optparse，是一个更够让程序设计人员轻松设计出简单明了、易于使用、符合标准的Unix命令例程式的Python模块。生成使用和帮助信息
  首先你必须导入该类，并创建一个OptionParser对象，然后再使用parser.add_option(...)待定义命令行参数，及其帮助文档。
'''

from optparse import OptionParser

optParser = OptionParser()
optParser.add_option('-f', '--file', action='store', type="string", dest='filename')
optParser.add_option("-v", "--vison", action="store_false", dest="verbose",
                     default='hello', help="make lots of noise [default]")
# optParser.parse_args() 剖析并返回一个字典和列表，
# 字典中的关键字是我们所有的add_option()函数中的dest参数值，
# 而对应的value值，是add_option()函数中的default的参数或者是
# 由用户传入optParser.parse_args()的参数
fakeArgs = ['-f', 'file.txt', '-v', 'how are you', 'arg1', 'arg2']
option, args = optParser.parse_args()
op, ar = optParser.parse_args(fakeArgs)
print("option : ", option)
print("args : ", args)
print("op : ", op)
print("ar : ", ar)
# 输出
# option :  {'filename': None, 'verbose': 'hello'}
# args :  []
# op :  {'filename': 'file.txt', 'verbose': False}
# ar :  ['how are you', 'arg1', 'arg2']

# add_option()参数说明：
#     action:存储方式，分为三种store、store_false、store_true
#     type:类型
#     dest:存储的变量
#     default:默认值
#     help:帮助信息
#
# action的取值有那么多，我么着重说三个store、store_false、store_true 三个取值。 action默认取值store。
#
#        --store 上表示命令行参数的值保存在options对象中。例如上面一段代码，如果我们对optParser.parse_args()函数传入的参数列表中带有‘-f’，那么就会将列表中‘-f’的下一个元素作为其dest的实参filename的值，他们两个参数形成一个字典中的一个元素{filename：file_txt}。相反当我们的参数列表中没有‘-f’这个元素时，那么filename的值就会为空。
#
#       --store_false fakeArgs 中存在'-v'verbose将会返回False，而不是‘how are you’，也就是说verbose的值与'-v'的后一位无关，只与‘-v’存在不存在有关。
#
#       --store_ture  这与action="store_false"类似，只有其中有参数'-v'存在，则verbose的值为True,如果'-v'不存在，那么verbose的值为None。