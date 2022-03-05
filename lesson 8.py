# son = 1
# while son<=5:
#     print(son, end=(','))
#     son +1
#
# else:
#     print('tamom')



#shartni tekirish yo'li bilan tsiklni to'xtatish
# print('kiritilgan kvadratini qaytaruvchi dastur ')
# savol = 'Istalgan sonni kiriting '
# savol +='(dasturni to\'xtaish uchun \'q\'harfni kiriting )'
# qiymat = ''
# while qiymat!='q':
#     qiymat = input(savol)
#     if qiymat != 'q':
#         print(int(qiymat) ** 2)
#
# print('Dastur tugadi.')





#ishora orqali skilnito'xtatish
# print('kiritilgan kvadratini qaytaruvchi dastur ')
# savol = 'Istalgan sonni kiriting '
# savol +='(dasturni to\'xtaish uchun \'q\'harfni kiriting )'
#
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat =='q':
#         ishora = False
#     else:
#         print(int(qiymat)**2)
# print('Dastur tugadi.')



#break funkusyasi yordamida to'xtatish

# print('kiritilgan kvadratini qaytaruvchi dastur ')
# savol = 'Istalgan sonni kiriting '
# savol +='(dasturni to\'xtaish uchun \'q\'harfni kiriting )'
# while True: #abadiy tskil
#     qiymat = input(savol)
#     if qiymat== 'q' : #shartni tekshiramiz
#         break # tskilni shu joyda buzamiz
#     else:
#       print(int(qiymat)**2) #shartdan False qaytsa bajariladi


#
#break for tskilda
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f'{son} ning kubi {son ** 3} ga teng')


#break tskilda for & while
# son = 1
# while son<11:
#     if son ==5:
#         break
#     print(f'{son} ning kubi {son**3} ga teng')
#     son = son + +1


#continu for tskilda

# sonlar = list(range(1,11))
# for son in sonlar:
#      if son ==5:
#          continue
#      if son ==1:
#          continue
#      print(f'{son} ning kubi {son ** 3} ga teng')

#
# son = 0
# while son <100:
#     son +=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# infinity loops

# son = 0
# while True:
#     son+1
#     if son%2!=0:
#         continue
#     else:
#         print(son)




# masala
# a= int(input('Son kiriting '))
# b=int(input('2 ni son kiriting '))
# while a>=b:
#     a=a-b
# else:
#     print(a)


# a= int(input('Son kiriting '))
# b=int(input('2 ni son kiriting '))
# hisob = 0
# while a>=b:
#     a=a-b
#     hisob+1
# else:
#     print(hisob)






#3
# n = int(input('n sonni kiriting>>> '))
# k = int(input('k sonni kiriting>>> '))
# butun = 0
# while n>=k:
#     n = n - k
#     butun +=1
# print(f'{butun} butun,{n} qoldiq ')


# while 4
# n = int(input('n sonni kiriting(N>0)>>> '))
# n=n+0
# while n<=3:
#     n=n-3
# if n//3:
#     n = n - 3
#     if n == 0:
#         print(f'{n} soni 3 ning  darjasi   ')
# elif n==0 :
#     print(f'{n} soni 3 ning  darjasi emas ')

# print("keling siz bilan sevimli sevimli mevalar ro\'yxatini tuzamiz")
# mevalar = []
# soni = 1
# while True:
#     savol = f"{soni}-sevimli mevangizni nomini kiriting: "
#     meva = input(savol)
#     mevalar.append(meva)
#     takror = input("Yana meva meva qo\'shasizmi (ha yoki yo'q) ? ")
#     soni=soni+1
#     if takror.lower()=='yoq':
#         break
# print(f'Sizni sevimli  mevalaringiz ro\'yxati:')
# for meva in mevalar:
#     print(meva, end=', ')

# mevalar = ['olma','anor','olcha','shaftoli','gilos']
# for meva in mevalar:
#     if meva == 'olcha':
#         break
#
#     print(f"Men {meva.title()}ni yaxshi ko\'raman")




# for ism in 'Abdulaziz':
#     print(ism)
#     print("Abdulaziz")

# i = True
# son = 1
# while i:
#     son +=1
#     if son%2==0:
#         print(son)
#         if son ==1000:
#             i=False























































































































