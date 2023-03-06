class Saya:
  def __init__(self, nama, nim, kelas_siakad, jumlah_sks):
    self.nama = nama
    self.nim = nim
    self.kelas_siakad = kelas_siakad
    self.jumlah_sks = jumlah_sks

  def hobi(self):
    print("Hobi:")
    print("Nonton anime")
    print("Rebahan")
    print("Tiduran")  
    
  def data(self):
    print("Nama: ", self.nama)
    print("NIM: ", self.nim)
    print("Kelas_siakad: ", self.kelas_siakad)
    print("Jumlah_sks: ",self.jumlah_sks)
    
orang = Saya("Fatur", "121140229", "RD", "2")
orang.data()
print("---------------")
orang.hobi()
