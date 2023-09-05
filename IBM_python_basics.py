#Describe the basic syntax of Python 
#in Python needs to be same number of spaces in a code block

a_variable = 1
A_variable = 2
print (a_variable, A_variable) #1,2
#variable names are case sensitive

#Data types in Python 
#Data type is set when we assign value to a variable
#   int   Integer numbers   -1, 17, 26
#   float   Real numbers    3.14, 1.23,
#   complex Complex numbers 3+4j, 5.0+4.1j,
#   bool    Boolean values  True, False
#   str     string characters   "", "Hey"

number = 3
type(number) #int 

float(number)
type(number)

number = float(number)
print(type(number)) #class "float"
print(number) #3.0

string = "Hello World!"
int(string) #ValueError

#String operations 
#                       P  Y  T  H  O  N 
#indexing               0  1  2  3  4  5
#negative ingexing     -6 -5 -4 -3 -2 -1

#Python Arithmetical Operations
#   +   Addition      10+12
#   -   Subtraction    5-1
#   *   Multiplication 5*1
#   /   Division       10/5
#   //  Int Division   9//4
#   %   Modulation     9 % 4

#Python comparison operators
#   ==  Equal to
#   !=  Inequal to
#   <   Less than
#   <=  Less than or equal to
#   >   Greather than
#   >=  Greater than or equal to 

#Data Structures
#Touple = an immutable sequence of objects (), (1,2,3), ("Python", 3)
#List = a mutable sequence of objects [], [1,2,3], ["Hello", "World"]
#Set = an mutable/immutable unordered set of unique items {1,2,3}  {"World", "Hello"}
#Dicitonary = a mutable and not ordered collector {},{"name":"Ezio","surname":"Melotti"}
#           = a key value pair 

#Conditions and Branching
#If, elif, else
#To trigger a command, given a certain condition, we can use if, elif, else statements:
#
# If = establishes the first condition
# Elif = is used when many conditions are possible 
# Else = will execute its command if none of the if and elif conditions were met 

Print("Hello")
if name == "Antonio":       #Hello!
    print("It is Antonio")  #it is Antionio
print("How are you?")       #How are you? 

print("a=",a)
if a > 0:
    print("a is positive")
elif a<0:
    print("a is negative")
else:
    print("a is zero")
print("This will be printed in any case")

#For loops 
L = ["Red", "Blue", "Yellow"]
print(L[0]) #"Red"
print(L[1]) #"Blue"

N = len(L)
for i in range(N):
    print(L[i])
]
#While loops 
L = [1, 0, 6, 8, 4, -3, 7, 5, -1]

i=0
while (L[i]>=0):
    print(L[i])
    i=i+1
