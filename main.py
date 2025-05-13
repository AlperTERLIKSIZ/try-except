liste = ["elma", "armut", "muz"]

try:
    indeks = int(input("İndeks girin: "))
    print(liste[indeks])
except (ValueError, IndexError):
    print("Geçersiz indeks!")
