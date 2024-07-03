# En basitinden bir fonksiyon aşağıdaki gibi tanımlanır.

def kayit_olustur(isim,soyisim,bolum):
    print("-"*30)
    print(f"Adınız   :   {isim}")
    print(f"Soyadınız    :   {soyisim}")
    print(f"Bolumunuz     :  {bolum}")

kayit_olustur("Omer","Bingol","Computer Programmer")

#! Fonksiyon tanımlarken 'def' anahtar kelimesini kullanılırız. Daha sonrasında fonksiyonumuza bir isim veririz ve ondan da sonra parametre alacak mı almayacak mı onu belirleriz
#! İki noktadan sonra calistirmak istedigimiz kodları yazarız.


def greeting_world():
    print("Hellow World!")

greeting_world()