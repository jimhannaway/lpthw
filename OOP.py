## CLASSES AND INSTANCES
## PYTHON OOP TUTORIALS - Working with classes by COREY SCHAFER
## https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

class Employee:

    # CLASS VARIABLES for the no of employees and pay raise amount
    no_of_emps = 0
    raise_amount = 1.04

    # METHODS within each class begin with def, __init__ and end with :
    def __init__(self, first, last, pay):
        # INSTANCE VARIABLES can vary for each instance of the class eg name, surname, email
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        Employee.no_of_emps += 1

    # INSTANCE to return an employee's full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # INSTANCE to apply a raise to a single employee
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # CLASS METHODS begin with @classmethod then on next line, def, cls and end with :
    # This CLASS METHOD sets a new class level raise amount, class variable is updated.
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Creating an 'ALTERNATIVE CONSTRUCTOR' using class methods to pull out employee details from hyphenated string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Creating a STATIC METHOD using the @static decorator
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # Creating SPECIAL METHODS or DUNDER METHODS (dunder = double underscore )
    # Special method returns employee name and pay details
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # Special method returns employee fullname hypenated and email address
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # Special method returns sum of two employee pay values
    def __add__(self, other):
        return self.pay + other.pay

    # Special method returns employee name character length
    def __len__(self):
        return len(self.fullname())


# CLASS INHERITANCE - Developer class inherits from Employee.
# Employees who are developers are getting their own raise set here.
class Developer(Employee):
    raise_amount = 1.1
    # Employee class variables inherited from 'super()' and we add in prog_lang separately.
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
##      Employee.__init__(self, first, last, pay) # this statement same as super() but maybe less flexible.
        self.prog_lang = prog_lang

# More CLASS INHERITANCE - Manager class inherits from Employee.
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # METHOD (function) to add employees to manager's list
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # METHOD (function) to remove employees from manager's list
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # METHOD (function) to print employees in manager's list
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


# PROPERTY DECORATORS EXAMPLE - GETTERS, SETTERS & DELETERS
# USING AN EDITED COPY OF EMPLOYEE CLASS FOR THIS DEMONSTRATION
class EmployeeDecorator:
    """docstring for EmployeeDecorator."""

    def __init__(self, first, last):
        self.first = first
        self.last = last
## removed   self.email = first + "." + last + "@email.com"

# INSTANCES in DECORATOR example to return an employee's email
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    # INSTANCE in DECORATOR example to return an employee's full name
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete", self.fullname)
        self.first = None
        self.last = None


# Creating ATTRIBUTES for CLASS INSTANCES
emp_1 = Employee('Jim', 'Twoglass(Jr)', 49000)
emp_2 = Employee('Test', 'User(Snr)', 65000)

# Employee ATTRIBUTES to be parsed by CLASS METHOD 'from_string'
emp_str_1 = 'John-Dee-70000'
emp_str_2 = 'Stevie-Oh-60000'
emp_str_3 = 'Feeahno-Choo-75000'
new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)

# CLASS INHERITANCE, create instances for developer...note no extra code
dev_1 = Developer('Jim', 'Twoglass', 50000, 'Python')
dev_2 = Developer('Test', 'User', 40000, 'Java')
mgr_1 = Manager('Suzy', 'Smith', 90000, [ emp_1, emp_2, dev_1, new_emp_1, new_emp_2, new_emp_3])
mgr_1.add_emp(dev_2) # Only one manager for all so add in the second developer to the list


# employee count is maintained in a CLASS VARIABLE 'no_of_emps' in the Employee class
print("No of employees (class variable) =", Employee.no_of_emps)

# Call the METHOD 'print_emps' to show the employee list
print("The list of employees who are not managers.")
mgr_1.print_emps()
## print(Employee.fullname(emp_1)) ## these two demos removed, replaced by 'print_emps' method.
## print(emp_2.fullname())

