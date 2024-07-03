import random

# 0-100 arasında random bir sayı ürettik.
randomNumber=random.randint(1,10)
# print(randomNumber)

t=0

tahminAdedi=int(input('Kaç adet hakkınız olsun? '))
for i in range(1,tahminAdedi+1):
    sayi=int(input('Bir adet sayı giriniz: '))
    if(sayi==randomNumber):
        print("Tebrikler sayı bildiniz")
        t+=1
        break

if(t!=1):
    print("Maalesef sayıyı bilemediniz")


