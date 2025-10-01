import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("VSCodeTest").getOrCreate()

df = spark.createDataFrame([(1, "Apple"), (2, "Orange")], ["ID", "Fruit"])
df.show()