def pi(): #parametre almayan ve değer döndüren fonksiyon
    return 3.14

def cemberinCevresi(yaricap): #parametre alan ve değer döndüren fonksiyon
    return 2*pi()*yaricap
def reklam(): #parametre almayan ve değer döndürmeyen fonksiyon
    mesaj = "Bu okulun en çalışkan sınıfı 9C sınıfıdır!"
    print(len(mesaj)*"-")
    print(mesaj)
    print(len(mesaj)*"-")

def sinifBas(x, y): #parametre alan ve değer döndürmeyen fonksiyon
    for say in range(y):
        print((say+1)*(x+" "))
        
r = int(input("Çembere ait yarıçap uzunluğu giriniz:"))
print("Yarıçapı", r, "olan çemberin çevresi", cemberinCevresi(r))
sinifBas("9C", 5)
reklam()
