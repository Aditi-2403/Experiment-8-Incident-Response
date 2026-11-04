
# Experiment 8: Security Incident Response Simulation

# Simulated hardcoded credential for Gitleaks detection
API_KEY = "INCIDENT_DEMO_SECRET_7F3A9C2D8E6B4A1"

DB_PASSWORD = "DummyPassword123!"

def welcome():
    return "Welcome to the application"

def check_credentials():
    if API_KEY and DB_PASSWORD:
        return "Credentials are configured"
    return "Credentials are missing"

if __name__ == "__main__":
    print(welcome())
    print(check_credentials())
