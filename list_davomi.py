# # tuple o'zgarmas ro'yxat
# ismlar = ["ali", "vali"]  # oddiy  ro'yxat

# familyalar = ("umrbek", "muhammadali", "elbek", "shoxrux")   # o'zgarmas ro'yxat

# print("oddiy ro'yxat : ", ismlar)
# print("o'zgarmas ro'yxat(tuple) : ", familyalar)

# # familyalar.append("akbar")  # xato beradi, chunki tuple o'zgarmas ro'yxat
# # print(familyalar)

# ismlar.append("akbar")  # to'g'ri ishlaydi, chunki oddiy ro'yxat

# o_familyalar = list(familyalar)  # tuple ni oddiy(list) ro'yxatga aylantirish
# print(o_familyalar) 

# o_familyalar = tuple(o_familyalar)  # ro'yxatni yana tuple ga aylantirish
# print(o_familyalarfamilyalar)



davlatlar = ['O‘zbekiston', 'Qozog‘iston', 'Rossiya', 'AQSh', 'Xitoy']

print("Davlatlar ro'yxati:", davlatlar)
print("Ro'yxat uzunligi:", len(davlatlar))
print("Tartiblangan ro'yxat:", sorted(davlatlar))
print("Teskari tartiblangan ro'yxat:", sorted(davlatlar,reverse=True))
print("Asl ro'yxat:", davlatlar)
davlatlar.reverse()

print("Ortidan boshlab ro'yxat:", davlatlar).sort()

print("Alifbo bo'yicha tartiblangan ro'yxat:", davlatlar)       
davlatlar.sort(reverse=True)
print("Alifboga teskari tartiblangan ro'yxat:", davlatlar) 

juft_sonlar = list(range(120, 1201, 2)) 
print("120 dan 1200 gacha bo'lgan juft sonlar ro'yxati:", juft_sonlar)
print("Sonlar yig'indisi:", sum(juft_sonlar))
print("Eng katta va eng kichik sonlar ayirmasi:", max(juft_sonlar) - min(juft_sonlar))
print("Elementlar soni:", len(juft_sonlar))
print("Ro'yxatning boshidan 20 ta qiymat:", juft_sonlar[:20])
print("Ro'yxatning o'rtasidan 20 ta qiymat:", juft_sonlar[ (len(juft_sonlar)//2 - 10) : (len(juft_sonlar)//2 + 10) ])
print("Ro'yxatning oxiridan 20 ta qiymat:", juft_sonlar[-20:])

taomlar = ['osh', 'shashlik', 'manti', 'lagman', 'somsa']
print("Taomlar ro'yxati:", taomlar)

