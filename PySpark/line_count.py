from pyspark import SparkConf, SparkContext
 
conf = SparkConf().setMaster("local").setAppName("test")
sc = SparkContext(conf=conf)
 
lines =sc.textFile("./README.txt")
 
print("lines.count() :", lines.count() ) 
print("lines.first() :", lines.first() )
 
pythonLines = lines.filter(lambda line : "EMR" in line)
print("pythonLines.first() :", pythonLines.first())