from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'


mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client[os.getenv("MONGO_DB")]
collection = db[os.getenv("MONGO_COLLECTION")]

    # Load model
model = tf.keras.models.load_model("models/crop_disease_model.h5")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded"
        
    file = request.files['file']
    if file.filename == "":
        return "No file selected"

    # ✅ Clean the filename (removes spaces, %, etc.)
    filename = secure_filename(file.filename)

    # Save uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

        # Preprocess image
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

        # Prediction
    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)
    confidence = np.max(predictions)

    # Load labels
    with open("models/labels.txt") as f:
        labels = [line.strip() for line in f]

    # ✅ Pass clean filename to url_for
    image_url = url_for('static', filename=f'uploads/{filename}')
        
    predicted_label = labels[class_index]
    predicted_label = predicted_label.replace("__", "_")

    disease_data = collection.find_one({"label": {"$regex": f"^{predicted_label}$", "$options": "i"}})

    if disease_data:
        crop_type = disease_data.get("crop", "Unknown")
        description = disease_data.get("description", "No details available.")
        causes = disease_data.get("causes", "N/A")
        prevention = disease_data.get("prevention", "N/A")
    else:
        crop_type = "Unknown"
        description = "No details available."
        causes = "N/A"
        prevention = "N/A"

    return render_template(
    "result.html",
    prediction=predicted_label,
    confidence=confidence,
    image_url=image_url,
    crop_type=crop_type,
    description=description,
    causes=causes,
    prevention=prevention
)



if __name__ == '__main__':
    app.run(debug=True)
