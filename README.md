# README

## Development Setup

Following the setup recommended by the `streamlit-component-template` project,

* Development Setup for Python using virtualenv:

  ```sh
  venv .venv
  source .venv/bin/activate
  pip install -e .
  streamlit run react_table_component/__init__.py
  ```

* Development Setup for the Javascript frontend:

  Open a new terminal and run these commands:
  
  ```sh
  yarn run start
  ```
  
  for the non-Release version,
  
  or
  
  ```sh
  yarn run build
  ```
  
  for the release version.
