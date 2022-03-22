# #ZADANIE_1
#
# lista_sportów=['piłka nożna','piłka ręczna','mieszane sztuki walki']
# print(lista_sportów)
# lista_sportów.reverse()
# print("Po przekształceniu: ",lista_sportów)
# lista_sportów.append('koszykówka')
# lista_sportów.append('hokej')
# print(lista_sportów)

# #ZADANIE_2
#
# słownik={ 'itd':'i tak dalej', 'np': 'na przykład' ,'cdn':'ciąg dalszy nastąpi'}
# print(słownik)
#
# #ZADANIE_3
#
# słownik_gry={'CS':'Counter Strike','MC':'Minecraft','LOL':'Ligue Of Legends'}
# print(słownik_gry)

# #ZADANIE_4
#
# napis=input('napisz zdanie: ')
# print(napis.count('a'))

# #ZADANIE_5
# import sys as system
# system.stdout.write('wczytaj a')
# a=system.stdin.readline()
# a=int(a)
# system.stdout.write('wczytaj b')
# b=system.stdin.readline()
# b=int(b)
# system.stdout.write('wczytaj c')
# c=system.stdin.readline()
# c=int(c)
# print(a**b+c)

# #ZADANIE_6

# a=input("podaj pierwsza liczbe : ")
# b=input("podaj druga liczbe : ")
# c=input("podaj trzecia liczbe : ")
# if (a>b) & (a>c):
#     print("pierwsza jest największa")
# if (b>a) & (b>c):
#     print("druga jest największa")
# if (c>a) & (c>b):
#     print("trzecia jest największa")

# #ZADANIE_7

# lista=[1,2.2,3,4.4,5,6.6,7,8.8,9,10.10]
# for i in lista:
#      print(i**2)

# #ZADANIE_8

# a=0
# lista=[]
# while a!=10:
#    if a%2==0:
#      lista.append(a)
#    a+=1
# print(lista)

#ZADANIE_9
liczba=input("podaj liczbe z której wyciągnąć pierwiastek?")
liczba=int(liczba)
if liczba<0:
   print("Podana liczba jest mniejsza od 0")
else:
   print(pow(liczba,1/2))


