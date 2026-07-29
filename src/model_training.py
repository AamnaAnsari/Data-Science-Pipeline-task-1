import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

class ModelTrainer:
    def __init__(self, x_path='data/processed/X.csv', 
                 y_path='data/processed/y.csv', 
                 model_path='models/model.pkl'):
        
        # Paths setup
        self.x_path = x_path
        self.y_path = y_path
        self.model_path = model_path
        
        # Variables initialization
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
        # Initialize Model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def load_and_split_data(self):
        """Processed data load karna aur Train/Test mein split karna."""
        self.X = pd.read_csv(self.x_path)
        self.y = pd.read_csv(self.y_path)
        
        # 80% for training, 20% for testing
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42
        )
        print("✅ Data Loaded and Splitted (80% Train, 20% Test).")

    def train_model(self):
        """Model ko train karna."""
        print("⏳ Model training in progress...")
        self.model.fit(self.X_train, self.y_train.values.ravel())
        print("✅ Model Trained Successfully.")

    def evaluate_model(self):
        """Model ka R2 Score (Accuracy) check karna."""
        predictions = self.model.predict(self.X_test)
        score = r2_score(self.y_test, predictions)
        print(f"🎯 Model Evaluation - R2 Score: {score:.4f}")

    def save_model(self):
        """Trained model ko mehfooz karna."""
        joblib.dump(self.model, self.model_path)
        print(f"✅ Model saved at {self.model_path}")

if __name__ == "__main__":
    print("🚀 Model Training Process Started...")
    
    # Make class object
    trainer = ModelTrainer()
    
    # Call methods
    trainer.load_and_split_data()
    trainer.train_model()
    trainer.evaluate_model()
    trainer.save_model()
    
    print("🎉 Model Training and Saving Completed!")