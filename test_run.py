from src.data_loader import DataLoader

# 1. Raw folder se initial dataset load karein
loader = DataLoader("data/raw/dataset.csv")

df = loader.load_csv()

if df is not None:
    loader.get_data_summary()
    
    # 2. Processed data ko processed folder mein save karein
    loader.save_data("data/processed/cleaned_dataset.csv")