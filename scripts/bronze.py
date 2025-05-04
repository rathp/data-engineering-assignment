from pyspark.sql import SparkSession

def run_bronze_layer(input_path, output_path):
    spark = SparkSession.builder.appName("BronzeLayer").getOrCreate()

    # TODO: Read raw JSON files from input_path
    # df = spark.read.json(input_path)

    # TODO: Write the DataFrame as Delta to output_path
    # df.write.format("delta").mode("overwrite").save(output_path)

    print("Bronze layer complete.")