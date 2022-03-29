from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ExampleApp").getOrCreate()
print("Hello World!")