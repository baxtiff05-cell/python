#string , metods , f "" string


ism = "Ali"
familya = "Valiyev"
ochestva = "Karimovich"
FIO = f"assalomu alaykum {familya} {ism} {ochestva}"
print(FIO.title())
print(f"assalomu aaykum {familya} {ism} {ochestva}!")

meva = 'anor , olma , shaftoli'
txt  = f"bobur  hello {meva} yisanmi "
x = txt.capitalize()
print(x)

#lower(), casefold() matndagi barcha katta harflarni kichik harflarga o'zgartiradi 
ism = 'Jamshidov Axmad '
txt = 'hello , and welcome my world!'
x = txt.casefold()
print(ism.lower())


#centr() string ma'lumotning  o'rtasiga bo'sh joy joylashtiradi
txt = "banana"
x = txt.center(150)
print(x)


#count() string ma'lumotda nechta ma'lum bir so'z yoki harff borligini hisoblaydi
txt = "I love apples , apple are my favourite fruit"
x = txt.count("a")
print(x)

#endwith() string ma'lumot ma'lum bir so'z bilan tugashini tekshiradi 
txt = "hello, welcome to my world."
x = txt.endswith("")
print(x)

#expantabs() string ma'lumotdagi tab belgilarini bo'sh joy bilan almashtiradi 
txt = "K/tamol/tbek"
x = txt.expandtabs(3)
print(x)

