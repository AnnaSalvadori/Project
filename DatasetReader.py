import pandas as pd
from abc import ABC, abstractclassmethod


''' General dataset reader interface'''
class DatasetReader(ABC):

    @abstractclassmethod
    def readDataset(self):
        pass

    
''' Specific dataset reader for GFF3'''
class DatasetReaderGFF3(DatasetReader):
    def __init__(self, filename): 
        self.__dataframe = filename


    def readDataset(self) -> pd.core.frame.DataFrame:
        df = pd.read_csv(
        self.__dataframe,
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
        return df
    
   
