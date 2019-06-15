# -*- coding:utf-8 -*-
'''
当使用spark-submit命令提交该py文件后 print正常输出
但是输出日志里面的监控的ui(http://192.168.99.1:4040)
在执行完成后就无法访问

如要能记录日志:
1.$SPARK_HOME/conf/spark-default.conf文件
    spark.eventLog.enabled           true
    spark.eventLog.dir               hdfs://namenode:8021/directory
    取消注释
2.$SPARK_HOME/conf/spark-env.sh文件
    SPARK_HISTORY_OPTS = "-Dspark.history.fs.logDirectory=hdfs://namenode:8021/directory"


'''
from pyspark import SparkConf, SparkContext

conf = SparkConf()

sc = SparkContext(conf=conf)

data = [1, 2, 3, 4, 5]
distdata = sc.parallelize(data)
print(distdata.collect())

sc.stop()
