#STRING OPERATORS 
#str() function = converts the input object into a string 
new_string = str(123)
print(type(new_string)) #class string 

#len() function = tells us how many characters are in an object
# returns the number of elements in an object 
print(len("Hello")) # 5 = each for one letter in the word

#string concatenation 
print("Hello" + "world") #Helloworld

#String methods
# a method is a function that belongs to a specific data type 
# common string methods are .upper and .lower
# .upper() returns a copy of string in uppercase letters
print("Hello".upper()) #HELLO 
print("Hello".lower()) #hello


#String indices and slices

#index is number assigned to every element in a sequence that indicates its position
"Hello" # H = index 0, E = index 1 ....
"Hello"[1] # outputs "E"

#We can extract a larger part of a string by specifing more indices 
#it is called SLICE 
"Hello"[1:4] #starts at 1 ands at 3 (output is "ell")

#.index() method
#finds the first occurrence of the input in a string and returns its location 
#exercise
#we want to find the letter E in Hello string 
print("HELLO".index("E")) #STRINGS IN PYTHON ARE CASE SENSITIVE
#returns 1 because E has a index number of 1
print("HELLO".index("L")) #2
#method only identifies the first occurence in "HELLO" and not the second

#Strings are immutable 
#meaning we cannot make changes like this 
my_string = "Hello"
my_string[1] = "A" #error = strings cannot be changed like this 
