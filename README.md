# 🏗️ Medallion Architecture Pipeline (Coding Assignment)

## 🎯 Goal
Implement and run a **Medallion Architecture** data pipeline using PySpark and Delta Lake. This is a hands-on assignment designed to test your ability to build a modular data processing pipeline that ingests raw JSON data, cleans and transforms it, and produces aggregated insights.

---

## 🧱 Medallion Architecture Overview

- **🔸 Bronze Layer**  
  Ingests raw JSON files from a data lake or local directory and stores them as Delta tables without schema enforcement.

- **🔹 Silver Layer**  
  Cleans and transforms the data: filters invalid records, parses timestamps, and selects relevant fields. Stores the output as Delta tables.

- **🟡 Gold Layer**  
  Aggregates daily metrics per patient — such as average heart rate and max blood pressure — and outputs analytics-ready tables.


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-ORG/medallion-pipeline-assignment.git
cd medallion-pipeline-assignment

```
### 2. Create the enviroment
```bash
conda create --name medallion-env python=3.10
conda activate medallion-env
pip install -r requirements.txt
```

### 3. Run the pipeline
```bash
python scripts/pipeline.py --date 2024-01-01
```

