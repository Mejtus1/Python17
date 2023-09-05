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

#Funtions 
#function is a block of code that only runs when it is called
#Python has many build in functions:
#type(4) = int 
#len([1,2,3]) = 3
#sum([1,2,3]) = 1+2+3=6
#float(6) = 6.0
#print("Hello World") = "Hello World"

#Defining function 
    def function_name(input_parameters)
        body of the function
        return output 
#We use functions because they cen be reused many times and automate tasks 

def max_function(a,b):
    if a>b
        Max = a
    else:
        Max = b
    return Max
max_function(5,7) #7
max_function("A","B") #B

#Methods 
#Methods function the same way as functions but they are a little bit different 
#They are a set of procedures for interacting with the data in an object
#sorted(L) = function 
#L.sort = method 

#Libraries

#Scientific Computing Libraries:
#Pands(data structure and tools)
#NumPy(arrays and matrices)
#SciPy(integrals, solving differential equations, optimization)

#Visualization Libraries:
#Matplotlib(most popular for plots and graphs)
#SeaBorn(heat maps, time series and violin plots)

#Algorithmic Libraries:
#Scikit-learn(tools for statistical modeling: regression, classification, clustering)
#StatsModels(explore data, estimate statistical models and perform statistical tests)
