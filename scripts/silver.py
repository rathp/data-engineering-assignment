from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

def run_silver_layer(input_path, output_path):
    spark = SparkSession.builder.appName("SilverLayer").getOrCreate()

    # TODO: Read Delta data from input_path
    # df = spark.read.format("delta").load(input_path)

    # TODO: Filter rows with null patient_id
    # TODO: Convert timestamp to Spark TimestampType
    # TODO: Select relevant columns: patient_id, timestamp, heart_rate, blood_pressure
    # cleaned_df = ...

    # TODO: Write cleaned data to output_path
    # cleaned_df.write.format("delta").mode("overwrite").save(output_path)

    print("Silver layer complete.")
