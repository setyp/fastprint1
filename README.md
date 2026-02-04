# fastprint1
Test Programmer - Hendro Prasetyo

Instalasi & Setup Project
1. Clone Repository
git clone https://github.com/USERNAME/fastprint1.git
cd fastprint1

2. Aktifkan Virtual Environment
Windows (PowerShell):
python -m venv venv
venv\Scripts\activate
Linux / macOS:
python3 -m venv venv
source venv/bin/activate

3. Install Dependency
pip install -r requirements.txt
Jika belum ada:
pip install django djangorestframework requests

4. Konfigurasi Database
disini saya menggunakan MySQL, sesuaikan di settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastprint_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. Migrasi Database
python manage.py makemigrations
python manage.py migrate

6. Import Data Produk dari API
python manage.py import_produk
Command ini akan:
Mengambil data dari API FastPrint
Menyimpan Produk, Kategori, dan Status ke database

7. Jalankan Server
python manage.py runserver
Buka di browser:
http://127.0.0.1:8000/produk/

project ini dibuat sudah dilengkapi form validasi, peringatan warning saat menghapus data, dan serialize walau tidakditerapkan di list namun api sudah dibuat dan dapat digunakan