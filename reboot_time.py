#!/usr/bin/python
import commands
str=commands.getstatusoutput("last reboot -F | head -32 | awk '{print $8,$10,$14}'")
l=str[1].splitlines()
l.pop(0)
l.pop(0)
for k in l:
	print k
time=[]
for y in range(0,len(l)-1):
	a= int(l[y].split("-")[0].split(":")[0])*60*60 +int(l[y].split("-")[0].split(":")[1])*60 + int(l[y].split("-")[0].split(":")[2])
	b= int(l[y+1].split("-")[1].split(":")[0])*60*60+int(l[y+1].split("-")[1].split(":")[1])*60 + int(l[y+1].split("-")[1].split(":")[2])
	time.append(a-b)
sum=0
for x in time:
	print x

print "average time - %s " %(float(sum(time)) / len(time))
print  "max time - %s " %(max(time)) 	
