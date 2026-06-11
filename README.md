# Tugas 4 - Website Profil Program Studi
**Flask + Jinja2 | Bootstrap 5**

## Cara Menjalankan

### 1. Install Flask
Buka terminal / command prompt, jalankan:
```
pip install flask
```

### 2. Jalankan Aplikasi
```
python app.py
```

### 3. Buka di Browser
Pergi ke: http://127.0.0.1:5000

---

## Struktur Folder
```
tugas4/
├── app.py                  ← File utama Python (routing + data)
├── requirements.txt        ← Daftar library yang dibutuhkan
├── templates/
│   ├── base.html           ← Template induk (navbar + footer)
│   ├── home.html           ← Halaman Home
│   ├── profil.html         ← Halaman Profil Prodi
│   ├── dosen.html          ← Halaman Daftar Dosen
│   └── mahasiswa.html      ← Halaman Daftar Mahasiswa
└── static/                 ← (kosong, Bootstrap pakai CDN)
```

---

## Konsep yang Diterapkan
- Template Inheritance (`{% extends %}` dan `{% block %}`)
- Variable Rendering (`{{ variabel }}`)
- For Loop (`{% for ... in ... %}`)
- If Statement (`{% if %} {% elif %} {% else %}`)
