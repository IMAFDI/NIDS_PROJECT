import logging

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO)

def log_intrusion(message):
    logging.info(message)

def alert_intrusion(message):
    print(f"Alert: {message}")
    