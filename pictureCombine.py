from PIL import Image
width=240
height=240
nums=576
prefix='IMG'
suffix='.bmp'
# the path is prefix+str(i)+suffix

white=(255,255,255)
black=(0,0,0)

res=Image.new('RGB', (width, height), black)
# fill with black color

for i in range(nums):
	path=prefix+(str(i)).rjust(5,'0')+suffix
	# print(path)
	pic=Image.open(path).convert('RGB')
	for j in range(width):
		for k in range(height):
			pixel=pic.getpixel((j,k))
			resPixel=res.getpixel((j,k))
			res.putpixel((j,k),max(resPixel,pixel))
res.save('ans'+suffix)
