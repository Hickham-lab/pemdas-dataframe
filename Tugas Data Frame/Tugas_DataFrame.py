import pandas as pd

#Nomor 1
df = pd.read_excel('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.xlsx', sheet_name='data')
df = df.fillna(0)
print('----Dataframe Awal----')
print(df)

#Nomor 2
hasil_thn_2019_2021 = {}
for i, row in df.iterrows():
   tahun = row['tahun']
   if 2019 <= tahun <= 2021:
      if tahun not in hasil_thn_2019_2021:
         hasil_thn_2019_2021[tahun] = 0
      hasil_thn_2019_2021[tahun] += row['jumlah_produksi_sampah']
jumlah_tahun_2019_2021 = pd.DataFrame(list(hasil_thn_2019_2021.items()), columns=['Tahun', 'Total'])
print('\n----Jumlah Sampah Berdasarkan Tahun 2019-2021----')
print(jumlah_tahun_2019_2021)

#Nomor 3
hasil_thn = {}
for i, row in df.iterrows():
   tahun = row['tahun']
   if tahun not in hasil_thn:
      hasil_thn[tahun] = 0
   hasil_thn[tahun] += row['jumlah_produksi_sampah']
jumlah_per_tahun = pd.DataFrame(list(hasil_thn.items()), columns=['Tahun', 'Total'])
print('\n----Jumlah Sampah Berdasarkan Tahun----')
print(jumlah_per_tahun)

#Nomor 4
hasil_kota = {}
for i, row in df.iterrows():
    kota = row['nama_kabupaten_kota']
    tahun = row['tahun']
    kahun = (kota, tahun)
    if kahun not in hasil_kota:
        hasil_kota[kahun] = 0
    hasil_kota[kahun] += row['jumlah_produksi_sampah']
dt_list = [{'Kota': k[0], 'Tahun': k[1], 'Total': v} for k, v in hasil_kota.items()]
jumlah_per_kota = pd.DataFrame(dt_list)
print('\n----Jumlah Sampah Berdasarkan Kota/Kabupaten dan Tahun----')
print(jumlah_per_kota)

jumlah_tahun_2019_2021.to_csv('Jumlah Sampah Berdasarkan Tahun 2019-2021.csv', index=False)
jumlah_tahun_2019_2021.to_excel('Jumlah Sampah Berdasarkan Tahun 2019-2021.xlsx', index=False)

jumlah_per_tahun.to_csv('Jumlah Sampah Berdasarkan Tahun.csv', index=False)
jumlah_per_tahun.to_excel('Jumlah Sampah Berdasarkan Tahun.xlsx', index=False)

jumlah_per_kota.to_csv('Jumlah Per Kota.csv', index=False)
jumlah_per_kota.to_excel('Jumlah Per Kota.xlsx', index=False)