import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# Streamlit UI
st.title("Fetal Health Prediction")
st.write("Enter the required features to predict fetal health.")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    baseline_value = st.number_input("Baseline Fetal Heart Rate (FHR)", min_value=0.0, step=0.1)
    accelerations = st.number_input("Accelerations", min_value=0.0, step=0.0001, format="%.5f")
    fetal_movement = st.number_input("Fetal Movement", min_value=0.0, step=0.0001, format="%.5f")
    uterine_contractions = st.number_input("Uterine Contractions", min_value=0.0, step=0.0001, format="%.5f")
    light_decelerations = st.number_input("Light Decelerations", min_value=0.0, step=0.0001, format="%.5f")
    severe_decelerations = st.number_input("Severe Decelerations", min_value=0.0, step=0.0001, format="%.5f")
    prolongued_decelerations = st.number_input("Prolonged Decelerations", min_value=0.0, step=0.0001, format="%.5f")
    abnormal_short_term_variability = st.number_input("Abnormal Short-Term Variability", min_value=0.0, step=0.1)
    mean_value_of_short_term_variability = st.number_input("Mean Value of Short-Term Variability", min_value=0.0, step=0.1)
    percentage_of_time_with_abnormal_long_term_variability = st.number_input(
        "Percentage of Time with Abnormal Long-Term Variability", min_value=0.0, step=0.1)
    mean_value_of_long_term_variability = st.number_input("Mean Value of Long-Term Variability", min_value=0.0, step=0.1)

with col2:
    histogram_width = st.number_input("Histogram Width", min_value=0.0, step=0.1)
    histogram_min = st.number_input("Histogram Min", min_value=0.0, step=0.1)
    histogram_max = st.number_input("Histogram Max", min_value=0.0, step=0.1)
    histogram_number_of_peaks = st.number_input("Histogram Number of Peaks", min_value=0, step=1)
    histogram_number_of_zeroes = st.number_input("Histogram Number of Zeroes", min_value=0, step=1)
    histogram_mode = st.number_input("Histogram Mode", min_value=0.0, step=0.1)
    histogram_mean = st.number_input("Histogram Mean", min_value=0.0, step=0.1)
    histogram_median = st.number_input("Histogram Median", min_value=0.0, step=0.1)
    histogram_variance = st.number_input("Histogram Variance", min_value=0.0, step=0.1)
    histogram_tendency = st.number_input("Histogram Tendency", min_value=0, step=1)

# Predict button
if st.button("Predict Fetal Health"):
    features = np.array([[baseline_value, accelerations, fetal_movement, uterine_contractions,
                          light_decelerations, severe_decelerations, prolongued_decelerations,
                          abnormal_short_term_variability, mean_value_of_short_term_variability,
                          percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability,
                          histogram_width, histogram_min, histogram_max, histogram_number_of_peaks,
                          histogram_number_of_zeroes, histogram_mode, histogram_mean, histogram_median,
                          histogram_variance, histogram_tendency]])
    prediction = model.predict(features)[0]

    # Map prediction to category
    categories = {1: "Normal", 2: "Suspect", 3: "Pathological"}
    result = categories.get(prediction, "Unknown")

    st.success(f"Predicted Fetal Health: {result}")
