import os

FLASK_PORT_NUMBER=8080
 
PATH=os.path.dirname(os.path.abspath(__file__))

MODEL_FILE_NAME=os.path.join(PATH,"Artifacts","Car_price_prediction_model.pkl")

COLUMN_DATA=os.path.join(PATH,"Artifacts","column_data.json")

# CSV_FILE_NAME=os.path.join(PATH,"Data","Car_Purchasing_Data.csv")