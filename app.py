from flask import Flask
import os
import webbrowser

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! (mrakashani)"
    webbrowser.open('127.0.0.1')

#if __name__ == '__main__':
#    port = os.environ.get('FLASK_PORT') or 8080
#    port = int(port)


    app.run(port=port,host='0.0.0.0')