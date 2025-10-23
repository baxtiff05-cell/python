import math

  #.5. Kubning yon tomoni a berilgan. Uning hajmini 
a = int(input("Kubning yon tomonini yozing: a ="))
print("Kubning hajmi(V=a**3): V=", a**3)
print("Kubning to'la sirti(S=6*a**2):S=", 6*(a**2))

# 6. Parallelepipedning tomonlari a, b, c berilgan. Uning hajmi V = a * b * c va to'la sirti S = 2 * (a * b + b * c + a * c) aniqlansin.
a = 4
b = 5
c = 6
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(f"Parallelepipedning hajmi V = {V}")
(f"Parallelepipedning to'la sirti S = {S}")

#7. Doiraning radiusi R berilgan. Uning uzunligi L va yuzasi S aniqlansin. L = 2 * pi * R, S = pi * R**2
import math

R = 10
pi = math.pi
L = 2 * pi * R
S = pi * R**2
print(f"Doiraning uzunligi L = {L}")
print(f"Doiraning yuzasi S = {S}")

# 8- Ikkita a va b berilgan. Ularning o'rta arifmetigi aniqlansin. (a + b) / 2
a = 15
b = 25
orta_arifmetik = (a + b) / 2
print(f"Sonlarning o'rta arifmetigi = {orta_arifmetik}")

# 9. Ikkita manfiy bo'lmagan son a va b berilgan. Ularning o'rta geometrigi aniqlansin. sqrt(a * b)
import math

a = 4
b = 9
orta_geometrik = math.sqrt(a * b)
print(f"Sonlarning o'rta geometrigi = {orta_geometrik}")

#10. Nolga teng bo'lmagan ikkita son berilgan. Ularning yig'indisi, ko'paytmasini va har birining kvadratini aniqlansin.
a = 7
b = 3
yigindi = a + b
kopaytma = a * b
a_kvadrati = a**2
b_kvadrati = b**2
print(f"Yig'indi = {yigindi}")
print(f"Ko'paytma = {kopaytma}")
print(f"a sonining kvadrati = {a_kvadrati}")
print(f"b sonining kvadrati = {b_kvadrati}")

#11. Nolga teng bo'lmagan ikkita son berilgan. Ularning yig'indisi, ko'paytmasini va har birining modulini aniqlansin.
a = -8
b = 2
yigindi = a + b
kopaytma = a * b
a_moduli = abs(a)
b_moduli = abs(b)
print(f"Yig'indi = {yigindi}")
print(f"Ko'paytma = {kopaytma}")
print(f"a sonining moduli = {a_moduli}")
print(f"b sonining moduli = {b_moduli}")

# 12. To'g'ri uchburchakning katetlari a va b berilgan. Uning gipotenuzasi c va perimetri P aniqlansin. c = sqrt(a**2 + b**2), P = a + b + c
import math

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
P = a + b + c
print(f"Gipotenuza c = {c}")
print(f"Perimetr P = {P}")

# 13. Umumiy markazga bo'lgan ikkita aylana radiusi berilgan. R1, R2 (R1 > R2). Ularning yuzalari S1 va S2, ularning ayirmasi S3 aniqlansin. S1 = pi * R1**2, S2 = pi * R2**2, S3 = pi * (R1**2 - R2**2).
import math

R1 = 8
R2 = 5
pi = math.pi

S1 = pi * R1**2
S2 = pi * R2**2
S3 = S1 - S2  # yoki S3 = pi * (R1**2 - R2**2)
print(f"Birinchi aylananing yuzasi S1 = {S1}")
print(f"Ikkinchi aylananing yuzasi S2 = {S2}")
print(f"Yuzalarning ayirmasi S3 = {S3}")

# 14. Aylananing uzunligi L berilgan. Uning radiusi R va yuzasi S aniqlansin. L = 2 * pi * R, S = pi * R**2, pi = 3.14
pi = 3.14
L = 31.4  # Misol uchun, aylana uzunligi

R = L / (2 * pi)
S = pi * R**2
print(f"Aylananing radiusi R = {R}")
print(f"Aylananing yuzasi S = {S}")

# 15. Aylananing yuzasi S berilgan. Uning diametri d va radiusi R aniqlansin. L = 2 * pi * R, S = pi * R**2, pi = 3.14
import math

pi = 3.14
S = 78.5  # Misol uchun, aylana yuzasi

R = math.sqrt(S / pi)
d = 2 * R
L = 2 * pi * R
print(f"Aylananing radiusi R = {R}")
print(f"Aylananing diametri d = {d}")
print(f"Aylananing uzunligi L = {L}")

# 16. Sonlar o'qida ikkita nuqta orasidagi masofa aniqlansin. |x2 - x1|
x1 = -5
x2 = 12
masofa = abs(x2 - x1)
print(f"Nuqtalar orasidagi masofa = {masofa}")

#Begin17. Sonlar o'qida A, B, C nuqtalar berilgan. AC va BC kesmalarning uzunligini va kesmalar uzunligining yig'indisini topuvchi programma tuzilsin.
#A, B, C nuqtalarining koordinatalari
A = 2
B = 8
C = 5

AC_uzunligi = abs(C - A)
BC_uzunligi = abs(C - B)
yigindi = AC_uzunligi + BC_uzunligi
print(f"AC kesmaning uzunligi = {AC_uzunligi}")
print(f"BC kesmaning uzunligi = {BC_uzunligi}")
print(f"Kesmalar uzunligining yig'indisi = {yigindi}")

