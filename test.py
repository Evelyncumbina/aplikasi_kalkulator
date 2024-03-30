import streamlit as st 


st.header('Aplikasi Penjumlahan Bilangan Numerik', divider='rainbow')

angka_pertama = st.number_input('Masukkan angka pertama')
st.write('The first number 15', angka_pertama)

angka_kedua = st.number_input('Masukkan angka kedua')
st.write('The second number 5', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write("Angka pertama (angka_pertama) * Angka kedua (angka_kedua) = (operasi_matematika)")
