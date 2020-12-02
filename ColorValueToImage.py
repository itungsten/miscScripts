from PIL import Image
width=WIDTH
height=HEIGHT
path=PATH
# line等于width*height
# 这个是把每行的颜色值转化为一张图片
# 建议使用wc数一数行数，再对行数因数分解
res=Image.new('RGB', (width+10, height+10), (255, 255, 255))
with open(path,'r') as f:
	i=0
	lines=f.readlines()
	for line in lines:
		line=line.strip('\n').split(',')
		line=[int(i) for i in line]
		line=tuple(line)
		pos=(int(i/width),i%width)
		i=i+1
		res.putpixel(pos,line)
res.save('ans.png')