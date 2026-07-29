import pandas as pd
import numpy as np
import os

class DataGenerator:
    def __init__(self, num_rows=1000, output_path='data/raw/customer_data.csv'):
        # __init__ method variables ko initialize karta hai
        self.num_rows = num_rows
        self.output_path = output_path
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

    def generate_data(self):
        """Synthetic data generate karne ka function."""
        np.random.seed(42)
        
        ages = np.random.randint(18, 65, self.num_rows)
        purchases = np.random.uniform(1000, 50000, self.num_rows)
        cities = np.random.choice(['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta'], self.num_rows)
        
        # Secret formula for Loyalty Score
        loyalty_scores = (purchases / 1000) * 1.2 + (ages * 0.5)
        
        # Adding some natural random noise
        noise = np.random.normal(0, 2, self.num_rows)
        loyalty_scores = loyalty_scores + noise
        loyalty_scores = np.clip(loyalty_scores, 1, 100) # Score 1 se 100 ke darmiyan rahe
        
        # Create DataFrame
        self.df = pd.DataFrame({
            'Age': ages,
            'City': cities,
            'TotalPurchases': purchases,
            'LoyaltyScore': loyalty_scores
        })
        print(f"✅ {self.num_rows} rows ka data successfully generate ho gaya!")

    def save_data(self):
        """Data ko CSV file mein save karne ka function."""
        self.df.to_csv(self.output_path, index=False)
        print(f"✅ Data saved at: {self.output_path}")

# If this script is run, automatically this block will be executed
if __name__ == "__main__":
    print("🚀 Data Generation Process Started...")
    
    # Make class object
    generator = DataGenerator() 
    
    # Call methods
    generator.generate_data()
    generator.save_data()
    
    print("🎉 Data Generation Completed!")