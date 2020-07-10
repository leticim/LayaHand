#from flask import Flask
import sys
import os
from config import router
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP_ROOT)
#import router
app = router.rouuter()

if __name__ == '__main__':
    print("hey")
    app.run(host='0.0.0.0')