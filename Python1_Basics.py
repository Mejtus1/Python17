# Python 
# Python excells in shell scripting task automation and web development 
# It can create games and work with embedded devices 
# It is also used in Data Analysis and Machine learning 
#You can use REPLIT to code and run programs in a web browser 

#Rock paper scissors game - VARIABLES IN PXTHON 
name = "Beau" #we created variable and assigned it value Beau
age = 39 #number
#variables can be capitale leaters, strings, underscore starts but IT CANNOT start with a number 
#there cannot be variables of python keywords (for, if, whiole, import)

#Expressions in python 
#any code that returns a value 
1 + 1 

#Statements in python 
#is an operation on a value, it is doing something to a value 
name2 = "Victoria" #statement
print(name2) #statement2

#COMMNETS 
# we use hash marks for comments 

#INDENTATION 
#in python indentation matters 
name3 = "Hey"
print(name3)
    print(name3) #here we have indentation error because of tap 


#DATA TYPES IN PYTHON 

#Strings
name = "Beau" #string data type 
print(type(name)) #class str = python outputs typo of this data type 
print(type(name) == str) # if name is equal using equality operator to string 
print(isinstance(name, str)) #if name is an instance of a string 

#Integer numbers 
#int = 1 
#float = 2.14

age = 2
print(isinstance(age, int)) #true age is integer 
ageFloat = 2.78
print(type(ageFloat) == float) #true ageFloat is float 

#we can convert data types in python 
ageIntFloat = float(2) #althrough 2 is integer we can assign it data type float 
print(isinstance(ageIntFloat, float)) #true because we assigned it data type float 

number = "test"
age2 = int(number)
print(isinstance(age, int)) #we cannot convert string to integer(number)
#Other types are 
# complex for complex numbers, 
# bool for booleans, 
# list for lists, 
# tuple for tuplets
# range for ranges 
# dict for dictionaries 
# set for sets



#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Operators 

#Arithmetic operators 
1 + 1 # 2
2 - 2 # 0
2 * 2 # 4
2 / 2 # 1
4 % 3 #remainder (how many are inside of given number) 1
4 ** 2 #exponents (4 to the power of 2 is 16) 16
5 // 2 #floor division (does division and rounds down to the nearest whole number)
# 2
1 + -1 # 0 (negative values)
print("Scamp" + " is a good dog") # plus sign (+) can be used to combine 
# plus sign (assignment operator) can be used also for adding syntax
age = 7
age += 7 #adds age = age + 7 
print(age) # 14
#this can be done with any of arithmetic operators 
year = 17
year *= 17 #multiplies year = year * 17
print(year)

#Comparison operators