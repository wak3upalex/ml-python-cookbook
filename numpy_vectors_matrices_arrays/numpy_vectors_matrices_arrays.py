# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Create a vector

# %% [markdown]
# With the help of NumPy create an array:
#
# Load library

# %%
import numpy as np

# %% [markdown]
# Create a row-array

# %%
vector_row = np.array([1, 2, 3])

# %% [markdown]
# Create a column-array

# %%
vector_column = np.array([[1],
                          [2],
                          [3]])

# %% [markdown]
# ## Description
# The main data structure in numpy is a multidimensional array. Definition of an array is equal to a one-dimensional array. To get vector we just create a one-dimensional array.
# These arrays same as vectors can be placed horizontally (rows) and vertically(columns)

# %%
print(vector_row)

# %%
print(vector_column)
