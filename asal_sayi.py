# Bir sayının asal sayı olup olmadıgını bulalım.

sayi=int(input('bir adet sayı giriniz : '))
baslangic=sayi
bolenAdedi=0
while baslangic>=1:
    if(sayi%baslangic==0):
        bolenAdedi+=1
    baslangic-=1

if(bolenAdedi>2):
    print(f"{sayi} sayisi bir asal sayi degildir, bolen sayısı {bolenAdedi}")
else :
    print(f"{sayi} sayisi bir asal sayidir")