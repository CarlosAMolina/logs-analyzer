from . import app
from . import config


if __name__ == "__main__":
    app.app.run(port=config.PORT, debug=True)
