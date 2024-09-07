# Import the necessary modules
from sklearn.ensemble import IsolationForest  # Import the Isolation Forest algorithm
import joblib  # Import the joblib module for model serialization
import pandas as pd  # Import pandas for data manipulation

# Load your training data from a CSV file 
train_data = pd.read_csv('models/anomaly_detection_data.csv')

# Assume the training data is stored in a pandas DataFrame
X_train = train_data.drop(['target_column'], axis=1)  # Drop the target column
y_train = train_data['target_column']  # Extract the target column

# Create an instance of the Isolation Forest algorithm
model = IsolationForest()  

# Fit the model to the training data
model.fit(X_train)

# Save the trained model to a file
joblib.dump(model, 'models/anomaly_model.joblib')

print("Model saved to models/anomaly_model.joblib")