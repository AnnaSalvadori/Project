import pandas as pd
from abc import ABC, abstractclassmethod
from DatasetReader import *


''' General interface Dataset class'''
class Dataset(ABC):

    @abstractclassmethod
    def dataframe(self):
        pass


'''Specific Dataset class'''
class DatasetGFF3(Dataset):
    
    def __init__(self, filename):
        self.__df = DatasetReaderGFF3(filename).ReadDataset()
    
    @property
    def dataframe(self) -> pd.core.frame.DataFrame:
        return self.__df
