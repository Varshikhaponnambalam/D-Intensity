from flask import Flask, request, render_template, redirect, url_for
import base64
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game',methods=['POST'])
def game():
    return render_template('game.html')

@app.route('/upload', methods=['POST'])
def upload():
    image_data = request.form['image']
    if image_data:
        # Decode the Base64 encoded image
        image_data = image_data.split(",")[1]
        image_data = base64.b64decode(image_data)
        
        # Save the image file
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        with open(filepath, 'wb') as f:
            f.write(image_data)
        
        return f"Image saved to {filepath}"
    return "No image data received", 400

if __name__ == '__main__':
    app.run(debug=True)
