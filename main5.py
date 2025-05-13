sepet = [49.99, 25.50, "yanlış veri", 10.0, 5.25]

toplam = 0

for fiyat in sepet:
    try:
        toplam += float(fiyat)
    except ValueError:
        print(f"Hatalı veri: {fiyat} — bu fiyat atlandı.")
    except TypeError:
        print(f"Geçersiz tür: {fiyat} — bu fiyat atlandı.")

print("Toplam fiyat:", toplam)
