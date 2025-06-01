# 🏡 Real Estate Price Prediction Using ML  

## Overview  
This project utilizes **Machine Learning models** to predict **Bengaluru house prices**, leveraging data preprocessing and regression techniques for accurate estimations. With **Linear Regression**, the model achieves **82% accuracy**, helping users make informed real estate decisions.  

## Features  
- **Price estimation** based on key housing attributes.  
- **Data preprocessing** using one-hot encoding for categorical features.  
- **Flask-based deployment** for real-time price predictions.  

## Technologies Used  
- **Python & Pandas** – Data handling.  
- **NumPy & Scikit-learn** – ML model development.  
- **Linear Regression & GridSearchCV** – Model tuning and optimization.  
- **Flask** – Web-based interface for predictions.  

## Installation  
```bash
git clone https://github.com/Lingesh-7/Real-Estate-Prediction-ML
cd Real-Estate-Prediction-ML
pip install -r requirements.txt
```

## Usage  
### 1. Training the Model  
```bash
python train.py --epochs 10 --batch_size 32
```

### 2. Running Price Prediction  
```bash
python predict.py --features "area=1200, bedrooms=3, location='Indiranagar'"
```

### 3. Web-Based Prediction (Flask App)  
```bash
python app.py
```
Visit `http://localhost:5000` to input property details and get price predictions.  

## Results  
The model predicts **house prices in Bengaluru** with **82% accuracy**, offering valuable insights for buyers and sellers.  

## Future Improvements  
- Improve feature selection for **higher accuracy**.  
- Integrate **LLMs for real estate insights**.  
- Expand to **multi-city housing price predictions**.
