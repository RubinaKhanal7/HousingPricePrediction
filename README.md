# Housing Price Prediction App

A simple Streamlit application that predicts house prices based on property features.

## Overview

This application uses a Linear Regression model to predict housing prices based on various property characteristics such as square footage, number of bedrooms, location score, and more. The model was trained on a dataset of 500 houses and achieves approximately 97% accuracy.

## Features

- Predict house prices based on multiple property features
- Simple and intuitive user interface
- Real-time predictions

## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install streamlit pandas scikit-learn
```

## Usage

1. Ensure you have the model file `housingprice.pickle` in the same directory as the app
2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Enter the property details in the web interface:
   - Square Feet
   - Number of Bedrooms
   - Number of Bathrooms
   - Number of Floors
   - Year Built
   - Garden availability
   - Pool availability
   - Garage Size
   - Location Score

4. Click "Predict Price" to get the estimated house price

## Files

- `app.py`: The Streamlit application
- `housingprice.pickle`: The trained Linear Regression model
- `Housing Prices Regression.ipynb`: Jupyter notebook with the model development process

## Model Details

The model was built using Linear Regression with the following features:
- Square_Feet
- Num_Bedrooms
- Num_Bathrooms
- Num_Floors
- Year_Built
- Has_Garden
- Has_Pool
- Garage_Size
- Location_Score
