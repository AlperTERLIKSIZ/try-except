while True:
    try:
        yas = int(input("Yaşınızı girin: "))
        if yas < 0:
            raise ValueError("Yaş negatif olamaz!")
        print("Yaşınız:", yas)
        break
    except ValueError:
        print("Geçerli bir yaş girin! (Pozitif bir tam sayı)")
