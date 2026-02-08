import streamlit as st
import pickle
import numpy as np

# Load pickle model
with open("SVM.pickle", "rb") as file:
    model = pickle.load(file)

st.title("🌸 Iris Flower Type Prediction")
st.write("Predict the Iris species using flower measurements")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", 4.0, 8.0)
sepal_width  = st.number_input("Sepal Width (cm)", 2.0, 4.5)
petal_length = st.number_input("Petal Length (cm)", 1.0, 7.0)
petal_width  = st.number_input("Petal Width (cm)", 0.1, 2.5)

# Prediction button
if st.button("Predict"):
    input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(input_data)

    pred_value = prediction[0]

    # Handle both int and string outputs safely
    if isinstance(pred_value, (int, np.integer)):
        flower = flower_names[pred_value]
    else:
        flower = pred_value  # already a label

    st.success(f"🌸 Predicted Iris Flower: **{flower}**")

