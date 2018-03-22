
#100的前n向和

sum_res = 0
num = 100
#a = a + 1


while num > 0:
	#如果是偶数则累加-----> if   %
	if num % 2 == 0:

		sum_res = sum_res + num
	num = num -1
    
print(sum_res)

#方法2

i = 0
num = 0

while num <= 100:
	i = i+ num
	num = num + 1

print(i)


