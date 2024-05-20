from flask import render_template,Response
from app import app, utils
import io
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate_image():
    width = 256
    height = 128
    pixel_size = 4

    colors = utils.generate_colors()
    image = utils.create_image(colors, width, height, pixel_size)

    img_io = io.BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)

    timestamp = int(time.time() * 1000)  # Generate a timestamp in milliseconds
    response = Response(img_io.getvalue(), mimetype='image/png')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Last-Modified'] = timestamp
    return response