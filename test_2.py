import numpy as np
from PIL import Image
from keras.models import load_model
from flask import Flask, jsonify, request
from io import BytesIO
import io

generator = load_model('gen25000v2.4.h5')


# generator.summary()

def restructure_img(file):
    try:
        # Read the image via file.stream
        img = Image.open(BytesIO(file.read())).convert('L')

        # Resize the image
        img = img.resize((64, 64), Image.Resampling.LANCZOS)

        # Convert image to RGB
        img = img.convert('RGB')

        # Normalize the image
        img_lr = np.asarray(img) / 255.0
        img_lr = np.expand_dims(img_lr, axis=0)

        return img_lr
    except Exception as e:
        raise e


def predict(img_lr):
    gen_img = generator.predict(img_lr)
    # print(gen_img.shape)
    # Convert the output to image (if needed, depends on your generator's output)
    # gen_img = Image.fromarray((gen_img[0] * 255).astype(np.uint8))
    # gen_img.show()
    gen_img_list = gen_img.tolist()

    # Return as a JSON response
    return gen_img_list


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == '':
            return jsonify({'error': 'no_file'})

        try:
            img_lr = restructure_img(file)
            prediction = predict(img_lr)
            return jsonify({
        'Prediction Tensor': prediction
    })
        except Exception as e:
            return jsonify({'error': str(e)})
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
