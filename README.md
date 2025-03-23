# 🏡 House Price Prediction

# 📌 Overview

This project is a Machine Learning-based House Price Prediction System built using FastAPI and Linear Regression. It predicts house prices based on key features such as median income, total rooms, and housing median age. The project includes:

  ✅ Machine Learning Model (Linear Regression)
  
  ✅ FastAPI Backend for real-time predictions
  
  ✅ Simple Web UI for user-friendly input
  
  ✅ Dataset from the California Housing Data

# ⚙️ Tech Stack

  🔹 Python - Core programming language
  
  🔹 FastAPI - For building the web API
  
  🔹 Scikit-Learn - For model training
  
  🔹 Pandas & NumPy - For data handling
  
  🔹 Joblib - For model saving/loading
  
  🔹 Uvicorn - For running the FastAPI server
  

# 📂 Project Structure

  📁 House Price Prediction
  
      │── 📜 housepriceprediction.py  # Main FastAPI application
      
      │── 📜 house_price_model.pkl    # Trained ML model
      
      │── 📜 requirements.txt         # Dependencies
      
      │── 📜 README.md                # Project documentation

# 🚀 Installation & Setup

  1️⃣ Clone the Repository

    git clone https://github.com/yourusername/house-price-prediction.git
    cd house-price-prediction

  2️⃣ Create a Virtual Environment (Optional but Recommended)

    python -m venv venv
    
    source venv/bin/activate   # On macOS/Linux
    
    venv\Scripts\activate      # On Windows

  3️⃣ Install Dependencies

    pip install -r requirements.txt

  4️⃣ Run the FastAPI Server

    uvicorn housepriceprediction:app --reload

    Server will start at: http://127.0.0.1:8000/

# 🎯 Usage

  🌐 Access the Web Interface

    1️⃣ Open http://127.0.0.1:8000/ in your browser.
    
    2️⃣ Enter values for Median Income, Total Rooms, Housing Median Age.
    
    3️⃣ Click Predict to get the estimated house price.

# 🔥 API Endpoint Usage

  📌 POST request to /predict
  
     curl -X 'POST' \
      'http://127.0.0.1:8000/predict' \
      
      -H 'Content-Type: application/json' \
      
      -d '{"median_income": 5.2, "total_rooms": 3000, "housing_median_age": 20}'

  🔹 Response: { "predicted_price": 210000.0 }

# 💡 Future Enhancements

  ✔️ Add more features for better accuracy
  
  ✔️ Deploy to cloud (AWS, Heroku, or Render)
  
  ✔️ Improve UI with React or Vue.js
  
  ✔️ Implement user authentication

# 🤝 Contributing

  Feel free to fork this repository and contribute! 🚀

# 📜 License

  This project is licensed under the MIT License.

 ⭐ If you found this project helpful, don’t forget to give it a star! ⭐
 # Author
   Sujit Dinkar

