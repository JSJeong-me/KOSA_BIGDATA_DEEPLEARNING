from pyspark import SparkContext, SparkConf
sc = SparkContext.getOrCreate()

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
res = distData.reduce(lambda a, b: a + b)
print(res)