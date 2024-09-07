import pandas as pd
from scapy.all import IP
import json
import logging_alerting
import joblib  

def load_anomaly_thresholds(file_path):
    """Load anomaly thresholds from a JSON file"""
    with open(file_path, 'r') as file:
        thresholds = json.load(file)
    return thresholds

def extract_features(packets):
    """Extract features from packets for anomaly detection"""
    features = []
    
    for packet in packets:
        if packet.haslayer(IP):
            ip_layer = packet[IP]
            features.append({
                'length': len(packet),
                'src_ip': ip_layer.src,
                'dst_ip': ip_layer.dst,
                'protocol': ip_layer.proto
            })
        else:
            features.append({
                'length': len(packet),
                'src_ip': None,
                'dst_ip': None,
                'protocol': None
            })
    
    return pd.DataFrame(features)

def perform_anomaly_detection(packets, thresholds):
    """Perform anomaly-based detection"""
    df = extract_features(packets)
    
    # Convert categorical features to numerical (if necessary)
    if df['protocol'].dtype == 'object':
        df['protocol'] = pd.factorize(df['protocol'])[0]  # Convert categorical to numeric
    
    # Ensure that the DataFrame only contains numerical data
    if df.empty or df.select_dtypes(include=['float64', 'int64']).empty:
        raise ValueError("No numerical features available for anomaly detection")
    
    # Load your pre-trained model
    model = load_model('path_to_model')  # Update with your actual model path
    if model:
        predictions = model.predict(df)
        anomalies = df[predictions == -1]
        
        if not anomalies.empty:
            logging_alerting.log_intrusion("Anomaly detected")
            logging_alerting.alert_intrusion("Anomaly detected")
            return True
        
    return False

def load_model(model_path):
    """Load a pre-trained model from file"""
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
