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

#Exercises
device_id = "72e08x0"
print(device_id)

# Assign the `device_id` variable to the device ID that only specified users can access
device_id = "72e08x0"
# Assign `device_id_type` to the data type of `device_id`
device_id_type = type(device_id)
# Display `device_id_type`
print(device_id_type)
    
# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Display `username_list`
print(username_list)

# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Assign `username_list_type` to the data type of `username_list`
username_list_type = type(username_list)
# Display `username_list_type`
print(username_list_type)

# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Display `username_list`
print(username_list)

# Assign `max_logins` to the value 3
max_logins = 3
# Assign `max_logins_type` to the data type of `max_logins`
max_logins_type = type(max_logins)
# Display `max_logins_type`
print(max_logins_type)

# Assign `login_attempts` to the value 
login_attempts = 2
# Assign `login_attempts_type` to the data type of `login_attempts`
login_attempts_type = type(login_attempts)
# Display `login_attempts_type`
print(login_attempts)
# Assign `login_status` to the Boolean value False
login_status = 5
# Assign `login_status_type` to the data type of `login_status`
login_status_type = type(login_status)
# Display `login_status_type`
print(login_status_type)


#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#
#Conditional statements in python 
