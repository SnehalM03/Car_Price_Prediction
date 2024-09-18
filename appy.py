from flask import Flask,request,jsonify,render_template
import config
from utils import  CarPricePrediction

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/Prediction',methods=["POST"])
def prediction():
    data=request.get_json()
    print(data)
    Gender=data.get('Gender')
    Age=data['Age']
    Annual_Salary=data['Annual_Salary']
    Credit_Card_Debt=data['Credit_Card_Debt']
    Net_Worth=data['Net_Worth']
    Car_pred= CarPricePrediction()
    pred_price=Car_pred.get_predicted_price(Gender,Age,Annual_Salary,Credit_Card_Debt,Net_Worth)
    return jsonify({"Prediction of Total amount Customer is willing to pay for new car:":pred_price})




if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.FLASK_PORT_NUMBER,debug=True)