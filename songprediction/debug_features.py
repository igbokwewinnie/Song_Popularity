import joblib

model = joblib.load("models/xgboost_log_model.pkl")

print("\nBOOSTER FEATURES:", len(model.get_booster().feature_names))
print(model.get_booster().feature_names)

# NEW: print the true training feature count
print("\nMODEL n_features_in_ =", model.n_features_in_)
