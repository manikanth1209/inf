# Operator overloading in Python allows you to define how operators behave for user-defined types (classes). This means you can redefine the behavior of operators like +, -, *, etc., for your own classes. This makes objects of these classes behave more like built-in types, enhancing readability and usability.
#
# # Here’s a detailed example to illustrate operator overloading in Python using a class that represents complex numbers:
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,other):
        return Complex(self.real-other.real,self.img-other.img)
    def __sub__(self,other):
        return Complex(self.real + other.real, self.img + other.img)

    def __str__(self):
        return f"{self.real} + {self.img}i"
c1=Complex(34,56)
c2=Complex(34,54)
c3=c1+c2

print(f"Addition: {c3}")