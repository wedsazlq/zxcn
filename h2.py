


# febnacii

# 0 1 1 2 3

a = 0
b = 1

#res = a + b  1
#a = b, b = res, res = a + b   2
res = 0
print(a)
while res < 100:
	res = a + b
	print(res, end=",")
	a = b
	b= res
#另一种方法求得 febacii
a, b = 0 , 1
while a < 100:
	print(a, b)	
	a, b = b, a + b

