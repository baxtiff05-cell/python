# # For14
# # n butun soni berilgan (n > 0). Shu sonning kvadratini quyidagi formula asosida hisoblovchi programma tuzilsin.
# # n^2 = 1 + 3 + 5 + ... + (2n - 1)
# n = int(input("n = "))
# s = 0
# for i in range(1, n + 1):
#     s += 2 * i - 1
#     print(f"{i}^2 = {s}")

# # For15
# # n butun soni va a haqiqiy soni berilgan (n > 0). a ning n-darajasini aniqlovchi programma tuzilsin.
# a = float(input("a = "))
# n = int(input("n = "))
# natija = 1
# for i in range(n):
#     natija *= a
# print("Natija:", natija)

# # For16
# # a ning 1 dan n gacha bo‘lgan barcha darajalarini chiqaruvchi programma tuzilsin.
# a = float(input("a = "))
# n = int(input("n = "))
# daraja = 1
# for i in range(1, n + 1):
#     daraja *= a
#     print(f"a^{i} =", daraja)

# # For17
# # 1 + a + a^2 + ... + a^n yig‘indisini hisoblovchi programma tuzilsin.
# a = float(input("a = "))
# n = int(input("n = "))
# yigindi = 1
# daraja = 1
# for i in range(1, n + 1):
#     daraja *= a
#     yigindi += daraja
# print("Yig‘indi =", yigindi)

# # For18
# # 1 - a + a^2 - a^3 + ... + (-1)^n * a^n yig‘indisini hisoblovchi programma tuzilsin.
# a = float(input("a = "))
# n = int(input("n = "))
# yigindi = 1
# daraja = 1
# for i in range(1, n + 1):
#     daraja *= a
#     if i % 2 == 1:
#         yigindi -= daraja
#     else:
#         yigindi += daraja
# print("Yig‘indi =", yigindi)

# # For19
# # n! (faktorial) ni hisoblovchi programma tuzilsin.
# n = int(input("n = "))
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print(f"{n}! =", f)

# # For20
# # 1! + 2! + 3! + ... + n! yig‘indisini hisoblovchi programma tuzilsin.
# n = int(input("n = "))
# f = 1
# yigindi = 0
# for i in range(1, n + 1):
#     f *= i
#     yigindi += f
# print("Yig‘indi =", yigindi)

# # For21
# # 1 + 1/1! + 1/2! + 1/3! + ... + 1/n! yig‘indisini hisoblovchi programma tuzilsin.
# n = int(input("n = "))
# yigindi = 1
# f = 1
# for i in range(1, n + 1):
#     f *= i
#     yigindi += 1 / f
# print("Yig‘indi =", yigindi)

# # For22
# # 1 + x + x^2/2! + x^3/3! + ... + x^n/n! yig‘indisini hisoblovchi programma tuzilsin.
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = 1
# p = 1
# f = 1
# for i in range(1, n + 1):
#     p *= x
#     f *= i
#     yigindi += p / f
# print("Yig‘indi =", yigindi)

# # For23
# # x - x^3/3! + x^5/5! - ... + (-1)^n * x^(2n+1)/(2n+1)! yig‘indisini hisoblovchi programma tuzilsin.
# import math
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = 0
# for k in range(n + 1):
#     yigindi += ((-1)**k) * (x**(2*k + 1)) / math.factorial(2*k + 1)
# print("Yig‘indi =", yigindi)

# # For24
# # 1 - x^2/2! + x^4/4! - ... + (-1)^n * x^(2n)/(2n)! yig‘indisini hisoblovchi programma tuzilsin.
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = 0
# for k in range(n + 1):
#     yigindi += ((-1)**k) * (x**(2*k)) / math.factorial(2*k)
# print("Yig‘indi =", yigindi)

# # For25
# # x - x^2/2 + x^3/3 - x^4/4 + ... + (-1)^(n-1) * x^n / n yig‘indisini hisoblovchi programma tuzilsin.
# x = float(input("x = "))
# n = int(input("n = "))
# yigindi = 0
# for k in range(1, n + 1):
#     yigindi += ((-1)**(k - 1)) * (x**k) / k
# print("Yig‘indi =", yigindi)
