import joblib
import os
from src.data_processing import preprocess_single
import numpy as np

# Robust model path (Docker-safe)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.getenv("MODEL_PATH", os.path.join(BASE_DIR, "../models/xgboost_log_model.pkl"))

def load_model(path=MODEL_PATH):
    """
    Load the saved XGBoost model.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at {path}")
    print(f"Loading model from {path}")
    return joblib.load(path)

def prepare_input(data_dict):
    """
    Preprocess a single input dictionary and return a NumPy array
    suitable for model prediction.
    """
    X = preprocess_single(data_dict)  # returns DataFrame in correct feature order


    return X.values  # model expects 2D array
