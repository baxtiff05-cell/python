import math

# Foydalanuvchidan sonlarni olish
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

# Manfiy emasligini tekshirish
if a < 0 or b < 0:
    print("Iltimos, manfiy bo‘lmagan son kiriting!")
else:
    g = math.sqrt(a * b)
    print(f"O‘rta geometrik: {g}")


    # Foydalanuvchidan A, B, C ni olish
A = float(input("A nuqtani kiriting: "))
B = float(input("B nuqtani kiriting: "))
C = float(input("C nuqtani kiriting: "))

# C nuqta A va B orasida joylashganini tekshirish
if not (min(A, B) < C < max(A, B)):
    print("C nuqta A va B orasida joylashgan bo‘lishi kerak!")
else:
    AC = abs(C - A)
    BC = abs(B - C)
    natija = AC * BC
    print(f"AC = {AC}, BC = {BC}")
    print(f"AC * BC = {natija}")

    # Foydalanuvchidan A sonini olish
A = float(input("A sonini kiriting: "))

# Hisoblash
A2 = A ** 2
A4 = A ** 4
A8 = A ** 8

# Natijani chiqarish
print(f"A^2 = {A2}")
print(f"A^4 = {A4}")
print(f"A^8 = {A8}")