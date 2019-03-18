def is_vowel(c): 
	return ((c == 'a') or (c == 'e') or
			(c == 'i') or (c == 'o') or
			(c == 'u')); 

X =list(map(str,input()))
print(X[0], end = "");
for i in range(1,len(X)): 
		if ((is_vowel(X[i - 1]) != True) or
			(is_vowel(X[i]) != True)): 
			
			print(X[i], end = ""); 
