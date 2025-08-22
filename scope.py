age=20
def hello():
    name = "sameer"
    global age
    print(age)
    age=29
    print(age)
    print(name)

hello()
