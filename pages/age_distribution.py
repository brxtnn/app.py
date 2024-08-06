import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.header("Age Distribution by Channel")

    # Memuat data
    data = pd.read_csv('Data Study Case BI - Study Case 1.csv')

    # Visualisasi distribusi usia berdasarkan channel
    plt.figure(figsize=(12, 6))
    sns.histplot(data, x='age', hue='channel', multiple='stack', kde=True)
    plt.title('Age Distribution by Channel')
    plt.xlabel('Age')
    plt.ylabel('Count')
    st.pyplot(plt)
