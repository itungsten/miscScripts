path='data.txt'
f=open(path,'r').read()
ans=''
for i in range((int(len(f)/7))):
	sub=f[i*7:i*7+7]
	sub=int(sub,2)
	ans=ans+chr(sub)
print(ans)