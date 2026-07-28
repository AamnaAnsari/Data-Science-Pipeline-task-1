import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    # 1. Load Data
    file_path = '../data/processed/cleaned_dataset.csv'
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("❌ Error: File not found.")
        return

    # 2. Data Cleaning
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['LoyaltyScore'] = df['LoyaltyScore'].fillna(df['LoyaltyScore'].mean())
    df['TotalPurchases'] = df['TotalPurchases'].fillna(df['TotalPurchases'].median())
    df['SignupDate'] = df['SignupDate'].fillna(df['SignupDate'].mode()[0])

    # 3. Categorical Encoding 
    df_encoded = pd.get_dummies(df, columns=['City'], drop_first=True, dtype=int)

    # 4. Feature Scaling (Standardization)
    scaler = StandardScaler()
    num_cols = ['Age', 'TotalPurchases', 'LoyaltyScore']
    df_encoded[num_cols] = scaler.fit_transform(df_encoded[num_cols])

    # 5. Drop Unnecessary Columns 
    cols_to_drop = ['CustomerID', 'Name', 'SignupDate']
    df_final = df_encoded.drop(columns=cols_to_drop, errors='ignore')

    print("\n--- Final ML-Ready Data ---")
    print(df_final.head())

    # 6. Save Pipeline Output
    output_path = '../data/processed/ml_ready_dataset.csv'
    df_final.to_csv(output_path, index=False)
    print(f"\n✅ Feature Engineering Complete! Saved to: {output_path}")

if __name__ == "__main__":
    main()