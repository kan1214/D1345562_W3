a=float(input('輸入係數a：'))
b=float(input('輸入係數b：'))
c=float(input('輸入係數c：'))
import math
d=math.sqrt(b**2-4*a*c)
x1=(-b+d)/2*a
x2=(-b-d)/2*a
print('x1 =',x1,end='')
print(', x2 =',x2)