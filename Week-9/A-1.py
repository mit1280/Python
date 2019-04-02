def spiralPrint(m, n, a) : 
	k = 0; l = 0

	''' k - starting row index 
		m - ending row index 
		l - starting column index 
		n - ending column index 
		i - iterator '''
	

	while (k < m and l < n) : 
		for i in range(l, n) : 
			print(a[i][k], end = " ") 
			
		k += 1

		for i in range(k, m) : 
			print(a[n-1][i], end = " ") 
			
		n -= 1

		if ( k < m) : 
			
			for i in range(n - 1, (l - 1), -1) : 
				print(a[i][m-1], end = " ") 
			
			m -= 1
		
		if (l < n) : 
			for i in range(m - 1, k - 1, -1) : 
				print(a[l][i], end = " ") 
			
			l += 1

p= int(input())
m = []
for i in range(1,p+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
		

spiralPrint(p,p, m) 
