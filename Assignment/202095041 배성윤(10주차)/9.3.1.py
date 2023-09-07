class PolyArea :

     pi=3.14159

     def rectangleArea(self,width,depth) :
          return width*depth

     def triangleArea(self,base,height) :
          return base*height/2

     def circleArea(self,r) :
          return self.pi*r*r

     def circumference(self,r) :
          return 2*self.pi*r

pa=PolyArea()

print('가로 세로가 10과 20인 사각형의 넓이 :',pa.rectangleArea(10,20))

print('밑변이 10이고, 높이가 19인 삼각형의 넓이 :',pa.triangleArea(10,19))

print('반지름이 5인 원의 넓이는 :',pa.circleArea(4))

print('반지름이 5인 원의 둘레는 :',pa.circumference(4))
