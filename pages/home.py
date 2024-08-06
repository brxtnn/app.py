import streamlit as st

def show():
    st.header("User Characteristics Analysis & Recomendation")
    st.markdown("""
    Dashboard ini memberikan analisis mendalam tentang pola pembelian pengguna, distribusi pelanggan berdasarkan lokasi, dan lead time dari kontak pertama hingga pembayaran.
    
    **Navigasi:**
    - **Home:** Halaman beranda ini memberikan penjelasan umum mengenai dashboard dan tujuannya.
    - **Lead Times by Channel:** Analisis lead time yang mendalam berdasarkan channel yang digunakan, termasuk waktu rata-rata dari kontak pertama hingga pembayaran di setiap channel.
    - **Customer Distribution by City and Occupation:** Visualisasi dan analisis distribusi pelanggan berdasarkan kota dan jenis pekerjaan, membantu memahami sebaran geografis dan profesional pengguna.
    - **Age Distribution by Channel:** Analisis distribusi usia pengguna berdasarkan channel yang mereka pilih, memberikan wawasan tentang demografi pengguna di berbagai channel.
    - **Conversion Rates by Channel:** Metrik tingkat konversi untuk setiap channel, membantu dalam mengevaluasi efektivitas berbagai channel dalam menghasilkan penjualan.
    - **Deep Down per Type of User:** Analisis mendalam berdasarkan tipe pengguna seperti fresh graduates, students, job seekers, dan workers. Bagian ini mengeksplorasi:
      - **Total Users per Type:** Jumlah total pengguna untuk setiap tipe pekerjaan.
      - **Average Checkout to Paid Time:** Rata-rata waktu dari checkout hingga pembayaran untuk setiap tipe pengguna.
      - **Average First Contact to Checkout Time:** Rata-rata waktu dari kontak pertama hingga checkout.
      - **Channel Distribution:** Preferensi channel berdasarkan tipe pengguna.
      - **Local Distribution:** Sebaran lokasi pengguna berdasarkan tipe pekerjaan.
      - **Histograms of Lead Times:** Distribusi periode hari antara kontak pertama dan checkout, serta antara checkout dan pembayaran untuk masing-masing tipe pengguna.
    """)
