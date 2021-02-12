# Import QRCode from pyqrcode
import pyqrcode
import json
import png
from pyqrcode import QRCode
from flask import send_file
from flask import request
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/QRGen', methods=['GET', 'POST'])
def hello_world():
    id = request.form["id"]
    capacity = request.form["cap"]
    # String which represents the QR code
    s = {
        "id": id,
        "capacity": capacity
    }
    jsonData = json.dumps(s)
    # Generate QR code
    url = pyqrcode.create(jsonData)

    # Create and save the svg file naming "myqr.svg"
    url.png("myqr.png", scale=8)

    return send_file('myqr4.png')


if __name__ == '__main__':
    app.run()
