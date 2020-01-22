def pascal_triangle(n): 

	for i in range(1, n + 1): 
		count = 1 
		for j in range(1, i + 1): 
			
		
			print(count, end = " ")
			count = int(count * (i - j) / j)
		print("")

 
user_input = int(input("Enter the number of row : "))
pascal_triangle(user_input)

 
