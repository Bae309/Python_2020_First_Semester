class PlusMinus:

     def _init_(self,x,y):
          self.sum=x+y
          self.minus=x-y

     def result(self):
          return self.sum, self,minus

x=int(input("첫번째 숫자 : "))
y=int(input("두번째 숫자 : "))

pm=PlusMinus(x,y)

a,b=pm.result()
print('입력한 두 수의 합 : ',a)
print('입력한 두 수의 차 : ',b)

