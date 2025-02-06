import streamlit as st

# Fungsi untuk menghitung jarak tempuh per liter
def hitung_jarak_per_liter(km_awal, km_akhir, liter):
    jarak_tempuh = km_akhir - km_awal
    jarak_per_liter = jarak_tempuh / liter
    return jarak_per_liter

# Judul aplikasi
st.title("Jarak Tempuh Kendaraan")

# Menambahkan logo di bagian atas dan memastikan logo berada di tengah
logo_path = 'aranademi.png'  # Ganti dengan path logo yang Anda miliki
st.image(logo_path, use_container_width=True, output_format='PNG')

# Styling agar logo di atas berada di tengah
st.markdown("""
    <style>
        .css-18e3th9 {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Input data
km_awal = st.number_input("Masukkan KM saat isi bahan bakar pertama:", min_value=0)
km_akhir = st.number_input("Masukkan KM saat isi bahan bakar kedua:", min_value=0)
liter = st.number_input("Masukkan jumlah liter bahan bakar yang digunakan:", min_value=0.0)

# Proses perhitungan
if km_awal and km_akhir and liter > 0:
    jarak_per_liter = hitung_jarak_per_liter(km_awal, km_akhir, liter)
    
    # Menampilkan hasil
    st.write(f"Jarak tempuh kendaraan per liter adalah {jarak_per_liter:.2f} km/liter.")
else:
    st.write("Masukkan semua nilai dengan benar.")
