import os


class Config:
    """
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    """

    DEBUG = True
    SERVER_NAME = "{host}:{port}".format(
        host="127.0.0.1",
        port="5000",
    )
    SQLALCHEMY_DATABASE_URI = (
        "{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}".format(
            dialect="postgresql",
            driver="psycopg2",
            username=os.environ["DB_USERNAME"],
            password=os.environ["DB_PASSWORD"],
            host="localhost",
            port=5432,
            database="logs_analyzer",
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
