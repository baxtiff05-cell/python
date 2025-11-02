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


# Davlatlar ro'yxatini yaratamiz
davlatlar = ["Ozbekiston", "AQSH", "Rossiya", "Xitoy", "Turkiya"]

# Ro'yxatni ekranga chiqaramiz
print(davlatlar)

# Ro'yxat uzunligini (nechta element borligini) chiqaramiz
print("Ro'yxat uzunligi:", len(davlatlar))

# Davlatlarni alifbo tartibida (A dan Z gacha) tartiblab chiqaramiz
print("Tartiblangan ro'yxat:", sorted(davlatlar))

# Davlatlarni alifboga teskari tartibda (Z dan A gacha) chiqaramiz
print("Teskari tartiblangan ro'yxat:", sorted(davlatlar, reverse=True))

# Asl ro'yxatni (tartiblanmagan holatda) yana chiqaramiz
print("Asl ro'yxat:", davlatlar)

# Ro'yxatni butunlay teskari tartibda aylantiramiz (birinchi element oxiriga, oxirgisi boshiga)
davlatlar.reverse()
print("Ortidan boshlab ro'yxat:", davlatlar)

# Davlatlarni yana alifbo tartibida chiqaramiz (asl ro'yxatdan mustaqil)
print("Alifbo bo'yicha tartiblangan ro'yxat:", sorted(davlatlar))

# Davlatlarni alifboga teskari tartibda chiqaramiz
print("Alifboga teskari tartibda ro'yxat:", sorted(davlatlar, reverse=True))


# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini hosil qilamiz
# range(120, 1201, 2) -> 120 dan boshlaydi, 1200 gacha boradi, har safar 2 ga oshadi
juft_sonlar = list(range(120, 1201, 2))
print("Juft sonlar ro'yxati:", juft_sonlar)

# Juft sonlar yig'indisini hisoblaymiz
yigindi = sum(juft_sonlar)
print("Sonlar yig'indisi:", yigindi)

# Eng katta va eng kichik sonlarni topamiz
eng_katta = max(juft_sonlar)
eng_kichik = min(juft_sonlar)

# Eng katta va eng kichik sonlar orasidagi farqni hisoblaymiz
ayirma = eng_katta - eng_kichik
print("Eng katta va eng kichik son o'rtasidagi ayirma:", ayirma)

# Ro'yxatda nechta element borligini aniqlaymiz
print("Elementlar soni:", len(juft_sonlar))

# Ro'yxatning boshidagi 20 ta elementni chiqaramiz
print("Ro'yxatning boshidan 20 ta qiymat:", juft_sonlar[:20])

# Ro'yxatning o'rtasidan 20 ta elementni chiqaramiz
# len(juft_sonlar)//2 -> ro'yxat markazidagi indeks
# undan 10 ta oldin va 10 ta keyin elementlarni olamiz
print("Ro'yxatning o'rtasidan 20 ta qiymat:", juft_sonlar[len(juft_sonlar)//2-10 : len(juft_sonlar)//2+10])

# Ro'yxatning oxiridagi 20 ta elementni chiqaramiz
print("Ro'yxatning oxiridan 20 ta qiymat:", juft_sonlar[-20:])

# Taomlar ro'yxatini yaratamiz
taomlar = ["osh", "shashlik", "manti", "lag'mon", "somsa"]

# Taomlar ro'yxatini ekranga chiqaramiz
print("Taomlar ro'yxati:", taomlar)



