def make_card(name,age,message="Have a good day!"):
    
    name =input("Enter your name: ")
    age = int(input("Enter your age: "))
    return f"Hello {name}({age} years old)!\n{message}"
    
res = make_card("Sameer",20)
print(res)
