import pickle
import numpy as np
import tensorflow as tf

MODEL_PATH = "models/tf_classifier.h5"
LABEL_ENCODER_PATH = "models/label_encoder.pkl"

class DocumentPredictor:

    def __init__(self):
        self.model = tf.keras.models.load_model(
            MODEL_PATH
        )

        with open(
            LABEL_ENCODER_PATH,
            "rb"
        ) as file:
            self.label_encoder = pickle.load(
                file
            )

    def predict(
        self,
        text: str
    ):
        prediction = self.model.predict(
            np.array([text]),
            verbose=0
        )

        predicted_index = int(
            np.argmax(prediction)
        )

        confidence = float(
            prediction[0][predicted_index]
        )

        category = self.label_encoder.inverse_transform(
            [predicted_index]
        )[0]

        return {
            "category": category,
            "confidence": round(
                confidence,
                4
            )
        }