a,b=0,1
out=[a,b]
n=int(input("enter the no.of numbers that u wanna print in the fibbanoci series"))
for i in range(n-2):
          c=a+b
          out.append(c)
          a,b=b,c
print(out)
