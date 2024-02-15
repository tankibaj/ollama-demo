import requests
import base64
import time


# Function to encode the image to base64
def encode_image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Specify the path to your image file here
image_path = './art.jpg'  # Replace this with your actual image path

# Encode the image
encoded_image = encode_image_to_base64(image_path)

# Prepare the request payload
data = {
    "model": "llava",
    "prompt": "What is in this picture?",
    "stream": False,
    "images": [encoded_image]  # List of base64-encoded images
}

# API endpoint
url = 'https://llm.local.naim.run/api/generate'

if __name__ == '__main__':
    # Record the start time
    start_time = time.time()

    # Make the POST request
    response = requests.post(url, json=data)

    # Record the end time
    end_time = time.time()

    # Calculate the duration
    duration = round(end_time - start_time, 2)

    # Check if the request was successful
    if response.status_code == 200:
        response_data = response.json()
        print(response_data.get('response'))
        print(f"Request took: {duration} seconds.")
    else:
        print(f"Request failed with status code: {response.status_code}. Reason: {response.text}")
        # Print the duration even if the request failed
        print(f"Request took: {duration} seconds.")
