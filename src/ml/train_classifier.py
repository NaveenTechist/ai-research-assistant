import os
import pickle
import tensorflow as tf
import keras
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from src.ml.dataset_prep import DatasetPreparator

MODEL_PATH = "models/tf_classifier.keras"
LABEL_ENCODER_PATH = "models/label_encoder.pkl"

print("TensorFlow:", tf.__version__)
print("Keras:", tf.keras.__version__)

class DocumentClassifier:

    def __init__(self):
        self.vectorizer = tf.keras.layers.TextVectorization(
            max_tokens=20000,
            output_mode="int",
            output_sequence_length=300
        )
        self.label_encoder = LabelEncoder()
        self.model = None

    def build_model(self, num_classes):
        model = tf.keras.Sequential([
            self.vectorizer,
            tf.keras.layers.Embedding(
                input_dim=20000,
                output_dim=128
            ),
            tf.keras.layers.GlobalAveragePooling1D(),
            tf.keras.layers.Dense(
                128,
                activation="relu"
            ),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(
                64,
                activation="relu"
            ),
            tf.keras.layers.Dropout(0.3),
            tf.keras.layers.Dense(
                num_classes,
                activation="softmax"
            )
        ])

        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )

        self.model = model

    def train(self):
        dataset = DatasetPreparator(dataset_path="data/dataset/bbc_data.csv")
        texts, labels = dataset.prepare()

        encoded_labels = self.label_encoder.fit_transform(labels)

        x_train, x_test, y_train, y_test = train_test_split(
            texts,
            encoded_labels,
            test_size=0.2,
            random_state=42,
            stratify=encoded_labels
        )

        self.vectorizer.adapt(x_train)


        self.build_model(
            len(self.label_encoder.classes_)
        )
        
        print(type(y_train))
        print(y_train.dtype)
        self.model.fit(
            x_train,
            y_train,
            validation_data=(x_test, y_test),
            epochs=10,
            batch_size=32
        )

        loss, accuracy = self.model.evaluate(
            x_test,
            y_test
        )

        print(f"Test Accuracy: {accuracy:.4f}")

        os.makedirs(
            "models",
            exist_ok=True
        )

        self.model.save(
            MODEL_PATH
        )

        with open(
            LABEL_ENCODER_PATH,
            "wb"
        ) as file:
            pickle.dump(
                self.label_encoder,
                file
            )

        print("Model saved successfully.")

if __name__ == "__main__":
    classifier = DocumentClassifier()
    classifier.train()