ogrenci_ort = float(input("Ortalamınızı giriniz: "))
zayif_sayi = int(input("Zayıf sayınızı giriniz: "))

if zayif_sayi == 0:
    if ogrenci_ort >= 85 and ogrenci_ort < 100:
        print("Takdir Belgesi alarak sınıfı geçtiniz.")
    elif ogrenci_ort >= 70:
        print("Teşekkür Belgesi alarak sınıfı geçtiniz.")
    elif ogrenci_ort >= 50:
        print("Takdir Belgesi alarak sınıfı geçtiniz.")
    else:
        print("Ortalama yükseltme sınavlarına giriniz.")
else:
    if ogrenci_ort >= 50:
        print("Sorumlu olarak sınıfı geçtiniz.")
    elif ogrenci_ort > 25:
        print("Sorumluluk sınavlarına giriniz.")
    else:
        print("Sınıfta tekrarı.")
