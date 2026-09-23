#DEADLINE SENIN 21 SEPTEMBER 2026 JAM 23.59 WIB

#Modul 1 Soal 1

lamaParkir = int(input())
if lamaParkir <= 2:
    totalBiaya = 5000
else:
    totalBiaya = 5000 + (lamaParkir - 2) * 2000
print(totalBiaya)

#Modul 1 Soal 2

username = input()
password = input()
if username == "admin" and password == "pass123":
    print("Akses Diterima")
else:
    print("Login Gagal")

#Modul 2 Soal 1
bilangan = int(input("Masukkan angka : "))
if bilangan % 2 == 0:
    print("genap")
else:
    print("ganjil")

print("Masukkan angka : ")    
bilangan = int(input())
if bilangan % 2 == 0:
    print("genap")
else:
    print("ganjil")

#Modul 2 Soal 2

N = int(input("Tinggi : "))

for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(str(j), end=' ')

    print("")


print("Tinggi : ")
n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end='', flush=True)
        print(" ", end='', flush=True)
        j = j + 1
    print(" ")
    i = i + 1


#Modul 2 Soal 3
kesempatan = 3
berhasil = False
while kesempatan > 0 and berhasil == False:
    print("Masukkan PIN: ")
    pinInput = input()
    if pinInput == "123456":
        print("Akses Diterima. Selamat Datang!")
        berhasil = True
    else:
        kesempatan = kesempatan - 1
        if kesempatan > 0:
            print("PIN SALAH! Sisa Kesempatan: " + str(kesempatan))
        else:
            print("Kartu ATM Anda Diblokir!")


#Modul 2 Soal 4
totalBelanja = 0
print("Masukkan Jumlah Barang: ")
n = int(input())
for i in range(1, n + 1, 1):
    print("Harga barang ke-: " + str(i))
    harga = float(input())
    print("Kuantitas barang ke-" + str(i))
    kuantitas = int(input())
    totalBelanja = totalBelanja + harga * kuantitas
if totalBelanja >= 500000:
    diskonUtama = totalBelanja * 0.2
else:
    if totalBelanja >= 250000:
        diskonUtama = totalBelanja * 0.1
    else:
        diskonUtama = 0
totalSetelahDiskon = totalBelanja - diskonUtama
print("Punya Member?")
jawabMember = input()
if jawabMember == "ya" or jawabMember == "Ya":
    diskonMember = totalSetelahDiskon * 0.05
else:
    diskonMember = 0
totalAkhir = totalSetelahDiskon - diskonMember
print("Total Bayar Akhir: Rp " + str(totalAkhir))

