# a = input('tilni tanlang (uzbek and enlish) ')
#
# # if a==uzbek or english:
# #     print('Siz til tanladingiz ')
# # else:
# #     print('siz tilni tanlang ')
# b = input('So\'zi kiriting ')
# enuz={
#     'book':'kitob',
#     'pen':'ruchka',
#     'program':'Program',
#     'nootbook':'daftar',
#     'pencil':'qalam',
#     'one':1,
# }
# en = {
#     'kitob':'book',
#     'ruchka':'pen',
#     'programa':'program',
#     'daftar':'nootbook',
#     'qalam':'pencil',
#     'olma':'apple'
# }
# print(enuz[b],[en])




from pprint import  pprint as print
mashinalar = {
    'kalit':'qiymat',
    "car":{
        'malibu2':{
            'rangi':'oq',
            'tezligi':'220km\s',
            'narxi':'210000$$',
        },
        'nexia':{
            'rangi':'oq',
            'tezligi':'190',
            'narxi':'10000$$'
        }

    }
}

# print(mashinalar['car']['nexia']['tezligi'])
# print(mashinalar ['car']['malibu2'].get('tezligi','bunday so\'z topilmadi'))
#
# print(mashinalar.items())
# print(mashinalar['car'].keys())
# print(mashinalar)


# talaba = {
#     'ism':'Rahmatillo',
#     'familya':'Rashidov',
#     'yoshi':20,
#     'fakulteti':'dasturlash',
#     'kursi':4
#
# }
#
# # for kalit ,qiymat in talaba.items():
# #     print(f'kalit >>>> {kalit}'
# #           f' : qiymat >>> {qiymat} ')
#
#
#
#
#
mahsulotlar = {
    'olma':7000,
    'banan':19500,
    'go\'sht':68000,
    'karto\'shka':5000,
    'piyoz':3000
}

# print(mahsulotlar.values())
#
#
#
# print('Do\'kondagi mahsulotlar')
#
#
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.upper())
#


# dictdan qiymat olish
# print(mahsulotlar.values())
#
#
#
# print('Do\'kondagi mahsulotlar')
#
#
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.upper())


telefonlar = {
    'jahongir':'Samsung A6',
    'abror':'Redmi 6 pro',
    'muhhamdjon':'LG x6',
    'abdurauf':'samsung A6',
    'alisher':'samsung a20',
    'adulaziz':'samasung A02',
    'Mirziyo':'Redmi 6',
    'rahmatillo':'Redmi 7'
}
#
# print(f'Xonamizdagi{telefonlar} rusmudagi telefondan foydalandi')



# for ism,qiymat in telefonlar.items():
#     print(f'Xonamizdagi {ism.title()} {qiymat.upper()} ishlatadi')

# telefonlar['Nozimjon'] = 'samsung a9'
# print(telefonlar)
















