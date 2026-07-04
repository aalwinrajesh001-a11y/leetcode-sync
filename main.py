import os
print("\n\n\tLEETCODE-SYNC TOOL\n\n")
problem_name=input("PROBLEM NAME : ")
topic=input("\nPROBLEM TYPE : ")
language=input("\nLANGUAGE : ")
print("\nEnter the copied code here (Type 'END' in a new line when finished) : \n")
lines=[]
while True:
	line=input()
	if line=='END':
		break
	lines.append(line)
code="\n".join(lines)
os.system('clear')
print(f"\nSUCCESSFULLY ADDED {len(lines)} LINES OF CODE.")
cn=input("\nDo you want to Check or Push to github (y/n)? ")
os.system('clear')
if cn=='y':
	print(f"\n\nDETAILS :\n\t PROBLEM NAME :{problem_name}\n\t TOPIC : {topic}\n\t LANGUAGE : {language}\n\t CODE : \n{code} ")
	print("PRESS Y TO CONFIRM AND PUSH OR N TO EDIT CODE ")
else:
	print("PUSHED SUCCESSFULLY!")
	

