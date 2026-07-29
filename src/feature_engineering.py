import pandas as pd
import joblib
import os
from sklearn.preprocessing import StandardScaler

class DataProcessor:
    def __init__(self, input_path='data/raw/customer_data.csv', 
                 output_x_path='data/processed/X.csv', 
                 output_y_path='data/processed/y.csv', 
                 scaler_path='models/scaler.pkl'):
        
        # Variables setup
        self.input_path = input_path
        self.output_x_path = output_x_path
        self.output_y_path = output_y_path
        self.scaler_path = scaler_path
        
        # Folders 
        os.makedirs(os.path.dirname(self.output_x_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.scaler_path), exist_ok=True)
        
        self.scaler = StandardScaler()
        self.df = None
        self.X = None
        self.y = None

    def load_data(self):
        """Raw data ko load karna."""
        self.df = pd.read_csv(self.input_path)
        print("✅ Data Loaded Successfully.")

    def preprocess_data(self):
        """Data clean, encode aur scale karna."""
        # 1. One-Hot Encoding (City)
        self.df = pd.get_dummies(self.df, columns=['City'], drop_first=True)
        
        # 2. Features (X) aur Target (y) alag karna
        self.X = self.df.drop('LoyaltyScore', axis=1)
        self.y = self.df['LoyaltyScore']
        
        # 3. Scaling (Age aur TotalPurchases)
        features_to_scale = ['Age', 'TotalPurchases']
        self.X[features_to_scale] = self.scaler.fit_transform(self.X[features_to_scale])
        
        # saving scaler
        joblib.dump(self.scaler, self.scaler_path)
        print(f"✅ Scaler saved at {self.scaler_path}")

    def save_processed_data(self):
        """Processed data ko save karna."""
        self.X.to_csv(self.output_x_path, index=False)
        self.y.to_csv(self.output_y_path, index=False)
        print("✅ Processed X and y saved successfully.")

if __name__ == "__main__":
    print("🚀 Feature Engineering Process Started...")
    
    # Make class object
    processor = DataProcessor()
    
    # Call methods
    processor.load_data()
    processor.preprocess_data()
    processor.save_processed_data()
    
    print("🎉 Feature Engineering Completed!")