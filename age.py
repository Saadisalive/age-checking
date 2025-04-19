try:
    age = int(input("Enter age"))
    if(age<18):
        raise ValueError
    else:
        print("the age is correct")
except ValueError:
    print("The is correct")
if age/2:
    print("it is an even number")
else:
    print("it is an even number ")   