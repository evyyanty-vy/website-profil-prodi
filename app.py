from flask import Flask, render_template

app = Flask(__name__)


#DATA STATIS (Dummy Data) 

info_prodi = {
    "nama": "Program Studi Ilmu Komputer",
    "fakultas": "Fakultas Sains Teknologi dan Ilmu kesehatan",
    "universitas": "Universitas Bina Bangsa Getsempena",
    "akreditasi": "B",
    "tahun_berdiri": 2016,
    "deskripsi": (
        "Program Studi Ilmu Komputer merupakan program studi yang berfokus pada "
        "pengembangan ilmu pengetahuan di bidang komputasi, algoritma, kecerdasan buatan, "
        "rekayasa perangkat lunak, dan sistem informasi. Program studi ini mencetak "
        "lulusan yang kompeten, inovatif, dan siap bersaing di era digital."
    ),
    "visi": (
        "Menjadi program studi unggulan di tingkat nasional dan internasional yang "
        "menghasilkan sumber daya manusia berkualitas di bidang ilmu komputer "
        "berbasis riset dan inovasi teknologi pada tahun 2030."
    ),
    "misi": [
        "Menyelenggarakan pendidikan ilmu komputer yang berkualitas dan relevan dengan kebutuhan industri.",
        "Mengembangkan penelitian inovatif di bidang ilmu komputer yang bermanfaat bagi masyarakat.",
        "Menjalin kerja sama dengan industri, pemerintah, dan institusi pendidikan dalam dan luar negeri.",
        "Membentuk lulusan yang berkarakter, profesional, dan berintegritas tinggi.",
    ],
}

daftar_dosen = [
    {
        "nama": "Ully Muzakir, M.T.",
        "nidn": "0127027902",
        "bidang": "Aljabar vektor dan Matriks",
        "email": "Ulyy.Muzakir@gmail.com",
        "foto": "https://lh3.googleusercontent.com/d/103hMOrQMIJgp6JdbyPSfdMl0J7IGEYM_",
    },
    {
        "nama": "Oktalia Triananda Lovita,S.ST, MT.",
        "nidn": "9990544271",
        "bidang": "Sistem Basis Data",
        "email": "OktaliaLovita@gmail.com",
        "foto": "https://lh3.googleusercontent.com/d/1vpyNyEXfL3dXi6aIof7TqPKJ-KGLzDLa",
    },
    {
        "nama": "Nazuarsyah, ST, MT.",
        "nidn": "1316048101",
        "bidang": "Pemograman Berorientasi Objek",
        "email": "Nazuarsyah12@gmail.com",
        "foto": "https://lh3.googleusercontent.com/d/1z-8RbX4CT0mwmFs34aLDVmsBDJifieoH",
    },
    
]

daftar_mahasiswa = [
    {"nim": "24210006", "nama": "EPIYANTI",    "angkatan": 2024, "status": "Aktif"},
    {"nim": "24210028", "nama": "Hafizah Azalia",   "angkatan": 2024, "status": "Aktif"},
    {"nim": "24210029", "nama": "Wesy Puspita",      "angkatan": 2024, "status": "Cuti"},
    {"nim": "24210046", "nama": "Revatul Maghfirah",  "angkatan": 2024, "status": "Aktif"},
    {"nim": "24210050", "nama": "Dewi Ratna Sari",    "angkatan": 2024, "status": "Aktif"},
    {"nim": "21210041", "nama": "Fahmi Al Ryansyah", "angkatan": 2021, "status": "Lulus"},
    {"nim": "22210055", "nama": "Prayoga Bima Gemilang",     "angkatan": 2022, "status": "Lulus"},
    {"nim": "24210049", "nama": "Cut Mutia",  "angkatan": 2024, "status": "Cuti"},
    {"nim": "221402009", "nama": "Intan Permata Sari",      "angkatan": 2022, "status": "Lulus"},
    {"nim": "231402010", "nama": "Yusuf Al-Farisi Panjaitan","angkatan": 2023, "status": "Aktif"},
    {"nim": "231402011", "nama": "Tiara Ananda Batubara",   "angkatan": 2023, "status": "Aktif"},
    {"nim": "231402012", "nama": "Dicky Firmansyah Pasaribu","angkatan": 2023, "status": "drop out"},
]



# ROUTING (Pengaturan Halaman)


@app.route("/")
def home():
    return render_template("home.html", prodi=info_prodi)


@app.route("/profil")
def profil():
    return render_template("profil.html", prodi=info_prodi)


@app.route("/dosen")
def dosen():
    return render_template("dosen.html", dosen_list=daftar_dosen, prodi=info_prodi)


@app.route("/mahasiswa")
def mahasiswa():
    return render_template("mahasiswa.html", mahasiswa_list=daftar_mahasiswa, prodi=info_prodi)



# JALANKAN APLIKASI


if __name__ == "__main__":
    app.run(debug=True)
