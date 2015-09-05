import os
def set(n):
	if not isinstance(n,int):
		raise ValueError("not int")
	return "n="+str(n)

if __name__ == '__main__':
	print(set(5))
	print('end')
	set('s')

