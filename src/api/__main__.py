from . import app as m_app


if __name__ == "__main__":
    app = m_app.get_app()
    app.run()
