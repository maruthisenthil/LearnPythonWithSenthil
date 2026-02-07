#Python   Practice Exercises
#1: Print "Hello, World!" to the console.
print("Hello, Senthil!");
#2: Create a variable called 'name' and assign it your name. Then print "Hello, [name]!".
name = "Senthil"
print("Hello, " + name + "!");

employee_id = 12345
print("Employee ID:", employee_id)
employee_name ="Senthil Kumar"
print("Employee Name:", employee_name)
employee_age = 30
print("Employee Age:", employee_age)
employee_salary = 75000.50
print("Employee Salary:", employee_salary)
employee_isActive  = True

#3 Print the data type of the variable 'name'.
print('Print the type of the data ')
print(type(name));
print(type(employee_id))
print(type(employee_name))
print(type(employee_age))
print(type(employee_salary))
print(type(employee_isActive))

#print("The name of the employee is " + employee_name + " and his employee id is " + str(employee_id) + " and his age is " + str(employee_age) + " and his salary is " + str(employee_salary) + " and his active status is " + employee_isActive) // This line will cause an error because employee_isActive is a boolean and cannot be concatenated with a string directly. We need to convert it to a string first.   

#print("Age "+employee_age) // This line will cause an error because employee_age is an integer and cannot be concatenated with a string directly. We need to convert it to a string first.
