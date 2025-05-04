from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, count, to_date

def run_gold_layer(input_path, output_path):
    spark = SparkSession.builder.appName("GoldLayer").getOrCreate()

    # TODO: Read Delta data from input_path
    # df = spark.read.format("delta").load(input_path)

    # TODO: Create 'day' column from timestamp
    # TODO: Group by patient_id and day
    # TODO: Compute avg heart rate, max blood pressure, count of readings
    # summary_df = ...

    # TODO: Write summary data to output_path
    # summary_df.write.format("delta").mode("overwrite").save(output_path)

    print("Gold layer complete.")
# Gold layer: aggregate data for analytics

