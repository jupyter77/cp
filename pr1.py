a,b= map(int,input("Enter the two numbers").split())
start=min(a,b)
end=max(a,b)
maximum=0

for i in range(start,end+1):
	n=i
	count=1
	while n>1 :
		if n%2==0:
			n=n//2
		else:
			n=3*n+1
		count=count+1
	if count>maximum:
		maximum=count
print("maximum count is :",maximum)
		