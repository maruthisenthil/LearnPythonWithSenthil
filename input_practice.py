# Get the input from the user and store it in a variable

#input() function is used to get the input from the user. It takes a string as an argument which is displayed as a prompt to the user. The input from the user is returned as a string.


user_name = input("Please enter your name: ")
print("Value entered by user " + user_name )
# print("Type of the value entered is : "+type(user_name)) // This line will cause an error because type(user_name) returns a type object and cannot be concatenated with a string directly. We need to convert it to a string first.
print("Type of the value entered is : "+str(type(user_name))) // This line will work because we are converting the type object to a string before concatenating it with the other string.


