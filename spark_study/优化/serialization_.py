# -*- coding:utf-8 -*-


'''
数据序列化有两种方式:
    1.用java序列化  java序列化灵活,慢,序列化格式大
    2.kryo序列化 速度快,格式更紧凑,但不支持所有serializable类型,并需要提前注册所要用到的类

val conf = new SparkConf().setMaster(...).setAppName(...)
conf.registerKryoClasses(Array(classOf[MyClass1], classOf[MyClass2]))
val sc = new SparkContext(conf)


pyspark中没有registerKryoClasses



'''

