import os
import sys
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import logging
import pandas as pd
@dataclass
class DataIngestionConfig : ## where to save train and test part
    train_data_path : str = os.path.join('artfact',"train.csv") 
    test_data_path : str = os.path.join('artfact',"test.csv") 
    row_data_path : str = os.path.join('artfact',"data.csv") 

class DataIngestion :
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Enterd the Data Ingestion method Or component")

        try :
            df = pd.read_csv("nootbook\data\stud.csv")
            logging.info( 'Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path) , exist_ok=True)

             ## save row data
            df.to_csv(self.ingestion_config.row_data_path, index = False , header = True)
            logging.info('Train Test Split initiated')
            # split the data 
            train_set , test_set = train_test_split(df , test_size = 0.2 , random_state = 0)
            ## save train data
            train_set.to_csv(self.ingestion_config.train_data_path, index = False , header = True)
            ## save test data
            test_set.to_csv(self.ingestion_config.test_data_path, index = False , header = True)

            logging.info('Ingestion of the data is completed')

            return (

                self.ingestion_config.train_data_path ,
                self.ingestion_config.test_data_path 
            )

        except:
            pass

if __name__ =="__main__" :
    obj = DataIngestion()
    obj.initiate_data_ingestion()