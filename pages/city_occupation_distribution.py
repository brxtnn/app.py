import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.header("Customer Distribution by City and Occupation")

    # Memuat data
    data = pd.read_csv('Data Study Case BI - Study Case 1.csv')

    # Distribusi pelanggan berdasarkan kota dan pekerjaan
    city_occupation_distribution = pd.crosstab(data['city'], data['occupation'])

    # Visualisasi heatmap distribusi pelanggan
    plt.figure(figsize=(12, 8))
    sns.heatmap(city_occupation_distribution, annot=True, fmt='d', cmap='Blues')
    plt.title('Customer Distribution by City and Occupation')
    plt.xlabel('Occupation')
    plt.ylabel('City')
    st.pyplot(plt)
