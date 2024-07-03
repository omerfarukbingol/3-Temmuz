
#! Faktoriyel Hesaplama Fonksiyonu

# def faktoriyel_al(sayi):
#     carpim=1
#     for i in range(1,sayi+1):
#         carpim*=sayi
#         sayi-=1
#     print(carpim)


# faktoriyel_al(6)


#!#################################################################################################

###################################################################################################
# Girilen kelimeyi palindrom mu değil mi kontrol ediniz

#! Hatalı fonksiyon
# istenilenKelime=input('bir kelime giriniz: ')

# def palindrom_kontrol(kelime):
#     reversedWord=''
#     liste=list(kelime).reverse()
#     for i in liste:
#         reversedWord+=i
#     if(reversedWord==istenilenKelime):
#         print("Girilen kelime palindrom bir kelime")
#     else : 
#         print("Girlen kelime palindrom kelime değil")

# palindrom_kontrol(istenilenKelime)


#! Dogru Fonksiyon

def palindrom_check(kelime):
    reversedWord=''.join(list(reversed(kelime)))

    if(reversedWord==kelime):
        print("Girilen kelime palindrom bir kelime")
    else : 
        print("Girilen kelime palindrom bir kelime degil")

istenilenKelime=input('kelime girin : ')
palindrom_check(istenilenKelime)