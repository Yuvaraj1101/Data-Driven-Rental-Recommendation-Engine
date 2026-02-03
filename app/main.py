import sys
import os
import streamlit as st
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from src.scoring import calculate_scores

st.title("AI Rental Recommendation System")

bhk = st.selectbox("Select BHK Type", ["1bhk", "2bhk", "3bhk"])
budget = st.number_input("Monthly Budget", min_value=5000, max_value=200000, value=30000)
office_lat = st.number_input("Office Latitude")
office_lon = st.number_input("Office Longitude")

if st.button("Recommend"):
    results = calculate_scores(bhk, budget, office_lat, office_lon)
    st.dataframe(results)
