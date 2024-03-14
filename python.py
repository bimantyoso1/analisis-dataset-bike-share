import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
day_df = pd.read_csv('day.csv')

# Konversi kolom tanggal ke tipe datetime
date_columns = ['dteday']
for column in date_columns:
    day_df[column] = pd.to_datetime(day_df[column])

# Sidebar untuk memilih rentang waktu
st.sidebar.header('Pilih Rentang Waktu')
start_date = st.sidebar.date_input("Tanggal Awal", min_value=day_df['dteday'].min(), max_value=day_df['dteday'].max(), value=day_df['dteday'].min())
end_date = st.sidebar.date_input("Tanggal Akhir", min_value=day_df['dteday'].min(), max_value=day_df['dteday'].max(), value=day_df['dteday'].max())

# Filter data berdasarkan rentang waktu
filtered_day_df = day_df[(day_df['dteday'] >= str(start_date)) & (day_df['dteday'] <= str(end_date))]

# Visualisasi data
st.header('Analisis Data Sewa Sepeda')
st.write('Nama: Bimantyoso Hamdikatama')
st.write('Email : bimantyosohamdikatam@gmail.com')

# Histogram jumlah sewa sepeda harian berdasarkan kondisi cuaca
plt.figure(figsize=(10, 6))
sns.histplot(data=filtered_day_df, x='cnt', hue='weathersit', bins=20, multiple='stack', kde=True)
plt.xlabel('Jumlah Sewa Sepeda')
plt.ylabel('Frekuensi')
plt.title('Distribusi Jumlah Sewa Sepeda Harian Berdasarkan Kondisi Cuaca')
plt.legend(title='Kondisi Cuaca', loc='upper right')
st.pyplot(plt.gcf())  # Menggunakan plt.gcf() untuk mendapatkan figur saat ini

# Diagram pie persentase total sewa sepeda untuk setiap kondisi cuaca
weather_counts = filtered_day_df.groupby('weathersit')['cnt'].sum()

# Menambahkan keterangan nama untuk setiap kondisi cuaca
weather_labels = {
    1: 'Cerah',
    2: 'Kabut',
    3: 'Salju Ringan',
    4: 'Hujan Badai'
}

# Membuat diagram pie menggunakan Seaborn
plt.figure(figsize=(6, 6))
plt.pie(weather_counts, labels=[weather_labels[i] for i in weather_counts.index], autopct='%1.1f%%', startangle=140)
plt.title('Persentase Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
plt.axis('equal')
st.pyplot(plt.gcf())  # Menggunakan plt.gcf() untuk mendapatkan figur saat ini


hour_df = pd.read_csv('hour.csv')
average_rentals_per_day = filtered_day_df['cnt'].mean()
st.write(f"Rata-rata Jumlah Sewa Sepeda per Hari: {average_rentals_per_day:.2f}")

workday_rentals = filtered_day_df[filtered_day_df['holiday'] == 1]['cnt']
holiday_rentals = filtered_day_df[filtered_day_df['holiday'] == 0]['cnt']

plt.figure(figsize=(10, 6))
sns.kdeplot(workday_rentals, label='Hari Kerja', shade=True)
sns.kdeplot(holiday_rentals, label='Hari Libur', shade=True)
plt.xlabel('Jumlah Sewa Sepeda')
plt.ylabel('Kepadatan')
plt.title('Perbedaan Pola Peminjaman Sepeda antara Hari Kerja dan Hari Libur')
plt.legend()
st.pyplot(plt.gcf())  

# Diagram boxplot untuk perbandingan jumlah sewa sepeda antara hari kerja dan hari libur
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_day_df, x='holiday', y='cnt')
plt.xlabel('Hari Kerja / Hari Libur')
plt.ylabel('Jumlah Sewa Sepeda')
plt.title('Perbandingan Jumlah Sewa Sepeda antara Hari Kerja dan Hari Libur')
plt.xticks(ticks=[0, 1], labels=['Hari Kerja', 'Hari Libur'])
st.pyplot(plt.gcf()) 

st.write('License')
st.text("""
[1] Fanaee-T, Hadi, and Gama, Joao, "Event labeling combining ensemble detectors and background knowledge", Progress in Artificial Intelligence (2013): pp. 1-15, Springer Berlin Heidelberg, doi:10.1007/s13748-013-0040-3.
""")



