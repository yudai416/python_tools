def split_str(buf, n):
	result = [''.join(x) for x in zip(*[buf[i::n] for i in range(n)])]
	return result + (lambda x: [buf[-x:]] if x else [])(len(buf) % n)
	
buf = 'dfhdashfodshofhdsaohsf'
print split_str(buf, 3)
