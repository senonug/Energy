# Dashboard Target Operasi AMR - P2TL

Aplikasi ini digunakan untuk melakukan screening data pelanggan AMR berdasarkan parameter teknis seperti arus, tegangan, dan daya aktif.

## Fitur
- Login pegawai
- Upload file Excel harian (INSTANT)
- Penyimpanan histori data
- Filter threshold teknikal
- Deteksi otomatis 15+ indikator anomali
- Visualisasi interaktif
- Ekspor hasil ke Excel

## Cara Menjalankan
1. Pastikan Anda memiliki Python 3.8+
2. Install dependency:
```bash
pip install -r requirements.txt
```
3. Jalankan:
```bash
streamlit run dashboard_amr.py
```

## Struktur
- `dashboard_amr.py`: kode utama
- `requirements.txt`: dependensi Python
- `README.md`: dokumentasi ini

## Streamlit Cloud
Untuk deploy ke Streamlit Cloud:
1. Push semua file ke GitHub (dashboard_amr.py, requirements.txt, README.md)
2. Login ke https://streamlit.io/cloud
3. Hubungkan ke repo dan jalankan `dashboard_amr.py`

