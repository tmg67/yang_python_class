#example 1: operator overrloading
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return vector(self.x - other.x, self.y - other.y)
    def __mul__(self,scalar):
        return vector(self.x * scalar, self.y * scalar)
    def __str__(self):
        return f"vector: ({self.x}, {self.y})"
    #example 2:using operator overloading for vector addition
v1 = vector(1,2)
v2 = vector(3,4)
v3 = vector(3,4)
v4 = vector(3,4)
result_vector = v1 +v2
print(result_vector)
#rxample 1: operator overloading

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,*other):
        sum_vector = Vector(self.x,self.y) 
        for other in others:
            sum_vector = Vector(sum_vector.x + other.x,sum_vector.y + other.y)

        return sum_vector
    def __sub__(self,*other):
        sub_vector = Vector(self.x,self.y)
        for other in others:
            sub_vector = Vector(sub_vector.x - other.x,sub_vector.y - other.y)
        return sub_vector
    def __mul__(self,*other):
        mul_vector = Vector(self.x,self.y)
        for other in others:
            mul_vector = Vector(mul_vector.x * other.x, mul_vector.y * other.y)
        return mul_vector
    def __str__(self):
        return f"Vector: ({self.x}, {self.y})"   