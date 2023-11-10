from flask import Flask, render_template, request
import pickle

import numpy as np
import pandas as pd
import PIL


app = Flask(__name__, static_folder='static', static_url_path='/static')

model = pickle.load(open('CNN_Tea_Leaf_Disease_Detection.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    uploaded_file = request.files['image']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)  # Save the uploaded file
        #return "File uploaded successfully!"
        return predict()
    return "No file uploaded."

def predict():
    # Get the image from the request
    image = request.files["image"]
    image = PIL.Image.open(image).resize((224, 224))
    x = np.array(image)
    x = np.expand_dims(x, axis=0)
    pred = np.argmax(model.predict(x))
    
    op = ['Anthracnose', 'Algal Leaf', 'Bird Eye Spot', 'Brown Blight', 'Gray Blight', 'Healthy', 'Red Leaf Spot', 'White Spot']
    	
    # Return the prediction
    return render_template("index.html", prediction=op[pred])


if __name__ == '__main__':
    app.run(debug=True)


