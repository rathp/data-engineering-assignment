import argparse
from bronze import run_bronze_layer
from silver import run_silver_layer
from gold import run_gold_layer

def main(date):
    print(f"Running pipeline for date: {date}")

    # Define hardcoded paths (you can replace with config/CLI args)
    bronze_in = "data/bronze"
    bronze_out = "data/silver/temp_bronze"
    silver_out = "data/silver/patient_vitals"
    gold_out = "data/gold/patient_daily_summary"

    # TODO: Call Bronze layer function
    run_bronze_layer(bronze_in, bronze_out)

    # TODO: Call Silver layer function
    run_silver_layer(bronze_out, silver_out)

    # TODO: Call Gold layer function
    run_gold_layer(silver_out, gold_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run medallion pipeline")
    parser.add_argument("--date", required=True, help="Date to process (YYYY-MM-DD)")
    args = parser.parse_args()
    main(args.date)
