from PIL import Image
width=45
height=45
path='data.txt'
# 这个是把零一矩阵转化为一张黑白图片
white=(255,255,255)
black=(0,0,0)
res=Image.new('RGB', (width+10, height+10), white)
with open(path,'r') as f:
	i=0
	lines=f.readlines()
	for i in range(height):
		for j in range(width):
			line=lines[i].strip('\n')
			flag=line[j]
			if(flag=='1'):
				res.putpixel((i,j),black)
			else:
				res.putpixel((i,j),white)
res.save('ans.png')