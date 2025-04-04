import streamlit as st
import pickle as pk
import pandas as pd

st.title('Housing Price Prediction')

model = pk.load(open('housingprice.pickle', 'rb'))

st.header("Enter Property Details")
square_feet = st.number_input("Square Feet", min_value=50.0, max_value=500.0, value=200.0)
num_bedrooms = st.number_input("Number of Bedrooms", 1, 10, 3)
num_bathrooms = st.number_input("Number of Bathrooms", 1, 5, 2)
num_floors = st.number_input("Number of Floors", 1, 4, 2)
year_built = st.number_input("Year Built", 1900, 2024, 2000)
has_garden = st.checkbox("Has Garden")
has_pool = st.checkbox("Has Pool")
garage_size = st.number_input("Garage Size", 0, 100, 20)
location_score = st.slider("Location Score (1-10)", 1.0, 10.0, 5.0)

input_data = pd.DataFrame([[square_feet, num_bedrooms, num_bathrooms, num_floors, 
                          year_built, int(has_garden), int(has_pool), garage_size, location_score]], 
                          columns=['Square_Feet', 'Num_Bedrooms', 'Num_Bathrooms', 'Num_Floors',
                                  'Year_Built', 'Has_Garden', 'Has_Pool', 'Garage_Size', 'Location_Score'])

if st.button("Predict Price"):
    predicted_price = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ${predicted_price:,.2f}")