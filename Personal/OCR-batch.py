import os
chapter=3
start=0
end=15

str = [[] for i in range(end-start + 1)]

for i in range(start,end+1):
	str[i] = "ch{}_{}.png".format(chapter, i)
	cmd = "tesseract {} ch{}_{}".format(str[i], chapter, i) 
	os.system(cmd)
