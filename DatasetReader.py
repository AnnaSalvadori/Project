import pandas as pd
from abc import ABC, abstractclassmethod


''' General dataset reader interface'''
class DatasetReader(ABC):

    @abstractclassmethod
    def ReadDataset(self):
        pass

''' Specific dataset reader for GFF3'''
class DatasetReaderGFF3(DatasetReader):
    def __init__(self, filename): 
        self.dataframe = filename


    def ReadDataset(self, filename):
        df = pd.read_csv(
        filename,
        sep="\t",
        comment="#",
        names=[
            "seq_id",
            "source",
            "type",
            "start",
            "end",
            "score",
            "strand",
            "phase",
            "attributes",
            ],
        )
        return pd.DataFrame(df)
    
   