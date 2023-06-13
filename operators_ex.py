#range operator
#range operator
print("Below is the range operator")
mylist=[1,2,3]
for num in range(0,10,2): #skips 2 digits
     print(num)

#indexing with enumerator    
word='abcd'
for index,letter in enumerate(word):
     print(index)
     print(letter)
     print('\n')

     #zip operator
num=[1,2,3]
list2=['a','b','c']
num2=[100,200,300]
for item in zip(num,list2,num2):
     print(item)
