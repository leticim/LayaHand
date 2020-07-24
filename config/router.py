from flask import Flask
from app.controllers import home_controller

instance_home_controller = home_controller.HomeController()
def rouuter():
    app = Flask(__name__)

    @app.route('/')
    def get():
        return instance_home_controller.get()
    
    return app
   
