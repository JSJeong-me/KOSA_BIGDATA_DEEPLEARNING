from pyspark import SparkContext, SparkConf
sc = SparkContext.getOrCreate()

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data, 10) # 10개의 파티션으로 수행!
res = distData.reduce(lambda a, b: a + b)
print(res)