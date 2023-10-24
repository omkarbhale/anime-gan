from flask import Flask, request, send_file
from PIL import Image
from flask_cors import CORS
from _model import inference

app = Flask(__name__)
CORS(app)

@app.route('/convert-to-anime', methods=['POST'])
def convert_to_anime():
    # Get the uploaded image from the request
    uploaded_image = request.files['image']

    if uploaded_image:
        # Process the image using the inference function
        image = Image.open(uploaded_image)
        processed_image = inference(image, 'version 2 (🔺 robustness,🔻 stylization)')

        # Save the processed image to a temporary file
        processed_image_path = 'processed_image.jpg'
        processed_image.save(processed_image_path)

        # Return the processed image as a response
        return send_file(processed_image_path, mimetype='image/jpeg')
    else:
        return "No image uploaded", 400

if __name__ == '__main__':
    app.run(debug=True)
