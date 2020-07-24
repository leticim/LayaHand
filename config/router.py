from flask import Flask

def rouuter():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    return app
   
