class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("addition :",self.num1+self.num2)

    def subtract(self):
        print("subtraction:",self.num1-self.num2)

    def multiply(self):
        print("multiplication:",self.num1*self.num2)

    def divide(self):
        print("division:",self.num1%self.num2)



obj=Calculator(10,94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()