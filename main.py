import numpy as np
import cv2
from keras.models import load_model
from flask import Flask, jsonify, request

generator = load_model('gen25000v3.1.h5')
# generator.summary()


def restructure_img(file):
    try:
        img = cv2.imdecode(np.asarray(bytearray(file.read()), dtype=np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (64, 64))
        img_lr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_lr = img_lr / 255.
        img_lr = np.expand_dims(img_lr, axis=0)
        return img_lr
    except Exception as e:
        raise e


def predict(img_lr):
    gen_img = generator.predict(img_lr)
    # print(gen_img.shape)
    # plt.imshow(gen_img[0, :, :, :])
    # plt.show()
    return gen_img.shape


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
            data = {'Prediction': prediction}
            return jsonify(data)
        except Exception as e:
            return jsonify({'error': str(e)})
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=8080)
