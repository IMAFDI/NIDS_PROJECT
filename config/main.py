import packet_capture
import signature_detection
import anomaly_detection
import logging_alerting
import cli
import logging


# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def load_configurations():
    """Load configuration files"""
    rules = signature_detection.load_rules('config/rules.json')
    thresholds = anomaly_detection.load_anomaly_thresholds('config/anomaly_thresholds.json')
    return rules, thresholds

def capture_packets(interface, count):
    """Start packet capture"""
    return packet_capture.capture_packets(interface, count)

def perform_signature_detection(packets, rules):
    """Perform signature-based detection"""
    if signature_detection.detect_signatures(packets, rules):
        logging_alerting.log_intrusion("Signature match")
        logging_alerting.alert_intrusion("Signature match")
        return True
    return False

def perform_anomaly_detection(packets, thresholds):
    """Perform anomaly-based detection"""
    if anomaly_detection.perform_anomaly_detection(packets, thresholds):
        logging_alerting.log_intrusion("Anomaly detected")
        logging_alerting.alert_intrusion("Anomaly detected")
        return True
    return False

def main():
    # Load configuration files
    rules, thresholds = load_configurations()

    # Start packet capture
    packets = capture_packets('Realtek RTL8822CE 802.11ac PCIe Adapter', count=100)

    # Perform detections
    signature_detected = perform_signature_detection(packets, rules)
    anomaly_detected = perform_anomaly_detection(packets, thresholds)

    # Log results
    if signature_detected or anomaly_detected:
        logging.info("Intrusion detected")

if __name__ == '__main__':
        main()