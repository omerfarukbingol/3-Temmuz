# Range() metodu 

# liste=list(range(11))
# print(liste)

# liste=list("Omer Faruk Bingol")
# print(liste)

# for i in range(1,11):
#     print(i)

#! Set Kullanımı

# isimler=["Ayse","Mustafa","Kayra","Ali","Ayse","Ayse"]
# isimler=set((isimler))
# print(isimler)

# set1=set(isimler)
# print(set1)
# print(set1)

#! CONTINUE

# for i in range(5):
#     if(i==2):
#         continue
#     print(i)

# print("-------------------------------------")

# for i in range(5):
#     if(i==2):
#         break
#     print(i)

#! Obje

obje1={
    "name":"omer",
    "surname":"bingol",
    "age":20,
    "job":"computer programmer"
}

isim=input('isim giriniz: ')
if(isim==obje1['name']):
    print('giris islemi basarili')
else :
    print("giriş basarisiz")
