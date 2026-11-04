
# Experiment 8: Security Incident Response Simulation
# Eradication: Remove hardcoded credentials

import os

# Load credentials securely from environment variables
API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def welcome():
    return "Welcome to the application"

def check_credentials():
    if API_KEY and DB_PASSWORD:
        return "Credentials are configured securely"
    return "Credentials are missing"

if __name__ == "__main__":
    print(welcome())
    print(check_credentials())
