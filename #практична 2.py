#практична 2. порівняти ім'я та прізвище, якщо вони однакового типу даних, 
#то вивести цей тип даних; створити список в якому через пробіл буде ім'я і прізвище, якщо тип даних віку - int, тоді порівняти і вивести цей тип.


#-----------------------------------------------------------------------------
print("ім'Я:")
name1 = input()
print("Прізвище:")
name2 = input()

if type(name1) == type(name2) :
    print("тип ім'я та прізвища:", type(name1), type(name2))
else:
    print("тип ім'я та прізвища не збігається")
    

print("---------------------------------------------------------------")
#-----------------------------------------------------------------------------
#друга частина завдання 

list = ["ᚾᚨᛗᛖ ᛋᚢᚱᚾᚨᛗᛖ 20"]
for abd in list:
    name3, surname, age = abd.split()

    print(f"name: {name3}, surname: {surname}, age: {age}") 
    
    print("age = int?")
    if isinstance(age, int):
        print("true,", type(age))
    else:
        print("false,", type(age))

