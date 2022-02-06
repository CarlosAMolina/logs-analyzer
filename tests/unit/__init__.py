import os
import sys

os.environ["VT_KEY"] = "foo"

PROJECT_PATH = os.path.join(os.path.dirname(__file__), "../../src")
sys.path.append(PROJECT_PATH)
