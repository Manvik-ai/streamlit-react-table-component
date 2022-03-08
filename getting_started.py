import streamlit as st
import pandas as pd
from react_table_component import react_table

@st.cache
def load_example_dataset():
    df0 = pd.read_json("https://raw.githubusercontent.com/vega/vega-datasets/next/data/cars.json")
    # Return first ten rows of the dataset
    return df0.head(10)

df = load_example_dataset()
react_table(df)
