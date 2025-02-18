import streamlit as st
import pandas as pd
from itertools import combinations

def generate_substrings(sequence):
    substrings = []
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence) + 1):
            substrings.append(sequence[i:j])
    return substrings

def calculate_mass(substrings, mass_table, terminal):
    mass_dict = {}
    for substring in substrings:
        mass = sum(mass_table.get(char, 0) for char in substring) + terminal
        mass_dict[substring] = mass
    return mass_dict

st.title("Mass Calculator for Sequence Substrings")

sequence = st.text_input("Enter the sequence:")
terminal = st.number_input("Enter the terminal value:", value=0, step=1)
uploaded_file = st.file_uploader("Upload Mass Table (CSV with 'char' and 'value' columns)", type=["csv"])

if uploaded_file is not None:
    mass_df = pd.read_csv(uploaded_file)
    if "char" in mass_df.columns and "value" in mass_df.columns:
        mass_table = dict(zip(mass_df["char"], mass_df["value"]))
        if st.button("Submit"):
            substrings = generate_substrings(sequence)
            mass_dict = calculate_mass(substrings, mass_table, terminal)
            result_df = pd.DataFrame(mass_dict.items(), columns=["Substring", "Mass"])
            st.write(result_df)
    else:
        st.error("CSV must contain 'char' and 'value' columns.")
