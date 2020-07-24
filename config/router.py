from flask import Flask

def app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    return app
   
