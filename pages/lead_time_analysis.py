import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.header("Lead Times by Channel")

    # Memuat data
    data = pd.read_csv('Data Study Case BI - Study Case 1.csv')

    # Konversi kolom tanggal ke datetime
    data['first_contact'] = pd.to_datetime(data['first_contact'], format='%m/%d/%Y')
    data['checkout_date'] = pd.to_datetime(data['checkout_date'], format='%m/%d/%Y')
    data['paid_date'] = pd.to_datetime(data['paid_date'], format='%m/%d/%Y')

    # Hitung lead time
    data['lead_time'] = (data['paid_date'] - data['first_contact']).dt.days

    # Visualisasi lead time berdasarkan channel
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='channel', y='lead_time', data=data)
    plt.title('Lead Times by Channel')
    plt.xlabel('Channel')
    plt.ylabel('Lead Time (days)')
    st.pyplot(plt)
