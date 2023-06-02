import tkinter as tk
import random

def pilihan_komputer():
    choices = ["Batu", "Gunting", "Kertas"]
    return random.choice(choices)

def permainan(pilihan):
    pilihan_kom = pilihan_komputer()
    hasil = ''
    
    if pilihan == pilihan_kom:
        hasil = "Seri!"
    elif (pilihan == "Batu" and pilihan_kom == "Gunting") or (pilihan == "Gunting" and pilihan_kom == "Kertas") or (pilihan == "Kertas" and pilihan_kom == "Batu"):
        hasil = "Anda Menang!"
    else:
        hasil = "Anda Kalah!"
        
    lbl_hasil.config(text="Komputer memilih: " + pilihan_kom + "\nHasil: " + hasil)
    

# Membuat jendela utama
window = tk.Tk()
window.title("Game Batu Gunting Kertas")
window.geometry("300x200")

# Membuat label
lbl_instruksi = tk.Label(window, text="Pilih salah satu: ")
lbl_instruksi.pack()

# Membuat tombol
btn_batu = tk.Button(window, text="Batu", command=lambda: permainan("Batu"))
btn_batu.pack()

btn_gunting = tk.Button(window, text="Gunting", command=lambda: permainan("Gunting"))
btn_gunting.pack()

btn_kertas = tk.Button(window, text="Kertas", command=lambda: permainan("Kertas"))
btn_kertas.pack()

# Membuat label untuk menampilkan hasil
lbl_hasil = tk.Label(window, text="")
lbl_hasil.pack()

# Memulai aplikasi
window.mainloop()