# 18. Sonlar o'qida A, B, C nuqtalar berilgan. C nuqta A va B nuqtalar orasida joylashgan. AC va BC kesmalar uzunligining ko'paytmasini toping.
#C A va B orasida joylashgani uchun A < C < B yoki B < C < A sharti bajariladi
A = 1
B = 10
C = 4 

AC_uzunligi = abs(C - A)
BC_uzunligi = abs(B - C)
kopaytma = AC_uzunligi * BC_uzunligi
print(f"AC kesmaning uzunligi = {AC_uzunligi}")
print(f"BC kesmaning uzunligi = {BC_uzunligi}")
print(f"Kesmalar uzunligining ko'paytmasi = {kopaytma}")

# 19. To'g'ri to'rtburchakning qarama-qarshi uchlari koordinatlari (x1, y1) va (x2, y2) berilgan. Uning tomonlari koordinata o'qiga parallel. To'g'ri to'rtburchakning perimetri va yuzasi aniqlansin.
x1, y1 = 1, 2
perimetr = 2 * (a + b)
yuza = a * b
print(f"To'rtburchakning tomonlari: a = {a}, b = {b}")
print(f"To'rtburchakning perimetri = {perimetr}")
print(f"To'rtburchakning yuzasi = {yuza}")

# 20. Tekislikdagi berilgan ikki nuqta (x1, y1) va (x2, y2) orasidagi masofa topilsin. sqrt((x2 - x1)**2 + (y2 - y1)**2)
import math

x1, y1 = 1, 1
x2, y2 = 4, 5

masofa = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Ikki nuqta orasidagi masofa = {masofa}")

# 21. Uchburchakning uchta uchining koordinatlari berilgan (x1, y1), (x2, y2), (x3, y3). Ikki nuqta orasidagi masofani topish formulasi (Begin20) dan foydalanib, uchburchakning yuzasini va perimetrini toping. S = sqrt(p * (p-a) * (p-b) * (p-c)), p = (a + b + c) / 2
import math

x1, y1 = 0, 0
x2, y2 = 3, 0
x3, y3 = 0, 4
# 22. Berilgan A va B sonlarining qiymatlarini almashtiring. A va B ning yangi qiymati ekranga chiqarilsin.
A = 10
B = 20
print(f"Almashtirishdan oldin: A = {A}, B = {B}")

# # Qiymatlarni almashtirish
A, B = B, A

print(f"Almashtirishdan keyin: A = {A}, B = {B}")

# 23. A, B va C sonlari berilgan. A ni qiymati B ga, B ni qiymati C ga va C ni A ga almashtirilsin. A, B va C ning yangi qiymatlari ekranga chiqarilsin.
A = 1
B = 2
C = 3
print(f"Almashtirishdan oldin: A = {A}, B = {B}, C = {C}")

#Qiymatlarni almashtirish (A -> B, B -> C, C -> A)
# # Vaqtinchalik o'zgaruvchi yordamida yoki Pythonda bir qatorda
# A, B, C = B, C, A

print(f"Almashtirishdan keyin: A = {A}, B = {B}, C = {C}")

# 24. A, B va C sonlari berilgan. A ni qiymati C ga, C ni qiymati B ga va B ni A ga almashtirilsin. A, B va C ning yangi qiymatlari ekranga chiqarilsin.
A = 10
B = 20
C = 30
print(f"Almashtirishdan oldin: A = {A}, B = {B}, C = {C}")

# # Qiymatlarni almashtirish (A -> C, C -> B, B -> A)
# # Python yordamida: A ni yangi qiymati C ning eskisi, C ni yangi qiymati B ning eskisi, B ni yangi qiymati A ning eskisi
#A, C, B = C, B, A

print(f"Almashtirishdan keyin: A = {A}, B = {B}, C = {C}")

# 25. x ning qiymati berilganda y = 3 * x**5 - 6 * x**2 - 7 funksiyaning qiymati aniqlansin.
x = 2 # Misol uchun

y = 3 * (x**5) - 6 * (x**2) - 7
print(f"x = {x} da funksiya qiymati y = {y}")

#26. x ning qiymati berilganda y = 4 * (x - 3)**6 - 7 * (x - 3)**2 + 2 funksiyaning qiymati aniqlansin.
x = 5  # Misol uchun
t = x - 3
y = 4 * (t**6) - 7 * (t**2) + 2
print(f"x = {x} da funksiya qiymati y = {y}")

# 27. A soni berilgan. A ning A**2, A**4, A**8 darajalarini aniqlovchi programma tuzilsin.

A2 = A**2
A4 = A2**2 
A8 = A4**2  

print(f"A = {A}")
print(f"A**2 = {A2}")
print(f"A**4 = {A4}")
print(f"A**8 = {A8}")

# 28. A soni berilgan. A ning A**2, A**4, A**10, A**15 darajalarini aniqlovchi programma tuzilsin.
# A = 2 # Misol uchun

A2 = A * A
A4 = A2 * A2
A8 = A4 * A4 
A10 = A8 * A2 
A15 = A10 * A4 * A  
A15 = A**15

print(f"A = {A}")
print(f"A**2 = {A2}")
print(f"A**4 = {A4}")
print(f"A**10 = {A10}")
print(f"A**15 = {A15}")