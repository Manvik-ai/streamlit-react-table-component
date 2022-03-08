import streamlit as st
import pandas as pd
from react_table_component import react_table
import names
import random


def _run_component(df, columns, key=None):
    st.subheader("Component with variable args")
    num_clicks = react_table(df=df, columns=columns, key=key)
    st.markdown("You've clicked %s times!" % int(num_clicks))


def make_columns_easy():
    return [
    {
      'Header': 'Name',
      'columns': [
        {
          'Header': 'First Name',
          'accessor': 'firstName',
        },
        {
          'Header': 'Last Name',
          'accessor': 'lastName',
        },
      ],
    },
    {
      'Header': 'Info',
      'columns': [
        {
          'Header': 'Age',
          'accessor': 'age',
        },
        {
          'Header': 'Visits',
          'accessor': 'visits',
        },
        {
          'Header': 'Status',
          'accessor': 'status',
        },
        {
          'Header': 'Profile Progress',
          'accessor': 'progress',
        },
      ],
    },
  ]


def make_df(n):
    def random_status():
        chance = random.random()
        if chance > 0.66:
          return 'relationship'
        elif chance > 0.33:
          return 'complicated'
        else:
          return 'single'

    def new_person():
        d = {}
        d['firstName'] = names.get_first_name()
        d['lastName'] = names.get_last_name()
        d['age'] = random.randint(0, 30)
        d['visits'] = random.randint(0, 100)
        d['progress'] = random.randint(0, 100)
        d['status'] = random_status()
        return d
        
    return pd.DataFrame([new_person() for i in range(n)]) 


def run_component_1():
    columns=make_columns_easy()
    df = make_df(20)
    _run_component(df, columns, key="component_1")


# columns = [{'Header': '_comment', 'accessor': '_comment'}, {'Header': 'year', 'accessor': 'year'}, {'Header': 'fertility', 'accessor': 'fertility'}, {'Header': 'life_expect', 'accessor': 'life_expect'}, {'Header': 'n_fertility', 'accessor': 'n_fertility'}, {'Header': 'n_life_expect', 'accessor': 'n_life_expect'}, {'Header': 'country', 'accessor': 'country'}, {'Header': 'p_fertility', 'accessor': 'p_fertility'}, {'Header': 'p_life_expect', 'accessor': 'p_life_expect'}]

def run_component_0():
    df = pd.read_json("https://raw.githubusercontent.com/vega/vega-datasets/next/data/countries.json")
    react_table(df.head(10), key="countries")


run_component_0()