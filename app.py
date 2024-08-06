import streamlit as st

# Judul aplikasi
st.title("Dashboard Study Case 1")

# Navigasi halaman
st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Lead Times by Channel", "Customer Distribution by City and Occupation", "Age Distribution by Channel", "Conversion Rates by Channel", "Deep Down per Type of User"])

# Memuat halaman sesuai pilihan
if page == "Home":
    from pages import home
    home.show()
elif page == "Lead Times by Channel":
    from pages import lead_time_analysis
    lead_time_analysis.show()
elif page == "Customer Distribution by City and Occupation":
    from pages import city_occupation_distribution
    city_occupation_distribution.show()
elif page == "Age Distribution by Channel":
    from pages import age_distribution
    age_distribution.show()
elif page == "Conversion Rates by Channel":
    from pages import conversion_rates
    conversion_rates.show()
elif page == "Deep Down per Type of User":
    from pages import user_analysis
    user_analysis.show()
