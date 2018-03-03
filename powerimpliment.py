
def pow(x,n,p):
	if n==0:
		return 1%p
	if (n &1 ):
		return (abs((x*pow(x,int(n/2),p)*pow(x,int(n/2),p))%p))
	else:
		return (abs((pow(x,int(n/2),p)*pow(x,int(n/2),p))%p))
if __name__ == '__main__':
	x=int(input("enter value for x"))
	n=int(input("enter value for y"))
	p =int(input("enter value for p"))
	print("the result is %d"%pow(x,n,p))
	
