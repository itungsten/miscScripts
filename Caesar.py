path='data.txt'
beg=-25
end=25
text=open(path,'r').read()
def move(step):
	print('move '+str(step)+' :')
	for i in range(len(text)):
		ele=text[i:i+1]
		if(ele.isalpha()):
			ele=ord(ele)+step
			ele=chr(ele)
		print(ele,end='')
	print('')
for i in range(beg,end):
	move(i)