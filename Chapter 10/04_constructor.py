class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Tia = Employee("Tia", 1300000, "JavaScript") 
# Tia.name = "Tia"
print(Tia.name, Tia.salary, Tia.language)
# pia = Employee("pia", 1300000, "JavaScript") 
# # Tia.name = "Tia"

# print(pia.name, pia.salary, pia.language)



# rohan = Employee()






















