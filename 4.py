a=int(input('輸入一個三位數：'))
b=a//100
c=a//10%10
d=a%100%10
print('每位數字總和：',d+b+c)