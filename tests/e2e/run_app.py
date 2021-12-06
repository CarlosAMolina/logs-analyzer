import os
import sys


if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
    from src_python import app

    app.app.run(debug=True)
