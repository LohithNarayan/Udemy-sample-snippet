# Given String  
str = "RINGCENTRAL"  
str1="INDIA"
# Start Oth index to end  
print(str[0:])  
# Starts 1th index to 4th index  
print(str[1:5])  
# Starts 2nd index to 3rd index  
print(str[2:4])  
# Starts 0th to 2nd index  
print(str[:3])  
#Starts 4th to 6th index  
print(str[4:7])  

#########################
print('negative slicing in the string')
print(str[-1])  
print(str[-3])  
print(str[-2:])  
print(str[-4:-1])  
print(str[-7:-2])  
# Reversing the given string  
print(str[::-1])  

##############################################
   
print(str*3) # prints RINGCENTRAL THRICE   
print(str+str1)# prints  RINGCENTRAL INDIA  
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('W' in str) # prints false as w is not present in str    
print('CEN' not in str1) # prints false as CEN is present in str1.     
#print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : RINGCENTRAL     