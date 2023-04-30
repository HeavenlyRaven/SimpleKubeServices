import os
import requests
from flask import Flask

app = Flask(__name__)

BACKEND_HOST = os.getenv('BACKEND_HOST', 'localhost')
BACKEND_PORT = os.getenv('BACKEND_PORT', 8080)

@app.route('/')
def index():
    response = requests.get(f'http://{BACKEND_HOST}:{BACKEND_PORT}/')
    return response.content

if __name__ == '__main__':
    app.run(debug=True)
