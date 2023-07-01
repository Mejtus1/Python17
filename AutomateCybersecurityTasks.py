# Create a Basic Python script 
# Hashes are used in python for comments 

#print - outputs a specified object to a screen 
print("Hello, Python")


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#DATA TYPES IN PYTHON 

#Strings 
#Data consisting of an ordered sequence of characters
#letters, symbols, spaces or numbers (numbers cannot be used in calculations)
#strings need to be inside quoation marks ""
print("hello python")

#Float data
#Data consisting of a number with a decimal point 
# 2.1 10.1 10.00

#Integer data 
#data consisting of a number that does not include a decimal point 
# 1, 48 , 12478514

print(1 + 1)#calcualtion with print 

#boolean data
#Data that cen only be one of two values - true or false
print(10<5)
print(9<12) #Determine boolean values 

#List Data
#Data structure that consists of a collection of data in sequantial form 
print(["dtanaka", "mabadi", "aestrada"]) #(like arrays in JS)


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
# Work with variables in python 
# creating variables is called assigment 
# we can reassign a variable whenever we want 
device_id = "hb2r17"
device_id = "145236hre" #reassign
print(device_id)
#we can ask python to tell us a data type of our variable
data_type = type(device_id)
print(data_type) #python tells us it is a string (str)

#Type error 
#an error that results from using the wrong data type 
number = 3
print(number + device_id) #throws type error
#python cannot combine two different data types



#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Conditional statements in python 
