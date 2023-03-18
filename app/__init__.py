from flask import Flask, render_template, flash, request, url_for
import requests
import openai
import json


def create_app(api_key:str):
    app = Flask(__name__)
    openai.api_key = api_key

    # Function to make a request to openai, returns URL of image 
    def generate_image(image_description:str):
        url = "https://api.openai.com/v1/images/generations"
        model = "image-alpha-001"
        data = {
            "model": model,
            "prompt": image_description,
            "num_images": 1,
            "size": "512x512",
            "response_format": "url"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}"
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_json = response.json()
            image_url = response_json['data'][0]['url']
            return image_url
        else:
            raise Exception("Failed to generate image")


    # Main route
    @app.route('/', methods = ['POST', 'GET'])
    def home():
        result = None
        description = None

        if request.method == 'POST':
            description = request.form.get('description')
            result = generate_image(description)
           
        return render_template('index.html', result = result, description = description)

    return app

