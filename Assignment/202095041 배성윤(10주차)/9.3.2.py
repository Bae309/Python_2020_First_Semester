class Box:

     def volume(self,width=1,depth=1,height=1) :
          vol=width*depth*height
          return width,depth,height,vol

b1=Box()

w,d,h,v=b1.volume()
print("박스의 가로 : ",w,"박스의 세로 : ",d,"박스의 높이 : ",h,"박스의 부피 : ",v)

w,d,h,v=b1.volume(10)
print("박스의 가로 : ",w,"박스의 세로 : ",d,"박스의 높이 : ",h,"박스의 부피 : ",v)

w,d,h,v=b1.volume(10,20)
print("박스의 가로 : ",w,"박스의 세로 : ",d,"박스의 높이 : ",h,"박스의 부피 : ",v)

w,d,h,v=b1.volume(10,20,30)
print("박스의 가로 : ",w,"박스의 세로 : ",d,"박스의 높이 : ",h,"박스의 부피 : ",v)

