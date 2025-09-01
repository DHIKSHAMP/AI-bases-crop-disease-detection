# 🌱 Crop Disease Prediction using Deep Learning & Flask

This project is a **web-based crop disease prediction system** that uses a deep learning model trained on plant leaf images.  
It allows farmers and researchers to upload an image of a crop leaf and get:

- ✅ Predicted **disease type**  
- ✅ **Confidence score** of the prediction  
- ✅ **Crop type** (e.g., Tomato, Potato, Pepper)  
- ✅ **Disease description**  
- ✅ **Causes** and **Prevention techniques**  
- ✅ Data fetched dynamically from **MongoDB**  

---

## 📂 Project Structure
```
crop-disease-prediction/
│── app.py # Flask backend
│── models/
│ ├── crop_disease_model.h5 # Trained deep learning model
│ ├── labels.txt # Class labels
│── static/
│ ├── css/
│ │ └── styles.css # Styling for frontend
│ ├── uploads/ # Uploaded leaf images
│── templates/
│ ├── index.html # Upload page
│ ├── result.html # Result page
│── mongodb_setup.py # Script to insert disease info into MongoDB
│── README.md # Documentation
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/crop-disease-prediction.git
   cd crop-disease-prediction

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
   ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:

    Rename .env.example to .env.

    Update the variables inside .env with your own values (API keys, database URL, etc.).

5. **Run the Flask application:**

   ```bash
   flask run
   ```
6. **Open your browser and go to:**

    ```bash
    http://127.0.0.1:5000
    ```
---

## 🚀 Tech Stack

- **Python 3.11+**
- **Flask** (for web app)
- **TensorFlow / Keras** (for deep learning model)
- **MongoDB** (for disease info storage)
- **HTML, CSS** (for frontend)

---

## 📷Output:

<img width="1919" height="973" alt="Screenshot 2025-08-23 131045" src="https://github.com/user-attachments/assets/452dd068-a6ea-483e-afeb-85218a3c17f5" />
<img width="1919" height="972" alt="Screenshot 2025-08-26 114447" src="https://github.com/user-attachments/assets/8e9d6879-fbed-4cd5-903e-cb49b5c8b2a1" />
<img width="1919" height="967" alt="Screenshot 2025-08-26 114436" src="https://github.com/user-attachments/assets/44e26918-157e-497e-abd1-7ca360ef39e3" />
<img width="1919" height="970" alt="Screenshot 2025-08-23 131055" src="https://github.com/user-attachments/assets/6fdd2e7c-df54-466c-a325-76ca563a77a7" />



# 👤 Author

**DHIKSHA M P**  

🌐 GitHub: [@DHIKSHAMP](https://github.com/DHIKSHAMP)

🔗 LinkedIn: [linkedin.com/in/dhikshamp](https://linkedin.com/in/dhiksha-m-p-095028257)

🌍 Portfolio: [Portfolio](https://sites.google.com/view/dhikshacyber/about)

## ⚖️ License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) – see the [LICENSE](./LICENSE) file for details.

## 🌟 Contributing

💡 Got suggestions or new ideas?  
🛠️ Pull Requests are welcome!  
📧 Contact me if you'd like to collaborate.

