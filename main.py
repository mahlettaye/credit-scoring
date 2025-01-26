from src.data_processing import load_data, clean_data, save_cleaned_data

# Define file paths
RAW_DATA_PATH = "data/raw/Mirame_AI_Engineer_Dataset.xlsx"
CLEANED_DATA_PATH = "data/processed/cleaned_data.csv"

def main():
    print("Loading data...")
    data = load_data(RAW_DATA_PATH)

    print("Cleaning data...")
    cleaned_data = clean_data(data)

    print("Saving cleaned data...")
    save_cleaned_data(cleaned_data, CLEANED_DATA_PATH)

    print("Data processing complete!")

if __name__ == "__main__":
    main()
