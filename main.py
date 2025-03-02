import os
from flask import Flask, render_template, url_for
import shutil

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_key")

# Ensure the images directory exists
images_dir = os.path.join(app.static_folder, 'images')
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Copy the uploaded images to the static folder
try:
    shutil.copy('attached_assets/20240730_001114200_iOS.jpg', os.path.join(images_dir, 'professional.jpg'))
    shutil.copy('attached_assets/thumbnail_IMG_4059.jpg', os.path.join(images_dir, 'athletic.jpg'))
except FileNotFoundError:
    print("Warning: 'attached_assets' files not found. Skipping image copy.")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('index.html')  # Placeholder

@app.route('/contact')
def contact():
    return render_template('index.html')  # Placeholder

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)