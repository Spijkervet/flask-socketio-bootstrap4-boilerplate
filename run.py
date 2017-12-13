import os.path
from app import create_app, socketio


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

app = create_app(DB_PATH)
app.host = '127.0.0.1'
app.debug = False


if __name__ == '__main__':
    socketio.run(app)
