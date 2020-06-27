6#
s=open("content.txt","r")
for i in s:
	print(i.readline())
s.close