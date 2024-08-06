import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.header("Deep Down per Type of User")

    # Memuat data
    try:
        data = pd.read_csv('Data Study Case BI - Study Case 1.csv')
    except FileNotFoundError:
        st.error("File tidak ditemukan. Pastikan nama file dan path sudah benar.")
        return


    # Strip whitespace from column names
    data.columns = data.columns.str.strip()

    # Verifikasi kolom yang ada
    required_columns = ['user_id', 'first_contact', 'checkout_date', 'paid_date', 'channel', 'occupation', 'city', 'age']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        st.error(f"Kolom berikut tidak ditemukan dalam dataset: {', '.join(missing_columns)}")
        return

    # Konversi kolom tanggal ke datetime
    try:
        data['first_contact'] = pd.to_datetime(data['first_contact'], format='%m/%d/%Y')
        data['checkout_date'] = pd.to_datetime(data['checkout_date'], format='%m/%d/%Y')
        data['paid_date'] = pd.to_datetime(data['paid_date'], format='%m/%d/%Y')
    except Exception as e:
        st.error(f"Kesalahan dalam konversi tanggal: {e}")
        return

    # Hitung periode hari
    data['first_to_checkout'] = (data['checkout_date'] - data['first_contact']).dt.days
    data['checkout_to_paid'] = (data['paid_date'] - data['checkout_date']).dt.days

    # Jenis pengguna yang berbeda berdasarkan kolom occupation
    occupations = data['occupation'].unique()

    for occupation in occupations:
        st.subheader(f"Type of User: {occupation.replace('_', ' ').capitalize()}")

        user_data = data[data['occupation'] == occupation]

        if user_data.empty:
            st.write(f"No data available for {occupation.replace('_', ' ').capitalize()}.")
            continue

        # Total pengguna
        total_users = len(user_data)
        st.write(f"**Total Users:** {total_users}")

        # Rata-rata waktu dari checkout ke pembayaran
        avg_checkout_to_paid = user_data['checkout_to_paid'].mean()
        st.write(f"**Average Checkout to Paid (Days):** {avg_checkout_to_paid:.2f}")

        # Rata-rata waktu dari kontak pertama ke checkout
        avg_first_to_checkout = user_data['first_to_checkout'].mean()
        st.write(f"**Average First Contact to Checkout (Days):** {avg_first_to_checkout:.2f}")

        # Distribusi channel
        st.write("**Channel Distribution:**")
        channel_distribution = user_data['channel'].value_counts(normalize=True) * 100
        st.bar_chart(channel_distribution)

        # Distribusi lokal
        st.write("**Local Distribution:**")
        local_distribution = user_data['city'].value_counts(normalize=True) * 100
        st.bar_chart(local_distribution)

        # Periode hari antara kontak pertama dan checkout
        st.write("**Days Period Between First Contact and Checkout Date:**")
        plt.figure(figsize=(12, 6))
        sns.histplot(user_data['first_to_checkout'], kde=True)
        plt.title(f'Days Period Between First Contact and Checkout Date for {occupation.replace("_", " ").capitalize()}')
        plt.xlabel('Days')
        plt.ylabel('Count')
        st.pyplot(plt)

        # Periode hari antara checkout dan pembayaran
        st.write("**Days Period Between Checkout Date and Paid Date:**")
        plt.figure(figsize=(12, 6))
        sns.histplot(user_data['checkout_to_paid'], kde=True)
        plt.title(f'Days Period Between Checkout Date and Paid Date for {occupation.replace("_", " ").capitalize()}')
        plt.xlabel('Days')
        plt.ylabel('Count')
        st.pyplot(plt)

    st.subheader("💡 Main Insights and Recommendations")

    # Menyusun Main Insights dan Recommendations
    st.write("""
    ### Main Insights
    1. **Variasi Waktu Checkout ke Pembayaran Berdasarkan Tipe Pengguna:**
       - **Workers** memiliki waktu rata-rata terpendek (8.09 hari) dari checkout hingga pembayaran, menunjukkan bahwa mereka cenderung menyelesaikan transaksi lebih cepat setelah membuat keputusan.
       - **Fresh Graduates** memiliki waktu rata-rata terpanjang (11.55 hari) untuk menyelesaikan pembayaran, mengindikasikan bahwa mereka mungkin memerlukan lebih banyak waktu untuk mempertimbangkan keputusan pembelian mereka.

    2. **Waktu Rata-Rata dari Kontak Pertama hingga Checkout:**
       - **Job Seekers** memiliki waktu rata-rata terpendek (8.04 hari) dari kontak pertama hingga checkout, menunjukkan mereka lebih cepat dalam proses pengambilan keputusan.
       - **Students** dan **Fresh Graduates** memiliki waktu rata-rata yang mirip (9.09 hari untuk Students dan 10.81 hari untuk Fresh Graduates), menunjukkan bahwa mereka memerlukan waktu yang relatif sama dalam membuat keputusan pembelian setelah kontak pertama.

    3. **Perbedaan dalam Kecepatan Proses Pembelian:**
       - **Job Seekers** menunjukkan waktu tercepat dari kontak pertama hingga checkout, tetapi memerlukan waktu yang lebih lama dari checkout hingga pembayaran dibandingkan dengan **Workers**.
       - **Workers** lebih efisien dalam menyelesaikan pembayaran, tetapi membutuhkan sedikit lebih banyak waktu untuk mencapai checkout dibandingkan dengan **Job Seekers**.
    """)

    st.write("""
    ### Recommendations
    1. **Optimalkan Proses Pembayaran untuk Fresh Graduates:**
       - **Fresh Graduates** membutuhkan waktu lebih lama untuk menyelesaikan pembayaran. Pertimbangkan untuk menyediakan insentif atau opsi pembayaran yang memudahkan mereka, seperti diskon khusus untuk pembayaran cepat atau cicilan tanpa bunga.

    2. **Tingkatkan Dukungan untuk Fresh Graduates:**
       - Karena **Fresh Graduates** memerlukan waktu lebih lama dari kontak pertama hingga checkout, berikan mereka informasi tambahan dan dukungan selama proses pembelian. Ini bisa berupa materi edukasi, panduan, atau sesi tanya jawab untuk membantu mereka merasa lebih nyaman dengan keputusan mereka.

    3. **Fasilitasi Pengalaman Pengguna untuk Job Seekers dan Workers:**
       - Untuk **Job Seekers** yang menunjukkan proses pembelian cepat, pertimbangkan untuk mempermudah proses checkout mereka dengan opsi pembayaran yang cepat dan mudah.
       - Untuk **Workers**, pastikan bahwa proses checkout dan pembayaran tidak terlalu rumit dan berikan opsi yang nyaman, seperti metode pembayaran yang dapat diakses secara luas.

    4. **Segmentasikan Penawaran Berdasarkan Tipe Pengguna:**
       - Tawarkan penawaran yang disesuaikan dengan tipe pengguna. Misalnya, tawaran khusus untuk **Job Seekers** yang mempercepat keputusan pembelian atau penawaran bagi **Fresh Graduates** yang memerlukan dorongan tambahan untuk menyelesaikan pembayaran.

    5. **Analisis Lebih Lanjut untuk Meningkatkan Konversi:**
       - Lakukan analisis lebih mendalam untuk memahami faktor-faktor yang mempengaruhi perbedaan waktu ini. Misalnya, periksa apakah ada perbedaan dalam metode pembayaran yang digunakan atau jika ada perbedaan dalam jenis produk yang dibeli oleh masing-masing tipe pengguna.
    """)

    st.write("""
    ### Summary
    Wawasan ini menunjukkan bahwa setiap tipe pengguna memiliki pola yang berbeda dalam proses pembelian mereka. Dengan menyesuaikan pendekatan pemasaran, pengalaman pengguna, dan strategi pembayaran berdasarkan waktu rata-rata yang dibutuhkan oleh masing-masing tipe pengguna, Anda dapat meningkatkan konversi dan kepuasan pelanggan secara keseluruhan.
    """)

if __name__ == "__main__":
    show()
