from PIL import Image
width=124
height=70
nums=9
prefix='IMG0000'
suffix='.bmp'
# the path is prefix+str(i)+suffix

res=Image.new('RGB', (width, height), (255, 255, 255))
#创建白色画布    

for i in range(nums):
	path=prefix+str(i)+suffix
	pic=Image.open(path).convert('RGB')
	for j in range(width):
		for k in range(height):
			pixel=pic.getpixel((j,k))
			resPixel=res.getpixel((j,k))
			res.putpixel((j,k),min(resPixel,pixel))
			#黑色最小
res.save('ans'+suffix)
