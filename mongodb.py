from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()


mongo_client = MongoClient(os.getenv("MONGO_URI"))
db = mongo_client[os.getenv("MONGO_DB")]
collection = db[os.getenv("MONGO_COLLECTION")]

disease_data = [
    {
        "label": "Tomato_healthy",
        "crop": "Tomato",
        "description": "The tomato leaf is healthy with no visible disease symptoms.",
        "causes": "Healthy plants with no pathogen infection.",
        "prevention": "Maintain good agricultural practices like proper watering, fertilization, and pest control."
    },
    {
        "label": "Tomato_mosaic_virus",
        "crop": "Tomato",
        "description": "Tomato mosaic virus causes mottling and distortion of leaves, stunted growth, and reduced yield.",
        "causes": "Caused by the Tomato mosaic virus, spread through infected seeds, tools, and plant contact.",
        "prevention": "Use certified virus-free seeds, disinfect tools, and remove infected plants."
    },
    {
        "label": "Tomato_YellowLeaf__Curl_Virus",
        "crop": "Tomato",
        "description": "Yellow Leaf Curl Virus causes yellowing, curling of leaves, stunted growth, and reduced fruit production.",
        "causes": "Spread by whiteflies carrying the Tomato Yellow Leaf Curl Virus (TYLCV).",
        "prevention": "Control whitefly population, use resistant varieties, and remove infected plants."
    },
    {
        "label": "Tomato_Target_Spot",
        "crop": "Tomato",
        "description": "Target spot causes small brown lesions on leaves that enlarge with concentric rings.",
        "causes": "Caused by the fungus Corynespora cassiicola.",
        "prevention": "Use crop rotation, improve air circulation, and apply fungicides if needed."
    },
    {
        "label": "Potato_healthy",
        "crop": "Potato",
        "description": "The potato plant is healthy with no disease symptoms.",
        "causes": "Healthy growth due to proper nutrient and pest management.",
        "prevention": "Maintain crop hygiene, proper irrigation, and regular monitoring."
    },
    {
        "label": "Potato_Late_blight",
        "crop": "Potato",
        "description": "Late blight causes dark, water-soaked lesions on leaves and tubers, spreading rapidly.",
        "causes": "Caused by Phytophthora infestans under cool, moist conditions.",
        "prevention": "Plant resistant varieties, ensure good drainage, avoid overhead irrigation, and use fungicides."
    },
    {
        "label": "Pepper_bell_healthy",
        "crop": "Pepper Bell",
        "description": "The pepper plant is healthy with no visible symptoms.",
        "causes": "Healthy growth under favorable conditions with no disease infection.",
        "prevention": "Follow good cultural practices, proper watering, and pest control."
    }
]

# insert data
collection.insert_many(disease_data)

print("Disease data inserted successfully into MongoDB!")
