from abc import ABC, abstractmethod
import os
os.system('cls')

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = 2023 - tahun_daftar
        self.saldo = saldo
        
    def lihat_saldo(self):
        print(f"Saldo {self.nama} adalah {self.saldo}")
    
    @abstractmethod
    def transfer_saldo(self, transfer_saldo):
        pass
    
    @abstractmethod
    def interest(self, saldo):
        pass
    
class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self, transfer):
        if self.tahun_daftar >= 3 and transfer > 1000000:
            biaya_admin = 0
        elif self.tahun_daftar < 3 and transfer > 1000000:
            biaya_admin = 2000
        else:
            biaya_admin = 0
        print(f"{self.nama} mentransfer sejumlah {transfer} dengan biaya administrasi Rp{biaya_admin}")
            
    def interest(self, saldo):
        if self.tahun_daftar >= 3 and saldo >= 1000000000:
            bunga = 0.1
        elif self.tahun_daftar < 3 and saldo >= 1000000000:
            bunga = 0.2
        else:
            bunga = 0.3
        print(f"{self.nama} memiliki tabungan dengan bunga {bunga} per bulan")
        
            
class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
    
    def transfer_saldo(self, transfer):
        if self.tahun_daftar >= 3 and transfer > 1000000:
            biaya_admin = 2000
        elif self.tahun_daftar < 3 and transfer > 1000000:
            biaya_admin = 5000
        else:
            biaya_admin = 0
        print(f"{self.nama} mentransfer sejumlah {transfer} dengan biaya administrasi Rp{biaya_admin}")
            
    def interest(self, saldo):
        if self.tahun_daftar >= 3 and saldo >= 10000000:
            bunga = 0.1
        elif self.tahun_daftar < 3 and saldo >= 10000000:
            bunga = 0.2
        else:
            bunga = 0.3
        print(f"{self.nama} memiliki tabungan dengan bunga {bunga} per bulan")

Akun1 = AkunGold("Syamsu Henry", 2019, 10000000)
Akun1.lihat_saldo()
Akun1.transfer_saldo(200000)
Akun1.interest(10000000)
print("")
Akun2 = AkunSilver("Jaja Miharja", 2017, 10000000)
Akun2.lihat_saldo()
Akun2.transfer_saldo(200000)
Akun2.interest(10000000)