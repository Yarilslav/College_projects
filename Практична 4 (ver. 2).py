#Створити функцію яка приймає список [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда'].
#Ця функція видаляє всі елементи які повторюються  та повертає список без повторень.
#створюєм функцію яка на вхід буде приймати наш список без повторень та сортувати його.
#Сортування відбувається від найменшого до найбільшого якщо є типи данних типу Str їх 
#в алфавітному порядку встановити після цифр в томуж самомому списку.



#---------------------------------------------------------------------------------------------------------
list0 = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
print("першопочатковий сипсок", list0)
#---------------------------------------------------------------------------------------------------------



#------ Функція для видалення повторень ------------------------------
def remove_duplicates(list0):
    seen = set()
    return [x for x in list0 if x not in seen and not seen.add(x)]
#---------------------------------------------------------------------



#----- Функція сортування --------------------------------------------
def sort_list(list0):
    # Розділяємо числа та рядки
    numbers = sorted([item for item in list0 if isinstance(item, (int, float))])
    strings = sorted(
        [item for item in list0 if isinstance(item, str)], 
        key=lambda x: (x.lower(), x)                                      #x.lower(): Рядки порівнюються без урахування регістру (тобто "Привіт" і "привіт" будуть вважатися однаковими).
    )
    
    # Повертаємо об'єднаний список
    return numbers + strings
#----------------------------------------------------------------------



#-------- Видаляємо повторення ----------------------------------------
list1 = remove_duplicates(list0)
print("Список без повторень:", list1)

#-------- Сортуємо список ---------------------------------------------
list2 = sort_list(list1)
print("Відсортований список:", list2)

#----------------------------------------------------------------------