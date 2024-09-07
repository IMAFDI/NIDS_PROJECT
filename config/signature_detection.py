import json
from scapy.all import IP

def load_rules(rule_file):
    """Load rules from a JSON file"""
    with open(rule_file, 'r') as f:
        rules = json.load(f)
    return rules

def detect_signatures(packets, rules):
    """Detect signatures based on loaded rules"""
    for packet in packets:
        # Check if the packet has the IP layer
        if packet.haslayer(IP):
            # Loop through the rules and check for matching signatures
            for rule in rules['rules']:
                # Ensure the rule format is correct and valid
                if 'dst_ip' in rule and (rule['dst_ip'] == 'any' or packet[IP].dst == rule['dst_ip']):
                    print(f"Signature matched: {rule['description']}")
                    return True
    return False
