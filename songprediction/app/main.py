from fastapi import FastAPI, HTTPException
from app.schemas import SongFeatures
from app.api_utils import load_model, prepare_input
import numpy as np

app = FastAPI(title="Song Popularity Prediction API")
model = load_model()

# DEBUG: Print model feature names
try:
    print("MODEL EXPECTS (booster):", model.get_booster().feature_names)
except:
    try:
        print("MODEL EXPECTS (sklearn):", model.feature_names_in_)
    except:
        print("MODEL EXPECTS: UNKNOWN (model format not recognized)")


@app.get("/")
def root():
    return {"message": "Song Popularity Prediction API"}


@app.post("/predict")
def predict(item: SongFeatures):
    try:
        data = item.dict()

        X = prepare_input(data)

        pred_log = model.predict(X)[0]
        pred = float(np.expm1(pred_log))

        return {"predicted_streams": pred}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
