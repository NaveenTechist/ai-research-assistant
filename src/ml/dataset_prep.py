import pandas as pd

class DatasetPreparator:

    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path

    def load_dataset(self):
        return pd.read_csv(self.dataset_path)

    def prepare(self):
        dataset = self.load_dataset()

        texts = dataset["data"].astype(str).to_numpy()
        labels = dataset["labels"].astype(str).to_numpy()

        return texts, labels