import os
    
lines = [line.rstrip('\n') for line in open('/home/ajay/CD/Project/complex.py')]   
#print(lines)

print("No of lines of code",len(lines))
def getindent(s):
	leading_spaces = len(s) - len(s.lstrip())
	return leading_spaces

j=0 #initialize j

while(j<len(lines)):
	flag=0
	if(":" in lines[j] and ("def" in lines[j])):
		scope=1
		j=j+1
		c=getindent(lines[j])
		#print(c)
		while((j<len(lines)) and (scope>0)):
			if((getindent(lines[j])!=c) and ("return" not in lines[j])):
				print("INDENT error at line no 1",j+1)
				flag=1
				scope=0
				break
			elif((getindent(lines[j])!=c) and ("return" in lines[j])):
				print("INDENT error at line no 2",j+1)
				flag=1
				scope=0
				break
			elif((getindent(lines[j])==c) and (":" in lines[j])):
				scope=2
				j=j+1
				c1=getindent(lines[j])
				#print(c1,j)
				while((j<len(lines)) and (scope==2)):
					if((getindent(lines[j])!=c1) and ("return" not in lines[j])):
						print("INDENT error at line no...",j+1)
						flag=1
						scope=1
						#j=k
						#break
					elif((getindent(lines[j])!=c1) and ("return" in lines[j])):
						print("INDENT error at line no...",j+1)
						flag=1
						scope=1
						#j=k
						#break
					elif((getindent(lines[j])==c1) and ("return" in lines[j])):
						scope=1
						j=j+1
						#j=k
						#break
					else:
						j=j+1
						#j=j+1
				#break	
			
			
			
			
			elif("if" in lines[j] and (":" in lines[j]) and (getindent(lines[j])==c)):
				j=j+1
				ifscope=1
				f=0
				c2 = getindent(lines[j])
				j=j+1
				while(j<len(lines) and (ifscope>0) and (f==0)):
					if((getindent(lines[j])!=c2) and ("print" in lines[j])):
						print("INDENT error at",j+1)
						j=j+1
						f=1
						ifscope=0
					elif((getindent(lines[j])!=c2) and ("print" not in lines[j])):
						print("INDENT error at ",j+1)
						j=j+1
						f=1
						#ifscope=0
					elif(("print" in lines[j])):
						j=j+1
						ifscope=0
					elif(("if" in lines[j] and (":" in lines[j])) or (("else" in lines[j]) and (":" in lines[j]))):
						ifscope=2
						j=j+1
						c3=getindent(lines[j])
						j=j+1
						while(j<len(lines) and (ifscope==2)):
							if((getindent(lines[j])!=c3) and ("print" in lines[j])):
								print("INDENT error at",j+1)
								j=j+1
								f=1
								ifscope=1
							elif((getindent(lines[j])!=c3) and ("print" not in lines[j])):
								print("INDENT error at ",j+1)
								j=j+1
								f=1
							elif("print" in lines[j] and (getindent(lines[j])==c3)):
								j=j+1
								ifscope=1

			
			
					elif("else" in lines[j] and (":" in lines[j])):
						j=j+1
						elsescope=1
						f1=0
						c4 = getindent(lines[j])
						j=j+1
						while(j<len(lines) and (elsescope>0) and (f1==0)):
							if((getindent(lines[j])!=c4) and ("print" in lines[j])):
								print("INDENT error at",j+1)
								j=j+1
								f1=1
								elsescope=0
							elif((getindent(lines[j])!=c3) and ("print" not in lines[j])):
								print("INDENT error at ",j+1)
								j=j+1
								f1=1
								#ifscope=0
							elif(("print" in lines[j])):
								j=j+1
								elsescope=0
							elif("else" in lines[j] and (":" in lines[j])):
								elsescope=2
								j=j+1
								c5=getindent(lines[j])
								j=j+1
								while(j<len(lines) and (elsescope==2)):
									if((getindent(lines[j])!=c5) and ("print" in lines[j])):
										print("INDENT error at",j+1)
										j=j+1
										f1=1
										elsescope=1
									elif((getindent(lines[j])!=c5) and ("print" not in lines[j])):
										print("INDENT error at ",j+1)
										j=j+1
										f1=1
									elif("print" in lines[j] and (getindent(lines[j])==c5)):
										j=j+1
										elsescope=1
									else:
										j=j+1
							else:
								j=j+1
			
			               
					else:
			
						j=j+1
		
			else:
				j=j+1
	

	elif("if" in lines[j] and (":" in lines[j])):
		j=j+1
		ifscope=1
		f=0
		c2 = getindent(lines[j])
		j=j+1
		while(j<len(lines) and (ifscope>0) and (f==0)):
			if((getindent(lines[j])!=c2) and ("print" in lines[j])):
				print("INDENT error at",j+1)
				j=j+1
				f=1
				ifscope=0
			elif((getindent(lines[j])!=c2) and ("print" not in lines[j])):
				print("INDENT error at ",j+1)
				j=j+1
				f=1
				#ifscope=0
			elif(("print" in lines[j])):
				j=j+1
				ifscope=0
			elif(("if" in lines[j] and (":" in lines[j])) or (("else" in lines[j]) and (":" in lines[j]))):
				ifscope=2
				j=j+1
				c3=getindent(lines[j])
				j=j+1
				while(j<len(lines) and (ifscope==2)):
					if((getindent(lines[j])!=c3) and ("print" in lines[j])):
						print("INDENT error at",j+1)
						j=j+1
						f=1
						ifscope=1
					elif((getindent(lines[j])!=c3) and ("print" not in lines[j])):
						print("INDENT error at ",j+1)
						j=j+1
						f=1
					elif("print" in lines[j] and (getindent(lines[j])==c3)):
						j=j+1
						ifscope=1
					else:
						j=j+1
			else:
				j=j+1

	else:
		j=j+1
	
	break
