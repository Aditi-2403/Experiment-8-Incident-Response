
# Experiment 9: Compliance as Code
# Secure Application Configuration

import os
import logging

# Compliance Rule 1: No hardcoded credentials
API_KEY = os.getenv("API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Compliance Rule 2: Debug mode disabled
DEBUG = False

# Compliance Rule 3: Application logging enabled
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def welcome():
    logger.info("Application started successfully")
    return "Welcome to the application"


def check_credentials():
    if API_KEY and DB_PASSWORD:
        logger.info("Credentials are configured securely")
        return "Credentials are configured securely"

    logger.warning("Credentials are missing")
    return "Credentials are missing"


if __name__ == "__main__":
    print(welcome())
    print(check_credentials())
