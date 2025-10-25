#ismlar ro'yhati va ularga qisqa habar yuborish 
ismlar = ["Shoxrux", "Muhammadali", "Kamolbek"]
print("Salom", ismlar[0] + ", bugun maktab bormi?")
print(ismlar[1] + ", maktabga boramizmi?")

#sonlar ro'yhati 
sonlar = [5, -3, 10, 2.5]
print("Dastlabki sonlar:", sonlar)
#sonlarni o'zgartirish
sonlar[0] = sonlar[0] + 10
sonlar[1] = sonlar[1] * -1
print("O'zgargan sonlar:", sonlar)

#tarixiy,zamonaviy shaxslar 
t_shaxslar = ["Imom Buxoriy", "Amir Temur"]
z_shaxslar = ["Bill Gates", "Elon Musk"]
#ro'yhatdan bitta shaxsni chiqarib olish
tarixiy = t_shaxslar.pop(0)
zamonaviy = z_shaxslar.pop(0)
print(f"Men tarixiy shaxslardan {tarixiy} bilan,")
print(f"zamonaviy shaxslardan esa {zamonaviy} bilan suhbat qilishni istar edim.")

#mehmonlar ro'yxati
friends = []
friends.append("Jasur")
friends.append("Nodir")
friends.append("Bekzod")
friends.append("Olim")
friends.append("Sardor")
#birini chaqira olmaymiz
print("Mehmonlar:", friends)
friends.remove("Bekzod")
print("Yangilangan mehmonlar ro'yxati:", friends)
#boshi va o'rtasiga yangi mehmonlar qo'shish
friends.insert(0, "Jmashid")
friends.insert(2, "Azam")
friends.append("Doston")
print("Yangi mehmonlar ro'yxati:", friends)

#yangi mehmonlar ro'yxati
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
print("Kelgan mehmonlar:", mehmonlar)
print("Kelmaganlar:", friends)
