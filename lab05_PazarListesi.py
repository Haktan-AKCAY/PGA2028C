mesaj = "Pazar listesi yapıyorum."
sepet = []
agirlik = []
print(mesaj, "\n", len(mesaj)*'-', end = "\n", sep = "")
while (1 == 1):
    print("Poşetinizde neler var?")
    icerik = input("Poşet içeriğini giriniz: ")
    icerik = icerik.lower()
    if icerik == "bos":
        break
    varMi = False
    for icindeki in sepet:
        if icindeki == icerik:
            varMi = True
            break
    miktar = float(input("Miktarını giriniz(kg): "))
    if varMi == False:
        sepet.append(icerik)
        agirlik.append(miktar)
    else:
        agirlik[sepet.index(icerik)]+=miktar
print("Pazardan Alınacaklar: ")
for indis in range(len(sepet)):
    print(sepet[indis][0].upper(), sepet[indis][1:], "\n", agirlik[indis], "kg", sep = "")
