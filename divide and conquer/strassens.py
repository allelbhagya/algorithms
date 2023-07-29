matrix1 = [[1,2],[3,4]]
matrix2 = [[5,6],[7,8]]

a,e = 1,5
b,f = 2,6
c,g = 3, 7
d,h = 4, 8

p1 = a*(f-h)
p2 = (a+b)*h
p3=(c+d)*e
p4 = d*(g-e)
p5 = (a+d)*(e+h)
p6=(b-d)*(g+h)
p7=(a-c)*(e+f)

c11=p5+p4-p2+p6
c21 = p1+p2
c12=p3+p4
c22=p1+p5-p3-p7
res = [[c11,c12],[c21,c22]]

print(res)