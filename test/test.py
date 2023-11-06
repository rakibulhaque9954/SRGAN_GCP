import requests

response = requests.post('https://model-znzp2767aq-an.a.run.app', files={'file': open('test_img.jpg', 'rb')})

try:
    data = response.json()
    print(data)
except requests.exceptions.JSONDecodeError as json_err:
    print(f"Failed to decode JSON from response: {json_err}")
    print("Response content:", response.text)