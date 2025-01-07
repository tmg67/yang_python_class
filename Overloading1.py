class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, *other):
        sum_vector = Vector(self.x, self.y) 
        for other in others:
            sum_vector = Vector(sum_vector.x + other.x, sum_vector.y + other.y)

            return sum_vector

    def __sub__(self, *other):
        sub_vector = Vector(self.x, self.y)
        for other in others:
            sub_vector = Vector(sub_vector.x - other.x, sub_vector.y - other.y)

            return sub_vector
    def __mul__(self, *other):
        mul_vector = Vector(self.x, self.y)
        for other in others:
            mul_vector = Vector(mul_vector.x * other.x, mul_vector.y * other.y)

            return mul_vector

    def __str__(self):
        return f"Vector: ({self.x}, {self.y})"   