# Print the pay details for emp_1
print(f"This shows the old pay, before class level rise for {emp_1.fullname()}.")
print(emp_1.pay)
emp_1.apply_raise()
print(f"This shows the new pay, after class level rise of {emp_1.raise_amount}.")
print(emp_1.pay)

print("This is Employee class level raise inherited by emp_1 and emp_2")
print("Class level rise set at", Employee.raise_amount) # attribute comes from the class variable
# Instances emp_1 & emp_2 inherit the attribute raise_amount from the class variable
print("Class rise for emp_1 is", emp_1.raise_amount)
print("Class rise for emp_2 is", emp_2.raise_amount)
print("\n")

# class namespace contains raise_amount while emp_1 instance namespace does not.
print("Printout of NAMESPACES for Employee class and all employees follows: \n")
print(Employee.__dict__)
print("\n")
print(emp_1.__dict__)
print(emp_2.__dict__)
print(dev_1.__dict__)
print(dev_2.__dict__)
print(new_emp_1.__dict__)
print(new_emp_2.__dict__)
print(new_emp_3.__dict__)
print(mgr_1.__dict__)
print("\n")

# Amending raise_amount for a specific instance is still possible because
# self.pay = int(self.pay * self.raise_amount) rather than
# self.pay = int(self.pay * Employee.raise_amount) this can be seen as...
emp_1.raise_amount = 1.05
print("Raise has been amended for a single employee")
print("Class level rise still at", Employee.raise_amount) # attribute comes from the class variable
print("Personal rise for emp_1 is now", emp_1.raise_amount) # attribute has been set for this instance
print("Class rise for emp_2 is", emp_2.raise_amount) # attribute comes from the class variable
## print(Employee.__dict__)
## print(emp_1.__dict__)
# Note: we could not do this using self.pay = int(self.pay * Employee.raise_amount)
# as the class variable always sets the raise_amount for each instance. We have some flex therefore!
print("\n")


# CLASS METHODS & STATIC METHODS
Employee.set_raise_amt(1.06)
print("Now changing class level raise using @classmethod 'set_raise_amount'.")
print("Class level rise now at", Employee.raise_amount) # all attributes come from the class method set_raise_amt
print("Personal rise for emp_1 remains at", emp_1.raise_amount)
print("Class rise for emp_2 changes to", emp_2.raise_amount)
print("\n")

# print out values from @classmethod 'from_string'
print("Remember here, another @classmethod 'from_string' was used earlier to create employees.")
print(new_emp_1.email, "was created from 'John-Dee-70000' using @classmethod 'from_string'.")
print("And this pay level of", new_emp_1.pay, "was also derived using the 'from_string'@classmethod.")
print("\n")

# Demonstrate use of the static method 'is_workday'for identifying workdays

import datetime
my_date = datetime.date(2020, 7, 10)
print("Simply demonstrating @staticmethod 'is_workday'", my_date, "a workday? = ",Employee.is_workday(my_date))
print("\n")


# Demonstrate inheritance of Developer class from Employee class
print("Now for inheritance!")
print("Dev_1 prog_lang is set by the Developer class =", dev_1.prog_lang)
print("Dev_1 inherits email address from Employee class as:",dev_1.email)
print("Dev_1 inherits pay from super() of Employee class as:", dev_1.pay)
dev_1.apply_raise()
print("Now employee dev_1 has Developer.pay applied using Employee method 'apply_raise'.")
print("This passes the value", Developer.raise_amount, "from Developer to Employee.apply_raise.")
print(f"{Employee.fullname(dev_1)} new pay is now {dev_1.pay}.")
print("\n")

print("The manager of the team is", mgr_1.email, "this address is inherited from the Employee class.")
print("Calling the Manager class 'print_emps' method which inherits fullname from the Employee class.")
mgr_1.print_emps()
print("\n")
print("Now remove employee", dev_1.fullname(), "using Manager class method 'remove_emp' from the list and reprint the list.")
print("\n")
mgr_1.remove_emp(dev_1)
print(mgr_1.email)
mgr_1.print_emps() # new list with employee dev_1 removed
print("\n")

