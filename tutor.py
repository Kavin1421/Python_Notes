"""
a = [1, 2, 3, 4]
for i in a:
    print(i)

for i in range(65, 70, 1):
    for j in range(65, 70, 1):
        print(chr(i), end="")
    print("")
print("---------------------")
for i in range(65, 70, 1):
    for j in range(65, 70, 1):
        print(chr(j), end="")
    print("")
print("---------------------")
# SETS
# Unorder and Unindex===>Sets
name = {"Kavin", 34, "Keetz", "Abdullah", "Balu"}
print(name)
print(type(name))
for i in name:
    print(i)
name.add(88)
print("****Before Updating****")
print(name)
name1 = {"Raj", "Kiruba", 23}
name.update(name1)
print("****After Updating****")
print(name)
name.remove(34)
print("****After Removing****")
print(name)
name.discard("Kavin")
print("****After Discarding****")
print(name)
# Pop fun will remove the last element but in set does'nt know
name.pop()
print("****After Poping****")
print(name)
name.add(25)
name.add(25)
print("****Duplicate****")
print(name)
# Union
a = {1, 2, 3}
b = {"a", "b", "c"}
print("Union")
c = a.union(b)
print(c)
a.update(b)
print("Update")
print(a)
# print(3<2)
# print(2<1)
# print(3>2>1)
# -------------------------------------------------------------------------------------------------------------------------------------
print("---------------------------------------------------------")
# Dict
user = {"Name": "Kavin", "Age": 23, "Ismarried": True}
print(user)
for i in user:
    print(user[i])

user = {
    "user1": {"Name": "Kavin", "Age": 23, "Ismarried": True},
    "user2": {"Name": "Raj", "Age": 21, "Ismarried": False},
}
print(user)
for i in user.values():
    print(i)

print("---------------------------------------------------------")
# 9 Types of Function
print("1.No Return Type Without Argument")


# def Kavin():
#     print("Balu Boys")
# Kavin()
# Kavin()
def add():
    a, b = 10, 20
    print(a + b)


add()

print("2.Return Type Without Argument")


def add():
    a, b = 10, 20
    # print(a+b)
    return a + b


print(add())

print("3.No Return tupe with Arguments")


def sub(a, b):
    print(a - b)


sub(4, 1)

print("4.Return tupe with Arguments")


def sub(a, b):
    # print(a-b)
    return a - b


print(sub(4, 1))

print("5.Arbitrary argument with Function ")


def MCA(*stu):
    return stu


# print(MCA('Kavin',23,'A-section')) ==>O/p in Tuple
main = MCA("Kavin", 23, "A-section")
for i in main:
    print(i)

print("6.Keyword Arguments function")


# def msg(name,age):
#     return(name,age)
# print(msg('Kavi',78))
def msg(name, age):
    print(name, "Age is", age)


msg("Kavi", 78)
msg(67, "Kiruba")
msg(age=67, name="Kiruba")
# we need to use double star (**)
print("7.Arbitrary Keyword with Arguments")


def bio(**data):
    print(data)


bio(name="Raj", age=20, gender="Male")


def bio(**data):
    for i in data:
        print(i, "=>", data[i])


bio(name="Raj", age=20, gender="Male")

print("8.Default Parameter Function")


def city(name, place="Hosur"):
    print(name, "lives in", place)


city("Kavin", "Dpm")
city("Kavin")

print("9.Passing List as a Argument")


def total(marks):
    return sum(marks)


print(total([1, 2, 3, 4, 5]))

print("9.Passing Tuple as a Argument")


def total(marks):
    return sum(marks)


print(total((9, 2, 3, 7, 5)))

print("----------------------------------------")
print("Recursive Function")
# for i in range(1,5):
#     print(i*(i-1))


def factorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return x * factorial(x - 1)


print(factorial(7))

print("Lambda Function")
c = lambda a: a + 50
print(c(5))
c = lambda a, b: a * b
print(c(5, 5))

print("---------------------------------------------------------")
# DateTime
import datetime as dt

ct = dt.date.today()
print("Current Date:", ct)
ct = dt.datetime.today()
print("Current Date and Time:", ct)

new = dt.date(2025, 9, 23)
print(new)
print("Year :", new.year)
print(new.month)
print(new.day)

cur = dt.datetime(2021, 8, 30)
ct = dt.datetime.today()
print(ct - cur)
s = ct.strftime("%A %B %d %Y")
print(s)
s = ct.strftime("%A %b %d %y %p => %w Days")
print(s)
print("---------------------------------------------------------")
# Math Package
import math as m

print(m.sqrt(25))
print(m.ceil(7.0175))
print(m.floor(7.878998))
print(m.factorial(5))
print(m.fabs(-7))
print(m.pow(5, 2))
print(m.log2(4))
print(m.log10(7))
print(m.pi)
print(m.e)
print("---------------------------------------------------------")
# Try Block
try:
    c = 8 / 2
except Exception as err:
    print("1.Zero Division Error =>", err)
else:
    print("C : ", c)
finally:
    print("Finished da Balu!!")
print("---------------------------------------------------------")
print("Types of Exceptions in Python")
# er=dir(locals()['__builtins__'])
# for i in er:
#     print(i)
print(len(dir(locals()["__builtins__"])))
print("2.Name Error Exception ==> ")
try:
    print(a)#Put aa here
except Exception as err:
    print("AA is Not Defined da Balu! ==> ", err)
print("---------------------------------------------------------")
print("3.value error Exception")
try:
    cs = int("lem")
except Exception as err:
    print("String Cannot Be Converted into the Int ==> ", err)
print("---------------------------------------------------------")
print("4.Index Error exception")
try:
    a = [1, 2, 3, 4]
    print(a[0])
    print(a[4])

except Exception as err:
    print("Array Index Out of Bound:", err)

print("---------------------------------------------------------")
print("5.File Not Found Error")
try:
    f = open("test.txt")
except Exception as err:
    print("File ilaye ! ", err)
else:
    print(f.read())

print("---------------------------------------------------------")
print("Handling Multiple Exception")
try:
    a = 10 / 9
    print(a)
    ak = [1, 2, 3, 4]
    print(ak[4])
except ZeroDivisionError:
    print("Zero")
except Exception as err:
    print("error in  Nagi Betta")

# Classes And Object
print("------------------------------------------------------------")


class Car:
    pass


swift = Car()  # Instance,swift is an Object
a = 10
print(type(a))
print(type(Car))
print(type(swift))
print(isinstance(swift, Car))
print(isinstance(a, int))
print("------------------------------------------------------------")
print("Class Attributes")


class Student:
    name = "Bhuvana"
    age = 19
    place = "Hosur"


# we can Access those class attributes in Two Methods (1.getattr,2.(.)dot operator)
# 1.Using getattr() method
print("Using getattr() ==> ")
print(
    getattr(Student, "name")
)  # 1st Argument=>Student is class,#2nd Argument=>name is attribute,#3rd Argument=>Optional it will executes that when the attributes not present in the class
print(getattr(Student, "age"))
print(getattr(Student, "place"))
print(getattr(Student, "mail", "Mail nu onu ila da Mendal"))
# 2.Using (.)dot Operator
print("Using Dot(.) ==> ")
print(Student.name)
print(Student.age)
print(Student.place)
# We can also update an create using setattr() method
setattr(Student, "name", "Keerthi")
print(Student.name)
setattr(Student, "gender", "Female")
print(Student.gender)
# We can also update an create using (.)operator
Student.name = "Bhuvi"
print(Student.name)
Student.college = "KASC"
print(Student.college)
# To view the Entire attributes in class
print(Student.__dict__)
# Deleting the attributes in class
delattr(Student, "college")
print(Student.__dict__)
del Student.gender
print(Student.__dict__)

print("---------------------------------------------------------")


# Instance attribute
class Course:
    sub1 = "Django"
    sub2 = "Flask"


ob1 = Course()  # Instance=class()
print(Course.__dict__)
print(ob1.__dict__)
print(ob1.sub1)
ob1.sub3 = "sql"
print(ob1.__dict__)
print(ob1.sub3)
# In instance attribute if we create or update an value in that class it will not be refelected in the original class coz it will create an own space and save it to its memory like dict format it could not affect the original class
print("---------------------------------------------------------")


# Class methods
# Accessing the methods inside the class without using the self keyword
class Home:
    father = "Kuppusamy"
    mother = "kalishwari"

    def fam_meb():
        print("Father is : ", Home.father)
        print("Mother is : ", Home.mother)


Home.fam_meb()  # Mostly used method
print(Home.__dict__)
print(getattr(Home, "fam_meb"))
getattr(Home, "fam_meb")()  # Calling the attributes inside the class

class Home:
    father = "Kuppusamy"
    mother = "kalishwari"

    def fam_meb(self,gender1,gender2):#Self is an Instance method with this we can directly call the the method using an object
        # we can pause an 1st Parameter as Class of an object should be paused
        # Python defaultly take "Self" as a First Argument
        print("Father is : ", Home.father)
        print("Mother is : ", Home.mother)
        print("Gender of Father is : ", gender1)
        print("Gender of Mother is : ", gender2)


o1 = Home()
# print(o1.father)
# o1.fam_meb() #Its an Mostly used one!!! #We can use this method 
# Home.fam_meb()
# Home.fam_meb(o1)  # Class.Object.Instance ===> Correct Procedure

o1.fam_meb("Male","Female")
# Home.fam_meb(o1,"Male","Female") # Class.Object.Instance,arguments

# Constructor!!!!
# print("__init__")#Inizializing of the Constructor in python
class Room:
    def __init__(self, charge):  # It will automatically called when the object is created!!
        # Mainly it is used for assigning the values for the class variables and instance variables in Runtime
        print("Bill uh kudukanum da Bro's")
        self.charge = charge # Instance attribute
    def selavu(self):
        print("Intha masam selavu : ",self.charge)

# ob1 = Room()
# ob2=Room()
# ob3=Room() 
ob1 = Room(4300)
ob1.selavu()
print(ob1.__dict__)
ob2 = Room(5000)
ob2.selavu()
print(ob2.__dict__)
# print(Room.__dict__)#The values could not stored in the class beacause it is an instance attribute that menas particular object attributes 


# Property Decorator
class Prands:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # self.msg=self.name+" age is "+str(self.age)+" years old!"
    @property #It converts the methods into  property
    def msg(self):
        return self.name + " age is " + str(self.age) + " years old!"


o1 = Prands("Rasu", 19)
print(o1.name)
print(o1.age)
print(o1.msg)
o1.age = 22
print(o1.msg)  
# print(o1.__dict__)

# Getter Setter using Property decorator Method!!!
print("Getter and Setter!! ====> Data Encapsulation")


class Dance:
    def __init__(self, dname):
        self._dname = dname  # _(name)=> private variable

    def Mem(self):
        return self._dname + " Kumar"

    @property
    def dname(self):
        return self._dname + " Raj"

    @dname.setter
    def dname(self, d):
        self._dname = d


o1 = Dance("Arun")
print(o1.dname)
print(o1.Mem())
o1.dname = "Kavin"
print(o1.dname)
print(o1.Mem())

print("===========================================")


class Student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 5

    def getter(self):  # Here getter is not an keyword we can use the any word!
        return self._total

    def setter(self, t):  # Similarly here setter is also an not a keyword we can use the any word!
        if t < 0 or t > 500:
            print("Invalid Total! Check the marks!!")
        else:
            self._total = t

    total = property(getter, setter)


o1 = Student(450)
print("Total   : ", o1.total)
print("Average : ", o1.average())
o1.total = 250
print("Total   : ", o1.total)
# print(o1.__dict__)
print("Average : ", o1.average())

# Class method Decorator


class Student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    def Details(self):
        print("Name : ", self.name, " || Age : ", self.age)
    @classmethod
    def times(cls):
        # print(Student.count,"Times Object Created!!")
        return cls.count


o1 = Student("Abdullah", 23)
o1.Details()
print(o1.times())
o1 = Student("Balaji S", 20)
o1.Details()
print(o1.times(),"Times Object Created!!")

# Static Method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Name:" , self.name + "  Age:", self.age)

    @staticmethod  # It is used to mainly run the method without using the self keyword!!
    def message(): 
        print("Vanakam!!!")
 

s1 = Student("Arun", 23)
s1.details()
s1.message()
s2 = Student("Kumar", 20)
s2.details()
s2.message()



# Abstraction ===> Abstraction is an process of the providing only  the essential details to the world and hiding
# the background details , to represent the needed information in program without presenting the details!!
# =========================================================================================
# Encaptulation is an wrapping upof code and data  together into the single unit !!


class Library:
    def __init__(self, books):
        self.books = books

    def list_books(self):
        print("Available Books!")
        for books in self.books:
            print(books)

    def borrow_books(self, borrow_books):
        if borrow_books in self.books:
            print("Books are:", borrow_books)
            self.books.remove(borrow_books)
        else:
            print("None of Books are Available")

    def received_books(self, received_books):
        if received_books not in self.books:
            print("You have returned book")
            self.books.append(received_books)
        else:
            print("Enter Valid Book Name!!")


books = ["c", "c++", "java", "python"]
o1 = Library(books)
# print(Library.__dict__)
msg = #'''
    1.Display Books
    2.Borrow books
    3.Return books
    #'''
while True:
    print(msg)
    ch = int(input("Enter your Choice : "))
    if ch == 1:
        o1.list_books()
    elif ch == 2:
        book = input("Enter the Borrowed Book Name :")
        o1.borrow_books(book)
    elif ch == 3:
        book = input("Enter the Returned Book Name :")
        o1.received_books(book)
    else:
        print("Invalid Option!!!")
        print("Thank You! For Visiting Us!!")
        exit()

# Single Inheritance
class Redmi:
    company = "Xiomi"
    website = "www.xiomi.com"
    contact = "+91 9343498983"

    def con_det(self):
        print("China Kuruku Santhu,Main Road!")


class RedmiNote7(Redmi):
    def __init__(self):
        self.name = "Redmi Note 7 "
        self.model = 2020

    def alldet(self):
        print("Comapant Name: " , self.name)
        print("Comapant model: " , self.model)
        print("Comapant company: " , self.company)
        print("Comapant website: " , self.website)
        print("Comapant contact: " , self.contact)


m1 = RedmiNote7() 
m1.alldet() 
m1.con_det() 



#Multiple Inheritance

class Father:
    fname="Kuppusamy"
    fage=51

class Mother:
    mname="Kalishwari"
    mage=45

class Son(Father,Mother):
    def __init__(self):
        self.sname="Kavin"
        self.sage=21
    def fdet(self):
        print(self.fname)
        print(self.fage)
    def mdet(self):
        print(self.mname)
        print(self.mage)
    def sdet(self):
        print(self.sname)
        print(self.sage)

s1=Son()
s1.fdet()
s1.mdet()
s1.sdet()



# Multilevel Inheritance!
class A:
    def dog(self):
        print("Barking Dogs")

    def cat(self):
        print("Seldom Bites")


class B(A):
    def lion(self):
        print("King of Forest")

    def tiger(self):
        print("Simply Waste !")


class C(B):
   
    def cow(self):
        print("Milk!!")

    def buf(self):
        print("Pure Milk!!")
 

o1 = C()
o1.cow()
o1.buf()
o1.lion()
o1.tiger()
o1.cat()
o1.dog()


# Function Overriding!!!
class Employee:
    def wrks(self):
        self.wrk = 50

    def show(self):
        print("Total working hrs are :", self.wrk, "hrs")


class Trainee(Employee):
    def wrks(self):
        self.wrk = 90

    def reset(self):
        super().wrks()


o1 = Employee()
o1.wrks()
o1.show()
o2 = Trainee()
o2.wrks()
o2.show()
# After Reset!!!!!
o2.reset()
o2.show()


#Dimond Problem 

class A:
    def dis(self):
        print("I'm Displaying from the Class ==> A")
class B(A):
    def dis(self):
        print("I'm Displaying from the Class ==> B")
class C(A):
    def dis(self):
        print("I'm Displaying from the Class ==> C")
class D(B,C):
    def dis(self):
        print("I'm Displaying from the Class ==> D")

d1=D()
d1.dis()


# polymorphism
# Operator Overloading


class Addition:
    def __init__(self, a):
        self.a = a

    def __add__(o1, o2):
        return o1.a + o2.a

    def __sub__(o1, o2):
        return o1.a - o2.a


o1 = Addition(10)
o2 = Addition(20)

print("Sum of Two Objects  :", (o1 + o2))
print("Diff of Two Objects :", (o1 - o2))

"""
"""
Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
 
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
 
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
 
Unary Operators :
Operator	Magic Method
-	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
 


# Abstract Base Class
from abc import ABC, abstractmethod


class Reserve_Bank:
    @abstractmethod
    def greet(self):
        pass

    @abstractmethod
    def loan(self):
        pass

    @abstractmethod
    def credit(self):
        pass


class HDFC(Reserve_Bank):
    def greet(self):
        print("Welcome to HDFC Bank")

    def loan(self):
        print("We Provude Loan Facility")

    def credit(self):
        print("We providing the Credit based Community")

    def Passbook(self):
        print("Passbook Recived")


class ICICI(Reserve_Bank):
    def greet(self):
        print("Welcome to ICICI Bank")

    def loan(self):
        print("We Provude Loan Facility with Low Interest")

    def credit(self):
        print("We providing the Credit based Community")

    def check(self):
        print("Checkbook Recived")


b1 = HDFC()
b1.greet()
b1.loan()
b1.credit()
b1.Passbook()
b2 = ICICI()
b2.greet()
b2.loan()
b2.credit()
b2.check()

"""
#File Handling
try:
    file=open('test.txt',"r")
    print(file.read())
except:
    print("Unable to fetch the file!!")

else:
    print("File readed successfully!!!")
    file.close()

finally:
    print("Avulothan")
