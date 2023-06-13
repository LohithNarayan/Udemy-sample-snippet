'''
st='Prints only the words that starts with s in this sentence'
for word in st.split():
    if word[0]=='s':
       print(word)
       '''

###################
'''
  #Use range to print all the even numbers 0 to 100
list(range(0,100))
for n in range(0,100):
  
 print (n)
 '''
 ########################
'''
#list comprehension ,1-50 divisible by 3
print([x for x in range(0,50)if x%3==0])
'''
#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
'''
for num in range(0,100):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz") 
    else:
        print(num)
'''
#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])