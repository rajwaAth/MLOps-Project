import pandas as pd
import numpy as np
from pathlib import Path
import joblib

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_training/model.joblib"))

    def predict(self, input_data):
        prediction = np.round(self.model.predict(input_data), 0)

        return prediction