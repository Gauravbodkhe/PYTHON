# 39. Class Patient
class Patient:
    def __init__(self, name, disease):
        self.__name = name
        self.__disease = disease

    def get_details(self):
        return self.__name, self.__disease

    def update_disease(self, new_disease):
        self.__disease = new_disease

patient1 = Patient("David", "Flu")
print("Patient Details:", patient1.get_details())
patient1.update_disease("Recovered")
print("Updated Details:", patient1.get_details())