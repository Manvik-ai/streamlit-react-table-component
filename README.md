# README

## Development Setup

Following the setup recommended by the `streamlit-component-template` project,

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
