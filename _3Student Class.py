class student:

    def __init__(self,name,rollnumber):
        self.__name=name
        self.__rollnumber=rollnumber

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name


    def get_rollnumber(self):
        return self.__rollnumber

    def set_rollnumber(self,rollnumber):
        self.__rollnumber=rollnumber



std=student('Dinesh',24)
print(std)
print(std.get_name())