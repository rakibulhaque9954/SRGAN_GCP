from flask import Flask, render_template, request, url_for
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename
import os
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_PATH'] = 1024 * 1024 * 2  # 2 MB limit for uploads

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            original_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(original_file_path)

            # Posting to the SRGAN model service
            response = requests.post('https://srgan-model-ver-1-znzp2767aq-an.a.run.app',
                                     files={'file': open(original_file_path, 'rb')})

            try:
                data = response.json()
            except requests.exceptions.JSONDecodeError as json_err:
                print(f"Failed to decode JSON from response: {json_err}")
                print("Response content:", response.text)
                return render_template('index.html', error='Could not decode the response.')

            # Convert the list back to a NumPy array and then to an image
            gen_img_list = data['Prediction Tensor']
            gen_img_np = np.array(gen_img_list)
            gen_img = Image.fromarray((gen_img_np[0] * 255).astype(np.uint8))

            # Save the generated image
            enhanced_filename = f'enhanced_{filename}'
            enhanced_file_path = os.path.join(app.config['UPLOAD_FOLDER'], enhanced_filename)
            gen_img.save(enhanced_file_path)

            return render_template('result.html',
                                   original_image=url_for('static', filename=f'uploads/{filename}'),
                                   generated_image=url_for('static', filename=f'uploads/{enhanced_filename}'),
                                   original_download=original_file_path,
                                   enhanced_download=enhanced_file_path)
        else:
            return render_template('index.html', error='Invalid file type.')
    return render_template('index.html')

@app.route('/test_image')
def test_image():
    default_image_filename = 'test_img.jpeg'  # Replace with your default image file name
    original_file_path = os.path.join(app.config['UPLOAD_FOLDER'], default_image_filename)

    # Posting to the SRGAN model service
    response = requests.post('https://srgan-model-ver-1-znzp2767aq-an.a.run.app',
                             files={'file': open(original_file_path, 'rb')})

    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError as json_err:
        print(f"Failed to decode JSON from response: {json_err}")
        print("Response content:", response.text)
        return render_template('index.html', error='Could not decode the response.')

    # Convert the list back to a NumPy array and then to an image
    gen_img_list = data['Prediction Tensor']
    gen_img_np = np.array(gen_img_list)
    gen_img = Image.fromarray((gen_img_np[0] * 255).astype(np.uint8))

    # Save the generated image
    enhanced_filename = f'enhanced_{default_image_filename}'
    enhanced_file_path = os.path.join(app.config['UPLOAD_FOLDER'], enhanced_filename)
    gen_img.save(enhanced_file_path)

    return render_template('result.html',
                           original_image=url_for('static', filename=f'uploads/{default_image_filename}'),
                           generated_image=url_for('static', filename=f'uploads/{enhanced_filename}'))



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

if __name__ == '__main__':
    app.run(debug=True)