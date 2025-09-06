from utils import konversi_suhu

print("*"*30)
print("Konversi Suhu".center(30))
print("*"*30)
print("c = Celsius")
print("f = Fahrenheit")
print("k = Kelvin\n")

dari = input("Masukkan satuan asal (c/f/k): ").strip()
ke = input("Masukkan satuan tujuan (c/f/k): ").strip()

try:
    nilai = float(input("\nMasukkan nilai suhu: "))
except ValueError:
    print("Error: Nilai suhu harus berupa angka.")
    exit()

hasil = konversi_suhu(nilai, dari, ke)

if isinstance(hasil, str): 
    print(hasil)
else:  
    print(f"\nHasil konversi: {nilai}°{dari.upper()} = {hasil:.2f}°{ke.upper()}")