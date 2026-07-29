import pandas as pd
import joblib

class ModelPredictor:
    def __init__(self, model_path='models/model.pkl', scaler_path='models/scaler.pkl'):
        # Paths setup
        self.model_path = model_path
        self.scaler_path = scaler_path
        
        # Load models
        self.model = joblib.load(self.model_path)
        self.scaler = joblib.load(self.scaler_path)

    def predict_new_customer(self, new_data):
        """Naye customer ka data input lena aur predict karna."""
        # Convert new data to DataFrame
        df_new = pd.DataFrame([new_data])
        
        # One-Hot Encoding (for City)
        # Ensure the same columns as training
        df_new = pd.get_dummies(df_new, columns=['City'])
        
       
        expected_cities = ['City_Karachi', 'City_Lahore', 'City_Peshawar', 'City_Quetta']
        for city in expected_cities:
            if city not in df_new.columns:
                df_new[city] = 0
                
        # Keep the same columns as training
        columns_order = ['Age', 'TotalPurchases'] + expected_cities
        df_new = df_new.reindex(columns=columns_order, fill_value=0)
                
        # Keep the same columns as training
        columns_order = ['Age', 'TotalPurchases'] + expected_cities
        df_new = df_new.reindex(columns=columns_order, fill_value=0)
        
        # Apply Scaling
        features_to_scale = ['Age', 'TotalPurchases']
        df_new[features_to_scale] = self.scaler.transform(df_new[features_to_scale])
        
        # Make Prediction
        prediction = self.model.predict(df_new)
        return prediction[0]

if __name__ == "__main__":
    print("🚀 Prediction Process Started...")
    
    # Make class object
    predictor = ModelPredictor()
    
    # New customer test data
    new_customer = {
        'Age': 28,
        'City': 'Karachi',
        'TotalPurchases': 15000
    }
    
    # Call prediction method
    predicted_score = predictor.predict_new_customer(new_customer)
    
    print(f"👤 Customer Profile: Age={new_customer['Age']}, City={new_customer['City']}, Purchases={new_customer['TotalPurchases']}")
    print(f"⭐ Predicted Loyalty Score: {predicted_score:.2f}/100")