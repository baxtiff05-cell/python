# """
# for loop sikl sikl yaratishda ishlatilaadi 
# """
# oquvchilar = ['Kamolbek', 'Umrbek', 'Shoxrux', 'Muhammadali']

# print(f"Assalomu alaykum {oquvchilar[0]},ishlar qonday!")
# print(f"Assalomu alaykum {oquvchilar[1]},ishlar qonday!")
# print(f"Assalomu alaykum {oquvchilar[2]},ishlar qonday!")
# print(f"Assalomu alaykum {oquvchilar[3]},ishlar qonday!")

# for ism in oquvchilar:
#     print(f"Salom ! {ism.title()}")
#     print(f"Dars tugadi{ism.upper()} ")



# raqamlar = list((1,11,-5,7,3,9,15,-20,0))
# for raqam in raqamlar:
#     print(f"{raqam} ning kvadrati {raqam**2} ga teng")

    
# raqamlar = list(range(20,31,21))
# for raqam in raqamlar:
#     print(f"{raqam} ning kubini 9 ga bo'lganda {raqam/9} ga teng")



sonlar2 = []

sonlar = list(range(1,11))

print(f"Asl sonlar ro'yxati: {sonlar}")
for son in sonlar:
    sonlar2.append(son**4)
    print(f"4-darajaga oshgan ro'yhat {sonlar2}")

    
