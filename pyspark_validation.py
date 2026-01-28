from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataValidation").getOrCreate()

source_df = spark.read.csv("../datasets/source_data.csv", header=True)
target_df = spark.read.csv("../datasets/target_data.csv", header=True)

if source_df.count() == target_df.count():
    print("Row count validation passed")
else:
    print("Row count validation failed")
