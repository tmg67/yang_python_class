
for  x in "banana":
    print(x)

a = "Hello world!"
print("length ===", len(a))

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello,Yangji!"
print(b[5:8])
print(b[:8])
print(b[5:])
print(b[-1:-8])

a = " He                       llo, Wor                   ld! "
print(a.strip())

a = " Hello, World! "
print(a.replace("H", "y"))

a = "Hello, World, yangji!"
print(a.split(","))

name = input(" enter your name")

print("you have enter your name = " + name)#string concant
print(f"you have enter your name = {name}")#format string
print("you have enter your name = %s" % (name))# modulus string

