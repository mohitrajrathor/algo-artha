import os

class DataIngestion:
    def __init__(self):
        """
        Facilitate data ingestion.
        """
        self.TrainDataPath = os.path.join("/data", "train.csv")

