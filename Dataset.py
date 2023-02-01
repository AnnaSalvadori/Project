#import pandas as pd
from abc import ABC, abstractclassmethod
from DatasetReader import *


''' General interface Dataset class'''
class Dataset(ABC):

    @abstractclassmethod
    def __init__(self):
        pass


'''Specific Dataset class'''
class DatasetGFF3(Dataset):
    def __init__(self, filename):
        self.__df = DatasetReaderGFF3.ReadDataset (self, filename)
    
    # getter ?
    def getDataframe(self): 
        return self.__df

'''eliminare?'''
class DatasetPandas (Dataset):
    def __init__(self, df = None):
        self.__df = df
    
    def getDataframe(self):
        return self.__df
