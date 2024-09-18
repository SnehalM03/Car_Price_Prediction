import pandas as pd
import numpy as np
import config
import json
import pickle
import warnings
warnings.filterwarnings('ignore')

class CarPricePrediction():
    def __init__(self):
        pass
    def load_data(self):
        with open(config.MODEL_FILE_NAME,'rb')as f:
            self.model=pickle.load(f)
        with open(config.COLUMN_DATA,'r')as f:
            self.column_data=json.load(f)

        self.column_name=self.model.feature_names_in_
        self.feature_count=self.model.n_features_in_
    
    def get_predicted_price(self,Gender,Age,Annual_Salary,Credit_Card_Debt,Net_Worth):
        self.load_data()
        Gender=self.column_data['Gender'][Gender]
        test_array=np.zeros((1,self.feature_count))
        test_array[0,0]=Gender
        test_array[0,0]=Age
        test_array[0,0]=Annual_Salary
        test_array[0,0]=Credit_Card_Debt
        test_array[0,0]=Net_Worth
        Predicted_Price=np.around(self.model.predict(test_array)[0],2)
        return Predicted_Price
#     def load_dataset():
#         df=pd.read_csv(config.CSV_FILE_NAME)
#         return df
        
# if __name__=="__main__":
#     ins=CarPricePrediction()
#     ins.load_data()
#     print(list(ins.column_data['Gender'].keys()))