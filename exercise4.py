name , age = input("enter name and age ").split(",")
age = int(age)
if age > 10 and (name[0]=='a' or name[0]=='A'):
    print("you can watch movie")
else:
    print("you cannot watch movie")