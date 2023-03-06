usn = 'informatika'
pwd = '12345678'
coba = 1

while coba <= 3:
    
    username = input("masukan username :")
    password = input("masukan password :") 
    coba += 1

    if username == usn and password == pwd:
        print ("berhasil login!")
        break
    else:
        print("username atau password salah coba lagi")

print("login gagal!")