# Print help on the Developer class follows in next line. Very useful for debugging.
## print(help(Developer))

# isinstance shows if an object is instance of a class
print("The 'isinstance' & 'issubclass' methods show useful class/instance inheritance information.")
print("Is mgr_1 an instance of Manager =", isinstance(mgr_1, Manager)) # True
print("Is mgr_1 an instance of Employee =", isinstance(mgr_1, Employee)) # True
print("Is mgr_1 an instance of Developer =", isinstance(mgr_1, Developer)) # False. Developer and Manager inherit from Employee, not each other.
print("\n")
#issubclass function tells us if a class is a subclass of another.
print("Is Developer a subclass of Employee =", issubclass(Developer, Employee)) # True
print("Is Manager a subclass of Employee =", issubclass(Manager, Employee))  # True
print("Is Manager a subclass of Developer =", issubclass(Manager, Developer))  # False
print("Is Developer a subclass of Manager =", issubclass(Developer, Manager))  # False
print("\n")
# *******  Exceptions Handling, quick lesson. Commented out. *****
## import sys
## print("Lets fix the previous code with exception handling.")

## try:
##     number = int(input("Enter a number between 1 - 10 "))

## except ValueError:
##     print("Err.. numbers only")
##     sys.exit()

## print("you entered number", number)
## **************************************************************

# demonstrating use of dunder methods.
print("A quick demonstration of magic/dunder methods.")
print("This is the __repr__ method printout:", repr(emp_1))
print("This is the __str__ method printout:", emp_1)
print("No of chars in employee name, pulled from __len__ method =:", len(emp_1))
print("This is the __add__ method, summing emp_1 and emp_2 pay =", emp_1 + emp_2)

# Dunder repr and str also be printed directly using the following code statements:
## print(repr(emp_1))  or  print(emp_1.__repr__())
## print(str(emp_1))  or   print(emp_1.__str__())
print("\n")
print("Quick demo of __add__ for integer addition and string addition.")
print("int.__add__(1,2) = ",int.__add__(1, 2))
print("str.__add__('a', 'b') = ",str.__add__('a', 'b'))
print("\n")

# Demonstrating use of setters, getters & deleters
print("Demonstrating Decorators: Adding a new employee Johnny Walker using the EmployeeDecorator class.")
emp_1 = EmployeeDecorator("Johnny", "Walker")
emp_1.first = "Jamsie"
print("Then realise a mistake that his name is Jamsie Walker, so change the first name at instance level only.")
print("-->", emp_1.first)
# note demonstration now hard coded as inserted @property code on def mail in EmployeeDecorator class.
print("--> Johnny.Walker@email.com")
print("--> Jamsie Walker")
print("Result is first and fullnames are correct but not the email!")
print("This is because the fullname method uses the class level first name which we haven't changed.")
print("We need to automatically update the email address each time first or last name is changed.")
print("\n")
print("So we remove the email creation from within EmployeeDecorator initial class statement.")
print("Then create a new email instance within EmployeeDecorator to create the email. And then changing first name to Jamsie gives:")
print("-->", emp_1.first)
print("Using @property on email instance we can code: print('-->', emp_1.email) rather than print('-->', emp_1.email()). Note bracket removal!")
print("-->", emp_1.email)
print("Using @property on fullname means we can code: type print('-->', emp_1.fullname) rather than print('-->', emp_1.fullname())")
print("-->", emp_1.fullname)
print("Everything is now as it should be for this employee first name being changed. \n")

print("Resetting emp_1 fullname to Corey Shafer and printing out the namespace shows use of @setter.")
emp_1.fullname = "Corey Shafer"
print(emp_1.__dict__)
print("Deleting emp_1 fullname Corey Shafer and printing out the namespace shows use of @deleter.")
del emp_1.fullname
print(emp_1.__dict__, "\n")
print("Both Jamsie and Corey are no longer associated with emp_1.")
print("\n")
