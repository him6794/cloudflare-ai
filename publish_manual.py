#!/usr/bin/env python3
"""
Manual PyPI publishing script for testing.
Run this locally to publish the package manually.
"""

import subprocess
import sys
import os

def main():
    print("Building package...")
    result = subprocess.run([sys.executable, "-m", "build"], capture_output=True, text=True)

    if result.returncode != 0:
        print("Build failed:")
        print(result.stderr)
        return 1

    print("Build successful!")
    print("To publish manually, run:")
    print("twine upload dist/*")
    print("")
    print("Make sure you have twine installed: pip install twine")
    print("And you have configured your PyPI credentials")

    return 0

if __name__ == "__main__":
    sys.exit(main())