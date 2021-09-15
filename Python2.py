a = int(input("Interval A: "))
b = int(input("Interval B: "))

for x in range(a, b):

	revers = int(str(x)[::-1])
	if (revers<b) and (revers>a):
		print(x , revers)
	x = x + 1
print("Finis")

