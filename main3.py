import math

while True:
    try:
        sayi = float(input("Bir sayı girin: "))
        karekok = math.sqrt(sayi)
        print("Karekök:", karekok)
        break
    except ValueError:
        print("Negatif sayı veya geçersiz giriş! Lütfen tekrar deneyin.")
