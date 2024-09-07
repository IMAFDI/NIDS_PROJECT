
# Network Intrusion Detection System (NIDS) 🔒

![NIDS Overview](https://yourimageurl.com/nids_overview.png)  
*(Add a network security image to visually represent the project)*

## Introduction
This project implements a **Network Intrusion Detection System (NIDS)** using **Scapy** to monitor network traffic and detect potential intrusions. The system performs both **signature-based detection** and **anomaly-based detection** to identify suspicious activities in real-time, providing alerts and logs for further analysis.

### Key Features:
- **Packet Capture**: Real-time monitoring of network traffic.
- **Signature-based Detection**: Identification of known attack signatures.
- **Anomaly-based Detection**: Machine learning-based detection of abnormal network behavior.
- **Alerting & Logging**: Comprehensive logging and alerting on potential intrusions.

![Intrusion Detection Flow](https://yourimageurl.com/intrusion_flow.png)  
*(Add a flow diagram to show the steps of packet capture, detection, and alerting)*

---

## Requirements

Before running the project, you need to install the following:

- **Scapy**: A Python library for packet manipulation and analysis.
- **Joblib**: For saving and loading pre-trained machine learning models.
- **Scikit-learn**: For the machine learning-based anomaly detection.

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Project Structure

```
nids_project/
│
├── config/
│   ├── anomaly_thresholds.json   # Anomaly detection thresholds
│   └── rules.json                # Signature detection rules
│
├── models/                       # Trained machine learning models
│   └── anomaly_model.joblib      # Pre-trained anomaly detection model
│
├── scripts/
│   ├── packet_capture.py         # Handles packet capture
│   ├── signature_detection.py    # Detects known attack signatures
│   ├── anomaly_detection.py      # Detects anomalies using ML
│   └── logging_alerting.py       # Logs and alerts on intrusions
│
└── main.py                       # Main execution script
```

---

## Configuration

### 1. **rules.json**: Defines the signature-based detection rules.
```json
{
    "rule_1": {
        "name": "TCP SYN Flood",
        "pattern": "SYN",
        "threshold": 100
    }
}
```

### 2. **anomaly_thresholds.json**: Defines threshold values for anomaly detection.
```json
{
    "threshold_1": {
        "name": "Packet Size",
        "value": 1500
    }
}
```

---

## Running the Project

To start the NIDS system, execute the following command:
```bash
python -u main.py
```

This will:
- Capture network packets from the specified interface.
- Perform both signature-based and anomaly-based detection.
- Log and alert you if any suspicious activity is found.

---

## Explanation of the Code

The NIDS system operates in two phases: **Packet Capture** and **Intrusion Detection**.

1. **Packet Capture**: The system uses the `packet_capture.py` script to capture packets from the network using **Scapy**. You can specify the network interface and packet count.
   ```python
   packets = capture_packets(interface='Realtek RTL8822CE 802.11ac PCIe Adapter', count=100)
   ```

2. **Signature Detection**: This is handled by the `signature_detection.py` module, which checks packets against pre-defined attack signatures from the `rules.json` file.
   ```python
   signature_detected = perform_signature_detection(packets, rules)
   ```

3. **Anomaly Detection**: Using the **Isolation Forest** algorithm, the `anomaly_detection.py` module identifies any abnormal patterns in network traffic.
   ```python
   anomaly_detected = perform_anomaly_detection(packets, thresholds)
   ```

4. **Alerting & Logging**: If an intrusion is detected, the system logs the incident and sends an alert using the `logging_alerting.py` module.
   ```python
   logging_alerting.log_intrusion("Anomaly detected")
   ```

---

## Example Use Case

### Step 1: Capture Network Traffic
The system captures 100 packets from the **Realtek RTL8822CE 802.11ac PCIe Adapter** interface:
```python
packets = capture_packets('Realtek RTL8822CE 802.11ac PCIe Adapter', count=100)
```

### Step 2: Detect Intrusions
The system performs both signature-based and anomaly-based detection on the captured packets. If an intrusion is detected, an alert is generated.

### Step 3: Log and Alert
If an intrusion is found, the system logs it and sends an alert, which can be further analyzed for security response.

---

## Troubleshooting

- **Wireshark Manuf Issue**: If Wireshark is installed but cannot read the `manuf` file, ensure that the `manuf` file is present in the Scapy installation directory and is not corrupted.
- **Packet Capture Issues**: Verify that the network interface specified in `main.py` matches your system's available interfaces.

---

## Screenshots (Optional)

You can add screenshots of your output or process to make it more user-friendly.

![NIDS Screenshot](https://yourimageurl.com/nids_screenshot.png)  
*(Add screenshots from your terminal showcasing packet capture and detection)*

---

## License
This project in not been licensed unber any License. You can are free to use and give your inputs.

---

## Future Enhancements

- Integration with a **database** for storing intrusion logs.
- Implementing a **real-time dashboard** for monitoring live traffic and alerts.
- Adding more complex machine learning models for anomaly detection.
  
---

Feel free to contribute, suggest new features, or report issues. Happy detecting! 😊

---

### Links to External Resources
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [Network Security Fundamentals](https://en.wikipedia.org/wiki/Network_security)

---

**Note:** Replace image links and file paths with actual resources once available.
