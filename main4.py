toplam = 0
adet = 0

while True:
    girdi = input("Bir sayı girin (bitirmek için 'q'): ")
    if girdi == 'q':
        break
    try:
        sayi = float(girdi)
        toplam += sayi
        adet += 1
    except ValueError:
        print("Hatalı giriş! Lütfen bir sayı girin.")

if adet > 0:
    print("Ortalama:", toplam / adet)
else:
    print("Hiç sayı girilmedi.")
