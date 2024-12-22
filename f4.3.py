# From Chapter 03


# Example 1 - Introduction to Classes
class Bin:
    my_data_member = "Hello!"

    def my_member_function(self):
        print("This is my member function.")


# Declaring a variable of MyClass
my_object = Bin()
my_object.my_member_function()
my_object.my_data_member


# Example 2 - Object Creation
class MyClass:
    my_data_member = None

    def my_member_function(self):
        print("This is my member function.")


my_object = MyClass()
# Access the data member and call the member function of my_object
my_object.my_data_member = "Hello, World!"
my_object.my_member_function()


# Example 3 - Data Members
class Student:
    # Data members
    student_id = 0
    student_name = "Bin"


# Creating Object
student = Student()
print(student.student_id)
print(student.student_name)


# Example 4 - Member Functions
class Student:
    # Data members
    student_id = 0
    student_name = ""

    # Member Function
    def display_student_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.student_name)


# Creating an instance of the Student class
student = Student()
student.student_id = 970
student.student_name = "siMobin"
student.display_student_info()


# Example 5 - Self Keyword
class MyClass:
    def Test(self, value):
        self.value = value

    def print_value(self):
        print(self.value)


# Creating an instance of MyClass
obj = MyClass()
obj.Test(34)
# Accessing an instance variable and calling a method using "self"
obj.print_value()


# Example 6 - Constructors
class MyClass:
    def __init__(self):
        self.my_data_member = None

    def my_member_function(self):
        print("This is my member function.")


my_object = MyClass()  # Creating an object of MyClass with a constructor
# Accessing the data member and calling the member function of my_object
my_object.my_data_member = "Hello, World!"
my_object.my_member_function()


# Example 7 - Parametrized Constructor
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print("A new car has been created!")

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"


my_car = Car("Audi", "A4", 2020)
print(my_car.get_descriptive_name())


# Example 8 - Destructor
class Car:
    def __init__(self):
        print("A new car has been created!")

    def __del__(self):
        print("The car is about to be destroyed!")


my_car = Car()


# Example 9 - Inheritance
class Vehicle:
    def start(self):
        return "The vehicle is starting."

    def stop(self):
        return "The vehicle is stopping."


class Car(Vehicle):
    def drive(self):
        return "The car is driving."


car = Car()
print(car.start())
print(car.drive())
print(car.stop())


# Example 10 - Polymorphism
class Math:
    def add(self, x, y, z=0):
        return x + y + z


m = Math()
print(m.add(1, 2))  # 3
print(m.add(1, 2, 3))  # 6


# Example 11 - Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks.")


class Dog(Animal):
    def speak(self):
        print("Dog barks.")


a = Animal()
a.speak()  # Animal speaks.

d = Dog()
d.speak()  # Dog barks.
