
import re

def check_compliance():
    violations = []

    with open("app.py", "r") as file:
        source_code = file.read()

    # Rule 1: No hardcoded AWS access keys
    if re.search(r"AKIA[0-9A-Z]{16}", source_code):
        violations.append("Hardcoded AWS access key detected")

    # Rule 2: Debug mode must be disabled
    if re.search(r"DEBUG\s*=\s*True", source_code):
        violations.append("Debug mode is enabled")

    # Rule 3: Application logging must be enabled
    if "import logging" not in source_code:
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
