import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


response = requests.post(' https://srgan-model-ver-1-znzp2767aq-an.a.run.app', files={'file': open('test_img.jpg', 'rb')})

try:
    data = response.json()
    print(data)
except requests.exceptions.JSONDecodeError as json_err:
    print(f"Failed to decode JSON from response: {json_err}")
    print("Response content:", response.text)

gen_img_list = data['Prediction Tensor']

# Convert the list back to a NumPy array
gen_img_np = np.array(gen_img_list)
plt.title('LR Image')
plt.imshow(gen_img_np[0,:,:,:])
plt.show()
# gen_img = Image.fromarray((gen_img_np[0] * 255).astype(np.uint8))
# gen_img.show()