sorozat:list[int] = [26, 2, 11, 7, 42, 7, 34]
print(f'input: {sorozat}')

# szorozatszámítás: összegzés
# [sorozat elemeinek összegét tudod vele meghatározni]
osszeg:int = 0
for szam in sorozat:
    osszeg += szam # ua. mint a sum = sum + szam
print(f'összegzés tételének outputja: {osszeg}')

# megszámlálás
# megadja az <T> tulajdonságú elemek számát a sorozatban
# [ebben a példában a páros elemek száma]
darab:int = 0
for szam in sorozat:
    if szam % 2 == 0:
        darab += 1
print(f'megszámlálás tételének (páros elemekre vonatkoztatott) outputja: {darab}')

# szélsőérték meghatározás: megadja az adott sorozat legkisebb/legnagyobb elemének helyét

mini:int = 0
for index in range(1, len(sorozat)):
    if sorozat[index] < sorozat[mini]:
        mini = index
print(f'legkisebb elem indexe: {mini}')
print(f'legkisebb elem értéke: {sorozat[mini]}')
print(f'ez a sorozat {mini + 1}. eleme')

maxi:int = 0
for index in range(1, len(sorozat)):
    if sorozat[index] > sorozat[maxi]:
        maxi = index
print(f'legnagyobb elem indexe: {maxi}')
print(f'legnagyobb elem értéke: {sorozat[maxi]}')
print(f'ez a sorozat {maxi + 1}. eleme')

# szamok = [3, 200, 3, 100, 11]
# lne:int = szamok[0]
# for szam in szamok[1:]:
#     if szam > lne:
#         lne = szam
# print(f'legnagyobb szám: {lne}')

# lineáris keresés:
keresett:int = int(input('irj be egy szamot: '))
index:int = 0
while index < len(sorozat) and sorozat[index] != keresett:
    index += 1
if index < len(sorozat):
    print('VAN TALÁLAT')
    print(f'a {keresett} indexe: {index}')
else:
    print('NINCS TALÁLAT')

# szavak = ['cica', 'kutya', 'nokedli', 'bicikli', 'páfrány']
# index = -1

# keresett = input('irdbeide: ')
# for i in range(len(szavak)):
#     if szavak[i] == keresett:
#         index = i
#         break
# if index != -1:
#     print('van találat')
#     print(f'helye: {index}')
# else: print('nincs találat')


# kiválasztás:
# CSAK AKKOR HASZNÁLHATÓ ha az inputot BIZTOSAN TARTALMAZZA a sorozat:

napok = ['hetfo', 'kedd', 'szerda', 'csutortok', 'pentek', 'szombat', 'vasarnap']

nap = input('írd be a hét egy napját: ')

index = 0
while nap != napok[index]:
    index += 1
print(f'a {nap} a hét {index + 1}. napja')

# eldöntés
# van-e a sorozatban 3al osztható szám?

index = 0
while index < len(sorozat) and sorozat[index] % 3 != 0:
    index += 1
if index < len(sorozat): print(f'van 3al osztható elem')
else: print('nincs 3al osztható elem')

# kiválogatás
paratlanok:list[int] = []

for szam in sorozat:
    if szam % 2 == 1:
        paratlanok.append(szam)
print(f'páratlan elemek: {paratlanok}')