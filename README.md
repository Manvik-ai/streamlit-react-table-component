# README

Display your Pandas Dataframe via Streamlit using this component. 
It is based on React-Table (https://react-table.tanstack.com/) Javascript UI library.

---

**Note**: This component is new and not yet ready for production use.

---

Tags: #pandas-dataframe, #react-table, #streamlit, #streamlit-components

## For Users

Read this section before using the component.

### Getting Started

```py
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
```

## For Developers

Read this section if you want to know how the extension works or modify the source code.

Following the setup recommended by the [`streamlit-component-template` project](https://github.com/streamlit/component-template) (do read it first),

* Development Setup for Python 3 using virtualenv:

  ```sh
  venv .venv
  source .venv/bin/activate
  pip install -e .[test]
  streamlit run react_table_component/test_component.py
  ```

* Development Setup for the Javascript frontend:

  Open a new terminal and run these commands:
  
  ```sh
  cd react_table_component/frontend
  yarn run start
  ```
  
  for the non-Release version,
  
  or
  
  ```sh
  yarn run build
  ```
  
  for the release version.
