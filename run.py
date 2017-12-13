from app import create_app, socketio

app = create_app(host='127.0.0.1', debug=True)

if __name__ == '__main__':
    socketio.run(app)
f
