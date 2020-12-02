st='BABABBBBABBA ABA AB B AAB ABAA AB B AA BBB BA AAA BBAABB AABA ABAA AB BBA BBBAAA ABBBB BA AAAB ABBBB AAAAA ABBBB BAAA ABAA AAABB BB AAABB AAAAA AAAAA AAAAB BBA AAABB'
ans=''
for i in range(len(st)):
	if(st[i]==' '):
		ans+=' '
	if(st[i]=='B'):
		ans+='-'
	if(st[i]=='A'):
		ans+='.'
print(ans)