# Creating an empty Dictionary       
Dict = {}       
print("Empty Dictionary: ")       
print(Dict)       
      
# Creating a Dictionary       
# with dict() method       
Dict = dict({1: 'Hcl', 2: 'WIPRO', 3:'Facebook'})       
print("\nCreate Dictionary by using  dict(): ")       
print(Dict)       
      
# Creating a Dictionary       
# with each item as a Pair       
Dict = dict([(4, 'Rinku'), (2, 'Singh')])       
print("\nDictionary with each item as a pair: ")       
print(Dict)       

#Accessing dictionary values
Employee = {"Name": "Dev", "Age": 20, "salary":45000,"Company":"WIPRO"}      
print(type(Employee))      
print("printing Employee data .... ")      
print("Name : %s" %Employee["Name"])      
print("Age : %d" %Employee["Age"])      
print("Salary : %d" %Employee["salary"])      
print("Company : %s" %Employee["Company"]) 