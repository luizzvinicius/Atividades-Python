class Valores:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print("está somando os valores.")
        return Valores(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"x = {self.x}, y = {self.y}"

    def to_string(self):
        return f"x = {self.x}, y = {self.y}"


n1 = Valores(10, 60)
n2 = Valores(20, -30)
n3 = n1 + n2
print(n1)
print(n3.to_string())
