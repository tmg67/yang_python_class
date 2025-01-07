class person: ##blue print
    def __init__(self, name, age):##dunder method or magic : self call, __init__: runs when ojject created
        self.name = name
        self.age = age
        #def __init__(self):
        #pass
        #pass

ruman = Person("Ruman", 27)

print(ruman.name)
print(ruman.age)


class PhoneFactory:
    model: None
    color: None
    is_android: None