#!/usr/bin/python3

input="13322222"

i=0
output=[]
prev=0

while(i<len(input)-1):
	if (input[i]<=input[i+1]):
		output.append(input[i])
		i+=1
	elif (prev==1):
		output.append("9")
		i+=1 
	else:
		prev=1
		el=int(input[i])-1
		output.append(str(el))
	
out_str=""
print(out_str.join(output))
