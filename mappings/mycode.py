from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

#start session
spark = SparkSession.builder.appName("spark practice").getOrCreate()

#read sales dataframe
df = spark.read.csv('/samples/sales.csv', sep =',' , inferSchema = True, header = True)

#show data
df.show(5)

#count total rows
count = df.count()
print("total number of rows", count)

#reading specific columns(select)
df1 = df.select("sale_id" , "sale_date")
df1.show()

#filter (where)
filtered_df = df.filter('total_amount > 50.00')
filtered_df.show()
print(filtered_df.count())
