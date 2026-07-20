class circle:
    def __init__(self, r):
        self.r = r
    def calculate(self):
        area=3.14*self.r*self.r
        p=2*3.14159*self.r
        print("area:", area)
        print("Perimeter:", p)
c1=circle(3.3)
c1.calculate()