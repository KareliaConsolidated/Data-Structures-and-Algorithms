# Write a recursive function called reverse which accepts a string and returns a new string in reverse
def reverse(stri):
	if len(stri) <= 1: return stri
	return reverse(stri[1:]) + stri[0]
	
print(reverse('awesome')) # emosewa
print(reverse('flipkart')) # trakpilf
print(reverse('amazon')) # nozama