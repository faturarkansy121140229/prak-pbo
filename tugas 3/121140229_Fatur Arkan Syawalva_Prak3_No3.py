class Mahasiswa:
    
    # atribut kelas
    jumlah_mahasiswa = 0
    nilai_ipk_minimal = 2.5
    
    def __init__(self, nama, jurusan, ipk, semester):
        # atribut instance
        self.nama = nama
        self.jurusan = jurusan
        self.semester = semester
        self.__ipk = ipk  # atribut private
    
        
        Mahasiswa.jumlah_mahasiswa += 1
    
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Semester: {self.semester}")
        print(f"IPK: {self.__ipk}")
        
        
    # fungsi public
    def perbarui_ipk(self, ipk_baru):
        if ipk_baru >= Mahasiswa.nilai_ipk_minimal:
            self.__ipk = ipk_baru
            print(f"Perbarui IPK: {ipk_baru}")
            print("IPK berhasil diperbarui.")
        else:
            print("IPK tidak valid.")
    
    # fungsi membenarkan semester
    def lupa_semester(self, semester):
        if self.semester == 2:
            self.semester = self.semester + 2
            print(f"{self.nama} lupa ternyata sudah semester {self.semester}")
            print(f"Sekarang adalah semester {self.semester}")
            print()
    
    # fungsi protected
    def _fungsi_protected(self):
        print("Data dilindungi.")
        print(f"Data akun akademik {self.nama} terlindungi")
    
    # fungsi private
    def __private_method(self):
        print("Data privasi")
        print(f"{self.nama} tinggal di jl. ulangan perumahan PU")


# membuat objek m1 dari kelas Mahasiswa
student = Mahasiswa("Fatur", "Informatika", 3.5, 2)

# memanggil fungsi tampilkan_info pada objek m1
student.info()
print()

#memperbarui semester
student.lupa_semester(4)

# mengubah nilai IPK pada objek m1
student.perbarui_ipk(4)

