import pandas as pd
import logging
import os

# Basic logging configuration setup
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class DataLoader:
    """
    A professional class to handle data loading, summarizing, and saving operations.
    """
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load_csv(self) -> pd.DataFrame:
        """Loads a CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.file_path)
            logging.info(f"CSV data successfully loaded from: {self.file_path}")
            return self.data
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            return None
        except Exception as e:
            logging.error(f"Error loading CSV: {e}")
            return None

    def load_excel(self) -> pd.DataFrame:
        """Loads an Excel file (.xlsx) into a pandas DataFrame."""
        try:
           
            self.data = pd.read_excel(self.file_path)
            logging.info(f"Excel data successfully loaded from: {self.file_path}")
            return self.data
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            return None
        except Exception as e:
            logging.error(f"Error loading Excel file: {e}")
            return None

    def get_data_summary(self):
        """Prints a professional overview of the loaded dataset."""
        if self.data is not None:
            logging.info("Generating data summary...")
            print("\n" + "="*40)
            print("📊 DATASET SUMMARY")
            print("="*40)
            print(f"Total Rows: {self.data.shape[0]}")
            print(f"Total Columns: {self.data.shape[1]}\n")
            print("Missing Values per Column:")
            print(self.data.isnull().sum())
            print("="*40 + "\n")
        else:
            logging.warning("No data loaded yet. Please load data first.")

    def save_data(self, output_path: str):
        """Saves the current DataFrame to a new CSV file."""
        if self.data is not None:
            try:
                # Ensure the output directory exists
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                self.data.to_csv(output_path, index=False)
                logging.info(f"Data successfully saved to: {output_path}")
            except Exception as e:
                logging.error(f"Error saving data: {e}")
        else:
            logging.warning("No data to save. Please load data first.")