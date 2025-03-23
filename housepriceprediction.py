from fastapi import FastAPI, Form
import numpy as np
import joblib
from fastapi.responses import HTMLResponse

# Load the trained model
model = joblib.load("house_price_model.pkl")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>House Price Prediction</title>
        </head>
        <body>
            <h2>Enter House Details</h2>
            <form action="/predict" method="post">
                Median Income: <input type="text" name="median_income"><br>
                Total Rooms: <input type="text" name="total_rooms"><br>
                Housing Median Age: <input type="text" name="housing_median_age"><br>
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """

@app.post("/predict")
def predict(
    median_income: float = Form(...), 
    total_rooms: float = Form(...), 
    housing_median_age: float = Form(...)
):
    features = np.array([[median_income, total_rooms, housing_median_age]])
    prediction = model.predict(features)[0]
    return {"predicted_price": prediction}


