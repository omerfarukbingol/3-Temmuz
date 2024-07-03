# Liste icerisinde tekrar etmeyen sayıyı bulma
# liste=[1,2,3,4,1,4,3,3,1,4,5,5]
# repliesValues=[]
# for value in liste:
#     if(liste.count(value)>1):
#         repliesValues.append(value)
#     else :
#         print(f"{value} rakamından bir adet var")


# print(
#     list(set(repliesValues))
# )

#!####################################################################################################

# Bir dizideki elemanları kullanarak , toplamı verilen sayıları elde etmek icin bir fonksiyon yazınız.
# istenilenToplam=int(input('bulmak istediginiz sayıyı giriniz: '))
# sayilar=[1,2,3,4,5,6,7,8,9,10]
# toplam=0

# for sayi in sayilar:
#     toplam+=sayi
#     if(toplam==istenilenToplam):
#         print("Toplama ulasıldı ")

#!########################################################################################################

sayi1=int(input('birinci sayı: '))
sayi2=int(input('ikinci sayı: '))

sayi1Bolenleri=[]
sayi2Bolenleri=[]


def ortak_bolen(sayi1,sayi2):
    #!bolenleri ayarlıyoruz
    bolen1=sayi1
    bolen2=sayi2
    #Birinci sayinin bolenlerini eklemeliyiz
    for sayi in range(1,sayi1+1):
       if(sayi1%bolen1==0):
           sayi1Bolenleri.append(bolen1)
    bolen1-=1
        
    
    #İkinci sayinin bolenlerini eklemeliyiz
    for sayi in range(1,sayi2+1):
       if(sayi1%bolen2==0):
           sayi1Bolenleri.append(bolen2)
    bolen2-=1
        


ortak_bolen(sayi1,sayi2)
print(sayi1Bolenleri)
print(sayi2Bolenleri)
    
