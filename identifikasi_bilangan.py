num = int(input("Masukkan angka : "))

while 10 > num or 15 < num < 20 or 25 < num < 35 or num > 40:
    print("Salah!")
    num = int(input("Masukkan angka : "))
else:
    print("True")