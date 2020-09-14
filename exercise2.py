name, char=input("enter you name and character : ").split(",")
print(f"count of character in name is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}")