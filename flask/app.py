from flask import Flask, render_template, request
import numpy, joblib, xgboost
import pandas as pd

app = Flask(__name__)

#get needed data from joblib file
model_details=joblib.load('./final_model_details.joblib')
xgb_model=model_details['xgb_model']
preprocessing=model_details['preprocessing']
brand=model_details['brand']
model=model_details['model']
seats=model_details['seats']
body_type=model_details['body_type']
rear_tyres=model_details['rear_tyres']

@app.route("/")
def index():
    driven_wheels = ['4x2', '4x4', 'All Wheel Drive', 'Front Wheel Drive', 'Rear Wheel Drive']

    return render_template("index.html", brands=brand,models=model,seats=seats,
                           body_types=body_type,rear_tyres=rear_tyres,driven_wheels =driven_wheels)


@app.route("/prediction", methods=['POST'])
def predict():
    form = request.form
    X_transformed = transform_input(form)
    prediction = predict_value(X_transformed)
    print(f"returning prediction :{(prediction[0])}")
    return {"price": (prediction[0])}

# transform_input : transforms incoming form to a format acceptable by our machine learning model
def transform_input(form):
    values = list(form.values())
    columns = form.keys()
    df = pd.DataFrame(data=[values], columns=columns)
    df['Year']=df['Year'].astype('int64')
    df['Power maximum (detail)']=df['Power maximum (detail)'].astype('float64')
    df['Torque maximum']=df['Torque maximum'].astype('float64')
    df['Maximum/top speed']=df['Maximum/top speed'].astype('float64')

    print(df.columns)
    print(df.values)
    return preprocessing.transform(df)

# predict_value: predicts the value sent to the API
def predict_value(X_transformed):
    predictions = xgb_model.predict(X_transformed)
    return predictions.tolist()

if __name__ == "__main__":
    app.run()
