# Mirame Credit Scoring Project

## Overview
This project is designed to build a basic credit scoring system for SACCO loan applications. It processes customer data, builds a scoring model, and implements an offline-first approach.

---

### Step 1: Data Processing

#### Description
We load the raw dataset, handle missing values, and save the cleaned data for further processing.

#### Scripts
- **`src/data_processing.py`**: Contains functions for loading, cleaning, and saving data.
- **`main.py`**: A script to run the data processing pipeline.

#### Usage
1. Place the raw dataset in `data/raw/` as `Mirame_AI_Engineer_Dataset.xlsx`.
2. Run the script:
   ```bash
   python main.py
