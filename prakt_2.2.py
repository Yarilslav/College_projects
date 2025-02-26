from datetime import datetime

#--------------- Основний Клас --------------------------------------
class Yaroslav:
    def __init__(self, first_name=None, last_name=None, birth_year=None): 
        self.first_name = first_name 
        self.last_name = last_name
        self.birth_year = birth_year
    
    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = datetime.now().year
        age = current_year - self.birth_year
        return max(1, min(4, age - 15)) if age >= 15 else None
    
    def get_name_list(self):
        return [self.first_name, self.last_name] if self.first_name and self.last_name else []
    
    def get_birth_year(self):
        return self.birth_year


# ------------- Дочірній клас --------------------------------------------------
class Yaroslav2(Yaroslav):
    def __init__(self, first_name=None, last_name=None, birth_year=None, group=None, major=None, student_id=None):
        super().__init__(first_name, last_name, birth_year)  # Використання " super().__init__() "  для наслідування полів
        self.group = group     
        self.major = major          
        self.student_id = student_id


    def get_full_info(self):
        
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "Курс": self.calculate_course(),
            "група": self.group,
            "Спеціальність": self.major,
            "ID студента": self.student_id
        }
    
    def can_graduate(self):
        #Перевіряє, чи студент може випуститися (курс 4 і має ID):
        return self.__protected_method()  # __protected_method()  -  Приватний метод, який не можна викликати напряму.

    def __protected_method(self):
        return self.calculate_course() == 4 and self.student_id is not None


# ---------------- Використання ----------------
student = Yaroslav2("Ярослав", "Процюк", 2008, "22-ІСТ","ІСТ", "11223344")
 
print("Повна інформація:", student.get_full_info())  
print("Чи може випуститися?", student.can_graduate()) 
