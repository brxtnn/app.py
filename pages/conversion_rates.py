import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show():
    st.header("Conversion Rates by Channel")

    # Memuat data
    data = pd.read_csv('Data Study Case BI - Study Case 1.csv')

    # Hitung tingkat konversi
    conversion_rates = data.groupby('channel').size() / len(data) * 100

    # Visualisasi tingkat konversi
    plt.figure(figsize=(12, 6))
    conversion_rates.plot(kind='bar')
    plt.title('Conversion Rates by Channel')
    plt.xlabel('Channel')
    plt.ylabel('Conversion Rate (%)')
    st.pyplot(plt)
