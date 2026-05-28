from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

#start session
spark = SparkSession.builder.appName("spark practice").getOrCreate()

#read sales dataframe
df = spark.read.csv('/samples/sales.csv', sep =',' , inferSchema = True, header = True)

#show data
df.show(5)

#printing schema
df.printSchema()
