from PIL import Image
width=240
height=240
path='ans.bmp'
# 这个是把一张图片转化为零一矩阵
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
map=Image.open(path).convert('RGB')

for i in range(height):
	for j in range(width):
		p=map.getpixel((j,i))
		if(p==green):
			print('0',end='')
		else:
			print('1',end='')
	print('')