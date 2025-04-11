hatasiz = False
while hatasiz == False:
    try:
        sayi = int(input("Bir tamsayı giriniz: "))
    except:
        print("Hatalı girdi!")
        hatasiz = False
    else:
        print("Girdide hata bulunmadı!")
        hatasiz = True
    finally:
        print("Girdi bloğu hata kontrolüne tabi tutuldu!")
print(sayi)
