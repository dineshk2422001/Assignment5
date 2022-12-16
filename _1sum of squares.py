class Point:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def sqSum(self):
        sq1=self.x**2
        sq2=self.y**2
        sq3=self.z**2
        sqtotal=sq1+sq2+sq3
        print('Sum of the squares:',sqtotal)


obj=Point(1,3,5)
obj.sqSum()