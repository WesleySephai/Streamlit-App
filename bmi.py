import streamlit as st
from PIL import Image

#Display tittle of the page
st.title('BMI Calculator')

#Display the image
img = Image.open("C:/Users/Thuto/Desktop/Digital Regenesys Dashboard/Web Development AI/Code/bmi_image.png")
st.image(img,caption="BMI image",use_column_width=True)

#input fields
name = st.text_input('Enter your name: ')
height = st.number_input('Enter your height(in meters)',format="%.2f")
weight = st.number_input('Enter your weight(in kgs)',format="%.2f")

#Button and logic
if st.button('Calculate BMI'):
    if height > 0:
        bmi = weight/(height ** 2)

        #Categorize BMI
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        st.success(f"{name}, your BMI is {bmi:.2f} which is considered '{category}'.")
