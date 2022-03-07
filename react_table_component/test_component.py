import streamlit as st
import pandas as pd
from react_table_component import react_table_component
import names
import random


def _run_component(df, columns):
    st.subheader("Component with variable args")
    # We use the special "key" argument to assign a fixed identity to this
    # component instance. By default, when a component's arguments change,
    # it is considered a new instance and will be re-mounted on the frontend
    # and lose its current state. In this case, we want to vary the component's
    # "name" argument without having it get recreated.
    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = react_table_component(
        name_input, df=df, columns=columns, key="foo")
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
    _run_component(df, columns)

run_component_1()