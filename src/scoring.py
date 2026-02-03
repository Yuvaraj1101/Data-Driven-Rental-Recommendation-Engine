import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "master_data.csv")

df = pd.read_csv(DATA_PATH)

def calculate_scores(bhk, budget, office_lat, office_lon):

    # Map selected BHK to correct column
    rent_column = {
        "1bhk": "avg_rent_1bhk",
        "2bhk": "avg_rent_2bhk",
        "3bhk": "avg_rent_3bhk"
    }[bhk]

    # Filter based on budget
    filtered = df[df[rent_column] <= budget]

    return filtered
