sozluk = {
    "elma": "Apple",
    "armut": "Pear",
    "muz": "Banana"
}

try:
    anahtar = input("Bir meyve ismi girin: ")
    print("İngilizcesi:", sozluk[anahtar])
except KeyError:
    print("Hata: Bu anahtar sözlükte yok!")
