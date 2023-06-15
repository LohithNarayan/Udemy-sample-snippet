x=0
while x<5:
    print(f'The current value of x is {x}')
    x=x+1
else:
    print("now x is not less than 5")

    ##############
    #'continue' key example

    mystring="sammy"
    for letter in mystring:
        if letter=="a":
            continue
        print(letter )
        print("the below example for break key")

        ###############
        #"break" key example

        mystring="lohith"
        for letter in mystring:
         if letter=="l":
            break
        print(letter)

        
