import os
from typing import List, Union
from dataclasses import dataclass, asdict
import streamlit.components.v1 as components
import pandas as pd
import json

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "react_table",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("react_table", path=build_dir)


# @dataclass
# class Column:
#     """
#     Attributes
#     ----------
#     name: str
#         The name of the thing we're saying hello to. The component will display
#     df: pandas.DataFrame
#         The dataframe to display
#     columns: 
#         The format to display the columsn
#     key: str or None
#         An optional key that uniquely identifies this component. If this is
#     """

#     header: str
#     accessor: str
#     columns: 'Columns'

#     def to_js_column(self):
#         def rename_field(f):
#             return (f if f not in self.fields_to_rename 
#                 else self.fields_to_rename[f])
#         def transform_field_value(f, v):
            
#         return {
#             rename_field(x): 
#         }

# @dataclass
# class Columns:
#     list_: List[Union[Column, 'Columns']]
    
#     def __init__(self):
#         self.list_ = []

#     @staticmethod
#     def item_convert_to_js(item):
#         m = {
#             Column: lambda x: x.to_js_column(),
#             Columns: lambda x: x.to_js_columns()
#         }
#         return m.get(type(item))(item)

#     def add_column(self, header, columns):
#         c = Column(header=header, columns=columns)
#         self.list_.append(c)
#         return self

#     def to_js_columns(self):
#         return map(Columns.item_convert_to_js, self.list_)
# 
# def make_columns_():
#     return Columns().add_column(
#         header='Name', 
#         columns=Columns().add_column(
#             header='First Name',
#             accessor='firstName'
#         ).add_column(
#             header='Last Name',
#             accessor='lastName'
#         )
#     ).add_column(
#         header='Info',
#         columns=Columns().add_column(
#             header='Age',
#             accessor='age'
#         ).add_column(
#             header='Visits',
#             accessor='visits'
#         ).add_column(
#             header='Status',
#             accessor='status'
#         ).add_column(
#             header='Profile Progress',
#             accessor='progress'
#         )
#     )


def make_columns_from_df(df):
    x = [
        {
          "Header": "%s" % name,
          "accessor": "%s" % name
        } for name in list(df.columns)
    ]
    return x 


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.
def react_table(df, columns=None, key=None):
    """Create a new instance of "react_table".

    Parameters
    ----------
    df: pandas.DataFrame
        The dataframe to display
    columns: 
        The format to display the columns
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    int
        The number of times the component's "Click Me" button has been clicked.
        (This is the value passed to `Streamlit.setComponentValue` on the
        frontend.)

    """
    data = df.to_dict('records')

    if columns is None:
        columns = make_columns_from_df(df)
    
    print(data)
    # Call through to our private component function. Arguments we pass here
    # will be sent to the frontend, where they'll be available in an "args"
    # dictionary.
    #
    # "default" is a special argument that specifies the initial return
    # value of the component before the user has interacted with it.
    component_value = _component_func(
        data=data, columns=columns, key=key, default=0)

    # We could modify the value returned from the component if we wanted.
    # There's no need to do this in our simple example - but it's an option.
    return component_value
