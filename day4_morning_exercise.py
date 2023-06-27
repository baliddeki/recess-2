# Exercise2: Convert temperature from degress Celcius to Fahrenheight


class Temperature:
    """program to convert from degree Celcus to Fahrenheight"""

    def __init__(self):
        self._temp = int(input("Enter the temperature to be converted: "))

    def convert(self):
        """method to convert celcius to fahrenheight"""
        fahren = (self._temp * (9 / 5)) + 32
        return fahren

    def get_fahren_temp(self):
        """method to return to new converted to temperature"""
        return self.convert()


tempObj = Temperature()
print(tempObj.get_fahren_temp())

print("-------------------------------------------------------------------------------")


# Assignment2: Show encapsulation with employee information to give a pay incrementation to give
# a pay incrementation (Salary with employee information to new_salary) eg from 850000 to 1000000


# Program to increase/decrease salary of employee
class EmployeeIncrement:
    """class constructor"""

    def __init__(self, employees):
        self.employees = employees
        print("The available employees current salaries are:")
        for key, value in employees.items():
            print(key, ":", value)
        self.employee_name = input(
            "Enter the name of employee to be increased salary: "
        )
        if self.employee_name in self.employees.keys():
            self.__salary = self.employees[self.employee_name]

        else:
            print("Employee not in the system. First register employee")

    def get_salary(self):
        """salary get method"""
        return self.__salary

    def set_salary(self, n_salary):
        """salary set method"""
        self.__salary = n_salary

    def change_salary(self):
        """method to change salary of employee"""

        # check if employee is in the system
        if self.employee_name in self.employees.keys():
            new_salary = input("Enter the new employee salary: ")
            print(self.employee_name, "new salary is", new_salary)

            # confirm salary change
            confirm = input("Type OK to confirm: ")
            confirm_to_upper = confirm.upper()
            confirm_stripped = confirm_to_upper.strip()

            # formatting confirmation input - capitalizing and removing white spaces
            if (confirm_stripped) == "OK":
                self.__salary = new_salary
                self.employees[self.employee_name] = new_salary
            else:
                print("Try again to change employee salary")
        else:
            print("Employee not in the system. First register employee")

    def print_new_salary(self):
        """method to print new salaries"""
        print("The available new employees current salaries are:")
        for key, value in self.employees.items():
            print(key, ":", value)


# dictionary of employees
employee = {
    "Aliddeki Bryan": 500000,
    "Nantume Stellah": 800000,
    "Nsereko Julius": 400000,
}

"""for key, value in employee.items():
    print(key, value)"""

empObj = EmployeeIncrement(employee)
empObj.change_salary()
empObj.print_new_salary()
