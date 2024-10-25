car_0 = { 'model':'bmw','rang':'qorcla'}
print(car_0['model'])
talaba_0 ={'ism':'Asror','yil':'2009','yosh':'15'}
print(f"{talaba_0['ism'].title()}),\
{talaba_0['yil']}-yilda tugilgan,\
{talaba_0['yosh']}yoshda")
telefonlarr = {
    'ali':'iphon x  not pro ultra',
    'vali':'redmi not 13 c',
    'xumoyun':'infinix 8'
}
phone = telefonlarr['asror']
print(f"Alining telefoni {phone}")
phone = telefonlarr.get('asror','Bunday ism mavjud emas')
print(phone)
talaba_0 = {
     'ism':'alijon',
     'familiya':'shamshiyev',
     'yosh':22,
     'fakultet':'matematika',
     'kurs':4  
        }

print(talaba_0.items())
for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'nokia 33310'
     }

for k, q in telefonlar.items():
mahsulotlar = { 
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys()) 
print('Dokondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title()) 
sonlar = {
    'ali':'nokia',
    'vali':'nokia',
    'bobr':'samsung',
    'hasan':'samsung'
     }
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for son in set (sonlar.values()):
    print(son)
car0 = {
    'model':'cobalt ltz',
    'rang':'qora',
    'yil':2000,
    'narh':15000,
    'km':89000,
    'karopka':'avtomat'
     }
car = car0
print(f"{car['model'].title}),\
    {car['rang']}
amallar = {
    'integer':'butun son',
    'boolean':'mantiqiy qiymat',
    'float':'onlik son',
    'for':'biror amalni qayta-qayta bajarish tsikli',
    'if':'shartlarni tekshirish operatori'
     }
for k,v in sorted(amallar.items()):
    print(f"{k.title()} - {v.title()}") 