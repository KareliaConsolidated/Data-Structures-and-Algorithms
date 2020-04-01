def karatsuba(n1,n2):
	if len(str(n1)) != len(str(n2)):
		return "Length Must be Equal !"
	length_n1 = int(len(str(n1)))//2
	length_n2 = int(len(str(n2)))//2
	a = int(str(n1)[:length_n1])
	b = int(str(n1)[length_n1:])
	c = int(str(n2)[:length_n2])
	d = int(str(n2)[length_n2:])
	n = int(len(str(n1)))
	return ((10**n)*a*c) + ((10**(n/2))*((a*d)+(b*c))) + (b*d)

print(int(karatsuba(1234, 5678))) # 7006652

print(int(karatsuba(788952, 123452))) # 97397702304