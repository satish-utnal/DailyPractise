# @Author Satish Utnal

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pyspark.sql import SparkSession
from datetime import datetime, date

spark = SparkSession.builder.appName('firsttest').getOrCreate()

# rdd = spark.sparkContext.parallelize([
#     (1, 4., 'GFG1', date(2000, 8, 1), datetime(2000, 8, 1, 12, 0)),
#     (2, 8., 'GFG2', date(2000, 6, 2), datetime(2000, 6, 2, 12, 0)),
#     (3, 5., 'GFG3', date(2000, 5, 3), datetime(2000, 5, 3, 12, 0))
# ])
#
# schema = ['a', 'b', 'c', 'd', 'e']
#
# df = spark.createDataFrame(rdd, schema=schema)
#
# df1 = spark.read.csv('../data/orders.txt', header=True, inferSchema=True)
