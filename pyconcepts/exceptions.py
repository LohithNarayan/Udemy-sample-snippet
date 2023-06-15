'''
try:
    for i in ["a","b","c"]:
      print(i**2)
except:
   print("this is not going to execute")
   '''
'''
try:
    x=5
    y=0
    z=x/y
except:
        print("error !")
finally:
    print("All done")        
    '''

def ask():
    while True:
        try:
            n=int(input("Enter a number"))
        except:
            print("Try again")
            continue
        else:
            break
    print(n**2)    
ask()    