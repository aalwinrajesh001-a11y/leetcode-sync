def basic_details():

	p=input("\tPROBLEM NAME : ")
	t=input("\tPROBLEM TOPIC : ")
	l=input("\tLANGUAGE : ")
	return p,t,l

def input_code():
	
	print("\n\nEnter the copied code here (Type 'END' in a new line when finished) : \n")
	lines=[]
	while True:
        	line=input()
        	if line=='END':
                	break
	        lines.append(line)
	code="\n".join(lines)
	return code,len(lines)

def check_details(p,t,l,c):
        print(f"\n\nDETAILS :\n\t PROBLEM NAME :{p}\n\t TOPIC : {t}\n\t LANGUAGE : {l}\n\t CODE : \n{c} ")
