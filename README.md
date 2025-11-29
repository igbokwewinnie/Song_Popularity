 # 🎵 Song Popularity Prediction – End‑to‑End ML Project
A full end-to-end machine learning system that predicts song popularity using audio, platform & engagement features.

<img width="1920" height="1020" alt="Screenshot 2025-11-29 101847" src="https://github.com/user-attachments/assets/3415c457-b1fb-4e8a-8ddd-79cd9046de6a" />

---

## 📌 Project Overview

Music platforms rely heavily on data to identify high-potential tracks and optimize promotion strategies.
This project builds a full ML system that:
- Predicts song popularity based on cross-platform metrics
- Helps A&R and Marketing teams make data-driven decisions
- Provides insights into which factors boost a song’s streaming success
- Uses a modular code structure + model deployment via FastAPI & Docker

Why it's useful:
✔ Helps music companies scout promising songs
✔ Shows which metrics influence viral success
✔ Deployable as a microservice for internal teams


<img width="1920" height="1020" alt="Screenshot 2025-11-29 101912" src="https://github.com/user-attachments/assets/fc9da6bb-8a5b-4aa1-a9c6-13535993a970" />

---

## 🚀 Key Features

* End‑to‑end ML workflow
* Extensive data preprocessing
* Multiple model training & evaluation
* Log‑transformed regression modeling
* Model persistence using `joblib`
* FastAPI backend for predictions
* Dockerized application for deployment
* Modular and production‑ready folder structure

---

## 📂 Project Structure

```
songprediction/
│
├── Most Streamed Spotify Songs 2024.csv/
│   └── Most Streamed Spotify Songs 2024.csv
│
├── notebooks/
│   └── untitled.ipynb
│
├── models/
│   └── xgboost_log_model.pkl
│
├── app/
│   ├── main.py
│   └── schemas.py
|   └── api_utils.py
|   └── requirements.txt
|
├── src/
|   ├── data_processing.py 
│
├── debug_features.py
├── Dockerfile
├── README.md
└── .gitignore
```

---

## 🧠 Machine Learning Workflow

### **1️⃣ Data Preprocessing**

* Handled missing values
* Cleaned numeric fields stored as text
* Converted date fields
* Removed duplicates
* Transformed skewed variables (log transformation)

### **2️⃣ Feature Engineering**

* Extracted year from release date
* Normalized numeric features
* Encoded categorical variables

### **3️⃣ Model Training**

Trained and compared:

* Linear Regression
* Random Forest
* XGBoost (best performing model)

🏆 **Final Model:** XGBoost Regressor with log‑transformed target

### **4️⃣ Model Saving**

Saved using joblib:

```
joblib.dump(model, "../models/xgboost_log_model.pkl")
```

---

## ⚡ API Deployment (FastAPI)

### **Run API locally:**

```
uvicorn api.main:app --reload
```

### **Prediction Endpoint**

`POST /predict`

**Example JSON body:**

```
{
  "spotify_streams": 5000000,
  "spotify_playlist_count": 120,
  "spotify_playlist_reach": 850000,
  "youtube_views": 2500000,
  "youtube_likes": 150000,
  "tiktok_posts": 3000,
  "tiktok_likes": 200000,
  "tiktok_views": 10000000,
  "youtube_playlist_reach": 900000,
  "apple_music_playlist_count": 50,
  "airplay_spins": 2300,
  "deezer_playlist_count": 40,
  "deezer_playlist_reach": 300000,
  "amazon_playlist_count": 25,
  "pandora_streams": 750000,
  "pandora_track_stations": 8000,
  "shazam_counts": 90000,
  "explicit_track": 1,
  "artist_encoded": 42,
  "release_date": "2023-05-12"
}
```

**Response:**

```
{
  "predicted_popularity": 82.4
}
```

---

## 🐳 Docker Deployment

### **Build the Docker image:**

```
docker build -t song-prediction-api .
```

### **Run the container:**

```
docker run -p 8000:8000 song-prediction-api
```

API will be available at:

```
http://localhost:8000/docs
```

---

## 📦 Requirements

Install dependencies:

```
pip install -r requirements.txt
```

Key packages:

* FastAPI
* Uvicorn
* XGBoost
* Joblib
* Pandas
* Scikit‑learn

---

## 📝 Future Improvements

* Add a frontend web UI
* Integrate CI/CD with GitHub Actions
* Implement monitoring with Prometheus
* Add model retraining pipeline using Airflow

---

9. FAQ / Troubleshooting

Model not found?
Check that models/xgboost_log_model.pkl exists and the path is correct.

Docker fails on Windows?
Enable WSL2 under “Turn Windows Features On or Off.”

---

## 🙌 Acknowledgements

Built as a personal ML engineering project to demonstrate skills in:

* Machine Learning
* MLOps
* API development
* Docker
* Data engineering fundamentals

---

## ⭐ Support

If you like this project, give it a **star** on GitHub! 🌟
