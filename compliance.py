
# Experiment 9: Compliance as Code

import ast
import os

def check_compliance():
    violations = []

    # Rule 1: Debug mode must be disabled
    if os.getenv("DEBUG", "False").lower() == "true":
        violations.append("Debug mode is enabled")

    # Rule 2: AWS credentials must not be hardcoded
    source_file = "app.py"

    with open(source_file, "r") as file:
        source_code = file.read()

    if "AKIA" in source_code:
        violations.append("Hardcoded AWS access key detected")

    # Rule 3: Application logging must be enabled
    if "logging" not in source_code:
        violations.append("Application logging is not enabled")

    if violations:
        print("COMPLIANCE CHECK FAILED")
        for violation in violations:
            print("-", violation)
        return False

    print("ALL COMPLIANCE CHECKS PASSED")
    return True


if __name__ == "__main__":
    if not check_compliance():
        exit(1)
